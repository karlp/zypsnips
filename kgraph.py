#!/usr/bin/env python
from __future__ import division
import struct
import matplotlib
import matplotlib.pyplot as plot
import multiprocessing
import numpy
import math
import subprocess
import tempfile

import gdb
import gdb.types

# GDB plugin for loading/saving/graphing memory

__author__ = "Karl Palsson <karlp@remake.is>"

__usage__ = """
(gdb) source kgraph.py
(gdb) display $kanalyse(*(state.adc_buff)@actual_count, start_samp)
or
(gdb) kgraph *(state.adc_buff)@actual_count start_samp

Or any array of digits really.... start_samp is the zero point to use

kgraph _requires_ 
```
set print elements 0
set print array-indexes off
```
As it's parsing the string representation to load the values.  This was
a workaround for the gdb/python interface when this was written, in 2014/15
but could hopefully be replaced with something more API oriented these days.
"""

class Utils:
    def calcrms(self, data, zero):
        sumsq = 0
        mymax = 0
        mymaxi = 0
        mymin = 100000000
        mymini = 0
        for i,q in enumerate(data):
            if q > mymax:
                mymax = q
                mymaxi = i
            if q < mymin:
                mymin = q
                mymini = i
            sumsq += (q - zero) * (q - zero)
        mean = sumsq / len(data)
        #return (0, mymaxi, mymini)
        return (math.sqrt(mean), mymaxi, mymini)

    def crunch(self, x):
        # the fuck? there's no gdb.types?
        #print("which is...", gdb.types.get_basic_type(x.type))
        print("which is type: ", x.type)
        print(f"which is of code: {x.type.code} vs type_code_array: {gdb.TYPE_CODE_ARRAY}?")
        if x.type.code == gdb.TYPE_CODE_ARRAY:
            # We _know_ it's an array
            type_as_str = str(x.type)
            brace_pos = type_as_str.find('[')
            brace_pos2 = type_as_str.find(']')
            klen = int(type_as_str[brace_pos+1:brace_pos2])
            print(f"Explicit array of length: {klen}")
            vals = [eval(str(x[i])) for i in range(klen)]
            return vals
            
        else:
            # from gdb-plot-0.0.3
            # But surely there is a better way of doign it ?
            x_str = str(x)
            brace_pos = x_str.find('{')
            brace_pos2 = x_str.find('}')
            x_str = '[ %s ]' % x_str[ brace_pos+1:brace_pos2]
            s = eval( '%s' % x_str )
            return s
    

def make_format_string_numeric(size, signed):
	ch = ""
	if size == 1: ch = "B"
	if size == 2: ch = "H"
	if size == 4: ch = "I"
	if size == 8: ch = "L"
	if signed: ch = ch.lower()

	return ch
    

class KAnalyse(gdb.Function):
    def __init__(self):
        gdb.Function.__init__(self, "kanalyse")
        self.kk = Utils()

    def invoke(self, buff, zero):
        data = self.kk.crunch(buff)
        (rms, maxi, mini) = self.kk.calcrms(data, int(zero))
        return "RMS: %f, max: %d, min:%d, n=%d, start=%d" % (rms, data[maxi], data[mini], len(data), zero)

class KLoad(gdb.Command):
    name = "kload"
    """
    Load a python array (that can be eval'ed) from a file into memory at position x
    """
    def __init__(self):
        gdb.Command.__init__(self, self.name, gdb.COMMAND_DATA, gdb.COMPLETE_FILENAME, True)

    def invoke(self, arg, from_tty):
        args = gdb.string_to_argv(arg)
        if len(args) != 2:
            print("Usage: %s <file> <address>" % self.name)
            return

        source = gdb.parse_and_eval(args[1])
        addr = int(str(source), 0)
        path = os.path.expanduser(args[0])
        print("trying to use file :%s, addr:%#x" % (path, addr))
        points = eval(open(path).read())
        dest = source.dereference().type
        elem_size = dest.sizeof

        # A little hacky....
        signed = True
        if str(dest)[0] == 'u':
            signed = False
        fmt = "<%d%s" % (len(points), make_format_string_numeric(elem_size, signed))
        print("Loading %d points from file into %#x as signed: %s elem_size:%d" % (len(points), addr, signed, elem_size))
        output = struct.pack(fmt, *points)
        gdb.selected_inferior().write_memory(addr, output)

class KRead(gdb.Command):
    name = "kread"
    def __init__(self):
        gdb.Command.__init__(self, self.name, gdb.COMMAND_DATA, gdb.COMPLETE_SYMBOL, True)

    def invoke(self, arg, from_tty):
        args = gdb.string_to_argv(arg)
        print(args)
        signed = False
        if len(args) < 2:
            print("Usage: %s <object> <length in elements> [signed]" % (self.name))
            return
    	# This is ugly, but so be it.
        source = gdb.parse_and_eval(args[0])
        addr = int(str(source), 0)
        length = int(args[1], 0)
        if len(args) > 2 and args[2] == "signed":
            signed = True
        elem_size = source.dereference().type.sizeof
        print("address = %#x, length = %d, signed = %s, size of each :%d" % (addr, length, signed, elem_size))
        q = gdb.selected_inferior().read_memory(addr, length * elem_size)
        fmt = "<%d%s" % (length, make_format_string_numeric(elem_size, signed))
        undone = struct.unpack(fmt, q)
        for qq in undone:
            print("%#x (%d)" % (qq, qq))


class KGraph(gdb.Command):
    def __init__(self):
        gdb.Command.__init__(self, "kgraph", gdb.COMMAND_DATA, gdb.COMPLETE_SYMBOL, True)
        self.kk = Utils()

    def invoke(self, arg, from_tty):
        args = gdb.string_to_argv(arg)
        zero = 0
        if len(args) < 1:
            print('Usage: kgraph <object> [zeropoint]')
            return
        
        x = gdb.parse_and_eval(args[0])
        if len(args) > 1:
       	    zero = int(gdb.parse_and_eval(args[1]))

        data = self.kk.crunch(x)

        (rms, maxi, mini) = self.kk.calcrms(data, zero)

        fig = plot.figure()
        ax = fig.add_subplot(111)
        ax.grid(True)
        label = "%s RMS=%f" % (args[0], rms)
        ax.plot(data, '.', label=label)
        ax.plot((maxi, mini), (data[maxi], data[mini]), "kD", label="max-min")
        plot.figtext(0.01,0.01, "RMS=%f max:%d, min:%d, start=%d" % (rms, max(data), min(data), zero))
        print("rms: %f max:%d, min:%d" % (rms, max(data), min(data)))
        print("maxi/mini at ", maxi, mini)
        leg = ax.legend(loc='upper right')
        leg.get_frame().set_alpha(0.5)

        # Just this makes ctrl-c work, but the plot is never properly drawn...
        #plot.show(block=False) # this lets ctrl-c work again..

        # Just this works for local gdb, but not for gdb server
        #plot.show()

        # This will leave droppings in /tmp, but otherwise xdg-open loses the image!
        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tf:
            fig.savefig(tf)
            subprocess.run(["xdg-open", tf.name])
            #subprocess.Popen(f"xdg-open {tf.name} && sleep 5 && rm -f {tf.name}", shell=True)
            print("immediately after popep")
            #os.unlink(tf.name)
        print("after plot call")


KGraph()
KAnalyse()
KLoad()
KRead()

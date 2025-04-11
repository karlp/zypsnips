#!python3
"""
Decode a binary RTT stream into a csv for plotting.
Expects to be used with a secondary up channel.

Why? Because, sometimes, printf into the classic RTT "terminal" is too expensive.

To use this in your code, you need a buffer...

```C
// section is optional, shown for completeness
static uint8_t __attribute__((section(SEGGER_RTT_BUFFER_SECTION))) ktrace_buf[1024];
```

and some initialization....
```C
    // name of channel is free form
	SEGGER_RTT_ConfigUpBuffer(1, "kTrace", ktrace_buf, sizeof(ktrace_buf), SEGGER_RTT_MODE_NO_BLOCK_SKIP );
```

And then, a structure of data you want to puhs....which _MUST MATCH_ the `frame_fmt` struct
definition below!
(Why is the magic at the end? So that you can use reader.readuntil....)

```C
struct __attribute__((packed)) ktrace {
	uint32_t ts;
	uint32_t inp;
	int32_t filt_f;
	int32_t filt_s;
	char stab_f:1;
	char stab_s:1;
	uint16_t magic;
};
```

And finally, instance your struct, and stuff it out into the up buffer

```C
	struct ktrace k = {
		.magic = 0xcafe,
		.ts = ustime(),
		.inp = v1,
		.filt_f = lowpass_value(f1->filters[0]),
		.filt_s = lowpass_value(f1->filters[2]),
		.stab_f = stable_ok(f1->stabilities[0]),
		.stab_s = stable_ok(f1->stabilities[2])
	};
	uint32_t bytesWritten = SEGGER_RTT_Write(1, (const char*)&k, sizeof(k));

```

Then, finally, finally... actually collect it. Here's an openocd example
```
Open On-Chip Debugger
> rtt channels
Channels: up=3, down=3
Up-channels:
0: Terminal 1024 0
1: kTrace 1024 0        <<< our channel name, informational only.
Down-channels:
0: Terminal 16 0
> rtt server start 9094 1   << serve channel 1 on port 9094
Listening on port 9094 for rtt connections
> 
```

"""
import argparse
import asyncio
import csv
import dataclasses
import struct

# This _MUST_ match your struct definition!
frame_fmt = "<IIiibH"
frame_size = struct.calcsize(frame_fmt)

@dataclasses.dataclass
class KTrace:
    """
    This is your _output_, it does _not_ have to match the struct
    """
    ts: int
    inp: int
    filt_f: int
    filt_s: int
    stab_f: bool
    stab_s: bool


def dissect_frame(frame):
    ts, inp, filt_f, filt_s, flags, magic = struct.unpack(frame_fmt, bytes(frame))
    if magic == 0xcafe:
        return KTrace(ts, inp, filt_f, filt_s, int(bool(flags & (1<<0))), int(bool(flags & (1<<1))))
    return


async def wait_for_ktrace(otps):
    reader, _ = await asyncio.open_connection(opts.host, opts.port)
    lol = await reader.readuntil(b'\xfe\xca')
    with open(opts.ofile, 'w') as csvfile:
        fields = ["ts", "inp", "filt_f", "filt_s", "stab_f", "stab_s"]
        ww = csv.DictWriter(csvfile, delimiter=";", fieldnames=fields)
        ww.writeheader()
        while True:
            dat = await reader.readexactly(frame_size)
            #print("ok, read in", dat)
            f = dissect_frame(dat)
            #print(f)
            ww.writerow(dataclasses.asdict(f))

class DefaultsAndFormattedIntroPlzkthx(argparse.RawDescriptionHelpFormatter,
                                       argparse.ArgumentDefaultsHelpFormatter):
    pass

def get_args():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=DefaultsAndFormattedIntroPlzkthx)
    parser.add_argument("-p", "--port", default=9094, type=int, help="RTT binary port")
    parser.add_argument("--host", default="localhost", type=str, help="Host serving RTT stream")

    parser.add_argument("-f", "--ofile", type=str, help="output filename to write", required=True)

    options = parser.parse_args()
    return options


if __name__ == "__main__":
    opts = get_args()
    asyncio.run(wait_for_ktrace(opts))

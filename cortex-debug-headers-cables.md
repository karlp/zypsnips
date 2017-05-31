## ARM "standard" cortex debug
ARM made a new "standard" for cortex debug, because smaller is cooler y0. [Read their description of it here](http://infocenter.arm.com/help/topic/com.arm.doc.faqs/attached/13634/cortex_debug_connectors.pdf)

The takeaway is, 2x5, in a _svelte_ 1.27mm pitch  
The common older style is 2x10, but in fatduino 2.54mm pitch.

## Cables

[Cable only](http://microcontrollershop.com/product_info.php?products_id=4517)

## Adapters
Helping clutter your desk and let you use two of your existing cables,
for ultimate bigmessowires style.

[Olimex 2.54mm->1.27mm adapter](https://www.olimex.com/Products/ARM/JTAG/ARM-JTAG-20-10/) 
(Also available as [Digikey part number: 1188-1016-ND](http://www.digikey.com/product-search/en?keywords=1188-1016-ND))

Like above, but with "moah fr33d0M" and now supporting windows!
[20pin<->10pin with power options](https://www.oshpark.com/shared_projects/QoUhDy2L)
-> [pic1](http://i.imgur.com/GKRR3Rj.jpg)
-> [pic2](http://i.imgur.com/Y6XAAdP.jpg)


## Board headers

### esden's choice: FTSH-105-01-L-DV-K   (SMT)
not super cheap, (he gets from samtec directly) but it has partial 
shrouding, only around the pins where the key on the cable goes, so it
takes up a lot less space. 
[Digikey partnumber SAM8799-ND](Or just http://www.digikey.com/product-search/en?keywords=SAM8799-ND)

### aandrew's choice: (and other people)
< aandrew> I use the standard everyday fucking used everywhere digikey 1175-1629-nd

* [Digikey 1175-1629-ND (smt)](http://www.digikey.com/product-search/en?keywords=1175-1629-ND)
* [Digikey 1175-1627-ND (pth)](http://www.digikey.com/product-search/en?keywords=1175-1627-ND)

Much much much cheaper, but fully fully shrouded, so more board space.

### englishman's choice: (shrouds and keys are for l0sers)

Note, this is actually _more_ expensive than the shrouded version above.

[Digikey 609-3729-ND](http://www.digikey.com/product-detail/en/amphenol-fci/20021121-00010T4LF/609-3729-ND/2209075)

### englishman's choice2: (shrouds appear to actually be useful)
Right angle, shrouded.  For that low profile look.

* [Digikey A115273-ND (smt)](http://www.digikey.ca/product-detail/en/te-connectivity-amp-connectors/5-104895-1/A115273-ND/2259789)

## Proprietary shit

Some people occasionally espouse the virtues of tag-connect.  They are wrong.

< aandrew> 
> it looks great on paper and if you don't need retention clips (i.e. you aren't oing to be debugging
> with it or flashing 2GB flash via JTAG) it's actually not half bad for press down, flash, done
> but the second you need it to stay there you are drilling four gigantic fucking holes which
> completely eliminates the size advantage of it your other option is two smaller holes and a little
> clip that goes on the bottom, but that only works for about 10 hours or so before the metal
> starts bending and it no longer holds, so you resort to wrapping the thing to the board with 30AWG
> like a spider wraps a fly. which works until you need to take it off
> 
> it's just fail
>
> you want to do debugging? gotta drill those fucking HUGE holes for retention 
> or use the clip on the bottom which works its way loose
> you want tiny footprint? use a fucking bed of nails and 4 test points. way smaller
> want to be frou-frou and have spring contacts on the cheap? Use something like isptouch for *way* cheaper


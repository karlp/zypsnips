## Choosing a FPC/FFC connector.

This is based on Karl's uneducated collection of pieces, he is _not_ an expert in this field!

(Tl;dr, it's a soup, you'd think there'd be more standard footprints, but there's not)

Goals
* Cheap
* well stocked
* multi vendor if available
* uses "standard" 0.3mm thick cables....

### Pitch, 0.5mm or 1.0mm?

0.5mm pitch and 1.0mm pitch are both readily available.  1.0mm pitch is somewhat cheaper from
big distros, at places like lcsc, it's the same.  0.5 is modern, 1.0 is jumbotron :)
1mm will let you run 1A, 0.5mm lets you run 0.5A.

Other pitches are for people who know what they're doing or legacy, they're way less common.

### ZIF or not?

Nominally, non-zif, friction fit are claimed to be less expensive.  Because of volumes, they're actually not.
They _are_ a bit smaller, if that's an acceptable tradeoff.  ALLLL the cheap parts are ZIF

### Right angle or vertical?
This is up to you.  you need to allow space on your board for mating the cable.
Vertical is readily available, but it's ~marginally more expensive at the time of writing.

### Top or bottom contacts?
Bottom is slightly more common, so if you're doing something new, pick that.  Otherwise, you pick this
based on what the connection orientation you need with what you're connecting to.

Most vendors have both options available.  Some even offer contacts on both sides, so you can use whatever
orientation you like.  They are footprint compatible normally.

### Why so many?!
Many of the variations in the product line ups are based on things that may or may not matter to you:

* height (you can get a range from 0.9mm up to 2.5mm, with price decreasing as you get bigger...)
* number of mating cycles
* tin/gold.

(Amphenol, looking at you, 28 different series of 0.5mm pitch!

### Front or back flip?
wtf do you care for?

## Ok, so, what are the parts?

### TE 1734592 (bottom) and 1734839 (top)
This is a "stuffer" style, not a "flip" style, if you care, 
(top contact is 1734839)

Available in kicad out of the box as the 1734839 footprint, which is nominally the top contact, but it's the same thing

### TE 1775333 (bottom) 
This is flip latch style.  it's also cheaper, and apparently newer. It does _not_ have the same footprint as the stuffer style

This is footprint identical to Hirose FH12 series!  . (available in kicad out of the box, if that matters...)

Mounting pads 1.8x2.2
terminals 0.3x1.3
bottom of terminals to top of mounting: 1.5mm

### Hirose tf31
mounting pads: 1.9x2.2
terminals: 0.3x1.3
bottom of terminals to top of mounting: 1.5
(I'd call that compatible with FH12 and teh TE style... good choice...)


So...
Hirose TF31 and FH12 same
FH28 is different, double the vertical spacing to 3.9 bottom to top!
FH19 is low profile, very tight, no appeal to me... (and a different footprint)

### Molex 505110 series.
1.9mm high

Mounting pads 2x1.3
terminals 0.3x1.0
bottom of terminals to top of mounting: 1.55
pads are "wider" set?
(Seems to be compatilble with Mintron XW-05200 on lcsc)

### Molex 54132 series.  (older parts?)
complicated recommended pads...

### Amphenol SFV-R (cheapest on digikey by far)
Only 1.8mm high.   
wonky pads.

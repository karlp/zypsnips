
## POL / ~5.5V buck/buck-boost pin compatible (1-2 cell target stuff)
### DFN10 ~ 3x3mm (SW1+SW2 style)
TPS63000 - 1.8A, 1.8-5.5V, Iq ~50uA, ~1.3MHz  (fixed voltage variants available)
MP2155 - 2.2A - 2-5.5V, Iq ~80uA, ~1MHz
ADP2503 - 0.6A - 2.3-5.5V, Iq ~38uA, ~2.5Mhz (fixed voltage variants available)
ADP2504 - 1A - 2.3-5.5V, Iq ~38uA, ~2.5Mhz (fixed voltage variants available)

### DFN10 ~ 3x3mm ("boost sandwich")
TPS54228 2A, 4.5-18V, Iq ~800uA, 700kHz
RT7280 - 2A, 4.5-18V, Iq ~700uA, 700kHz (Discont)
RT7279 - 2A, 4.5-18V, Iq ~700uA, 700kHz (Forced PWM)

### DFN10 ~ 3x3mm (R-side GND/LX)
NCP1597B - 2A, 4-5.5V, Iq ~1700uA, 1Mhz
TPS62040 - 1.2A, 2.5-6V, Iq ~18uA, 1.25MHz (fixed voltage variants available)

Lots of other stuff uses a slew of wildly incompatible footprints

r2com offered this nugget, so I added ADP250x to the list.
```
07:02 < R2COM> dont use TPS
07:02 < R2COM> lol
07:02 < R2COM> use AD25xx whatever
07:03 < R2COM> they are less noisy
07:03 < R2COM> and more efficient
07:09 < dongs> ADP2503 does look nice
```
TPS/ADP not providing enough juice or takin up too much room, or just out of stock? Feeling like WLCSP? 
Try the ISL91110 today! 1.8v-5.5v in, 1.0v-5.2v out, 2.5mhz, doable on 6/6, price competative!

## Dual/PMIC....
ncp1532
```
03:00 < dongs> im using it everywehre
03:00 < dongs> pretty compact layout with 0402 also
03:00 < zyp> two channels, bunch of current, few external parts
03:02 < dongs> takes up 1cm^2
03:02 < dongs> http://i.imgur.com/CT4cGyf.png
```


## "bigger"
```
20:49 <karlp> so, going through zypsnips for bucks from 12 -> 5V sort of space, not seeing much, did I miss things that were suggested before?
20:50 <qyx> tps62125?
20:50 <zyp> rt7225 or whatever that was called?
20:50 <qyx> but 300 mA only
20:50 <karlp> qyx: yeah, was abotu to say, I want like 3-4A peak
20:50 <qyx> 54240 then?
20:50 <karlp> zyp: yeah, I thought there must be a richtek/mps part somewhere
20:51 <qyx> nobody wants ti :(
20:51 <antto> i'm dumb and i use onsemi's online PSU designer
20:51 <karlp> 54240 looks ok, is that one you've used?
```


RT7257B - 3A, 18V, 1.2MHz sync ~0.50 in singles
TPS54240 - 2.5A, 42V, 100-2500kHz ~$3 in singles
TPS563200 - 3A, 17V, 650kHz, ~0.50 in singles (family with 2A, 3A, 4A and different speeds, TPS56xxxx)
TPS54531 - 5A, 28V, non-sync 570kHz, ~0.50 in singles
AOZ3018 - 5A, 18V, sync 500kHz, ~0.50 in singles



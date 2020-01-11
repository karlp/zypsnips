## build your own
http://de.aliexpress.com/store/407105

## package sizes
```
20:12 < perole> can someone school me on small smd inductor packages/part#?
20:12 < perole> a lot of them have CDxxx names
20:13 < karlp> what's the real question?
20:15 < perole> is there any industry standard for them?
20:15 < perole> or defacto standard?
20:15 < perole> right now, looking for 2.2uh for small switcher
20:19 < qyx> grab some 3225 wirewound or 0805 chip inductor
20:19 < qyx> depends on the parameters
20:19 < aandrew> I'm partial of the 4x4mm package ones
20:19 < qyx> I usually use 3225 because of their good availability
20:19 < qyx> also IHLP series for example
20:20 < qyx> ihlp2525, 4040, etc.
20:20 < qyx> xal series is also good but $$$
20:20 < qyx> also they have quite different footprint so once you make a pcb with their footprint it is 
             hard to fit some alternatives
20:21 < qyx> they are nice cubes
20:21 < qyx> and cheap stores also have DR74, DR125, etc
20:21 < qyx> those are so generic and cheap that even eagle has footprints for them :X
20:23 < qyx> on the 3225 footprint you can also fit 1206 or 0805 and #yolo
20:23 < qyx> (3225 is metric, 1206/0805 imperial)
20:23 < qyx> such mess
20:24 < qyx> eof.
```


## more small inductor sizes
```
08:27:03           invzim | dongs: got a fav inductor for the tiny switchers?
09:01:34            dongs | https://www.zerohedge.com/news/2018-04-05/i-just-discovered-i-owe-irs-50k-i-dont-have-because-i-traded-cryptos
09:01:40            dongs | invzim: SWPA3010
09:01:45            dongs | or pretty much any 3x3mm thing
09:02:00            dongs | theres a ton just pick what you can get from china/whaever
09:06:23           invzim | gracias
09:06:26           invzim | https://lcsc.com/products/Power-Inductors_544.html?sourcePage=product_detail&package=3010&Inductance=2.2uH
09:06:39            dongs | excrtly
09:06:47           invzim | I really like how lcsc makes this game a lot easier
09:06:54            dongs | do not get VLF3010  
09:07:00            dongs | nonstandar footprint
09:07:04            dongs | and its been out of production for years
09:07:11            dongs | any stock tehy have is likely oxidized to fuck
09:07:36            dongs | swpa is there so looks good
```

## inductors, how do they work...
```
15:52 <PeterM> rajkostoso like how do you find specs on those chink inductors?
15:52 <rajkosto> PeterM, i dont
15:52 <Steffanx> what will it be then specing?
15:53 <rajkosto> just type in 47uh inductor and get 12x12x7 one
15:53 <PeterM> so what good is a 47uh inducctor that could saturate at 1ma?
15:53 <PeterM> because you dont know the spec
15:53 <rajkosto> they are good enough at that size
15:53 <specing> Steffanx: Ada
15:53 <rajkosto> the chinks use them themselves
15:53 <PeterM> good enough for what?
15:53 <rajkosto> dc2dc
15:54 <PeterM> ...
15:54 <rajkosto> current rating comes from the wire thickness
15:54 <rajkosto> and at that size they have thick wire
15:54 <PeterM> bro
15:54 <PeterM> dude
15:54 <PeterM> man
15:54 <PeterM> mate
15:54 <PeterM> cunt
15:54 <rajkosto> oi
15:54 <PeterM> thats not how inductors work
5:57 <BrainDamage> currrent rating is wire thickness only if the core is not lossy
15:57 <BrainDamage> spoiler: at high freq cores are pretty lossy
```

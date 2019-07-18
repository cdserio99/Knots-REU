#!/usr/bin/env/python
# This script was saved by SnapPy on Thu Jul 18 11:05:47 2019.

X = Manifold('DT:[(-110,42,60,94,-32,114,-78,-4,40,38,2,76,-12,-66,84,102,48,-92,-58,18,-54,-88,24,-122,72,106,16,-20,128,-52,96,-30,116,-80,-62,-8,34,-112,44,98,28,-118,68,14,-22,126,-50,-104,-86,26,-120,70,-6,36),(56,90,-46,-100,-82,64,10,130,-74,-108),(124,)]')

X.dehn_fill((0,1),1)

Z = X.filled_triangulation()

Kverify = Z.copy()

Kverify.dehn_fill((0,1),1)

Kfill = Kverify.filled_triangulation()

Kfill.identify()
#[10_44(0,0), K10a32(0,0)]

Kfill.volume()
#12.968994205

Z.volume()
#20.866198487

Z.cusp_translations()
#[(-1.231863755 + 1.032895382*I, 3.931960893), (0.128267761 + 1.602469520*I, 2.534403431)]

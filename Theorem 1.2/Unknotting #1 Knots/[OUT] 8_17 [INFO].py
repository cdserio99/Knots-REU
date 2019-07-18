#!/usr/bin/env/python
# This script was saved by SnapPy on Thu Jul 18 10:53:47 2019.

X = Manifold('DT:[(-14,54,-84,64,-94,74),(36,-4,58,78,-88,-68,44,42,40,-66,86,-76,-56,16,28,26,-82,-62,72,92,-38,2,-52,80,22,-32,6,46,-60,-20,-34,12,-50,-90,24,30,-8,48,70,-18),(-10,)]')

X.dehn_fill((0,1),0)

Z = X.filled_triangulation()

Kverify = Z.copy()

Kverify.dehn_fill((0,1),1)

Kfill = Kverify.filled_triangulation()

Kfill.identify()
#[8_17(0,0), K8a14(0,0)]

Kfill.volume()
#10.9859076063

Z.volume()
#17.8840422747

Z.cusp_translations()
#[(1.1352148040 + 1.0266162320*I, 4.0811843233), (-0.0190991086 + 1.5304537769*I, 2.7376260136)]

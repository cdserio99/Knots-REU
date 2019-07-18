#!/usr/bin/env/python
# This script was saved by SnapPy on Thu Jul 18 10:51:27 2019.

X = Manifold('DT:[(40,-28,18,-44,2,-20,-24,6,-32,26,-38,-14,-12,-48,34,-16,46,-8,-22),(10,50,36,30,-4),(42,)]')

X.dehn_fill((0,1),1)

Z = X.filled_triangulation()

Kverify = Z.copy()

Kverify.dehn_fill((0,1),1)

Kfill = Kverify.filled_triangulation()

Kfill.identify()
#[t11291(0,0), 7_6(0,0), K8_241(0,0), K7a2(0,0)]

Kfill.volume()
#7.0849259535

Z.volume()
#13.7023056990

Z.cusp_translations()
#[(-1.070809920 + 1.030378591*I, 4.112278473), (0.004615096 + 1.486032512*I, 2.851353294)]

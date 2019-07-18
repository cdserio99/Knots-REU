#!/usr/bin/env/python
# This script was saved by SnapPy on Thu Jul 18 10:50:45 2019.

X = Manifold('DT:[(-26,-18,32,-14,22,-36,2,24,-6,12,-30,16,8,-20,34),(4,-10,28,-40),(-38,)]')

X.dehn_fill((0,1),1)

Z = X.filled_triangulation()

Kverify = Z.copy()

Kverify.dehn_fill((0,1),1)

Kfill = Kverify.filled_triangulation()

Kfill.identify()
#[m289(0,0), 6_2(0,0), K5_19(0,0), K6a2(0,0)]

Kfill.volume()
#4.4008325161

Z.volume()
#10.9907910203

Z.cusp_translations()
#[(-1.0602507356 + 0.9989923483*I, 4.1346681656), (-0.0491886512 + 1.4559182020*I, 2.8370425306)]

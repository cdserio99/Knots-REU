#!/usr/bin/env/python
# This script was saved by SnapPy on Thu Jul 18 10:59:51 2019.

X = Manifold('DT:[(26,-10,-12,-24,14,-20,18,-28,8,-4,32,-6),(22,-16,2,-34),(-30,)]')

X.dehn_fill((0,1),1)

Z = X.filled_triangulation()

Kverify = Z.copy()

Kverify.dehn_fill((0,1),1)

Kfill = Kverify.filled_triangulation()

Kfill.identify()
#[m199(0,0), 9_42(0,0), K5_8(0,0), K9n4(0,0)]

Kfill.volume()
#4.0568602242

Z.volume()
#10.000401669

Z.cusp_translations()
#[(-1.0783408238 + 1.0425115222*I, 3.8504352683), (0.1292554534 + 1.4943032603*I, 2.6862841293)]

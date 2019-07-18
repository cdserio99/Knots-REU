#!/usr/bin/env/python
# This script was saved by SnapPy on Thu Jul 18 10:51:06 2019.

X = Manifold('DT:[(16,-26,-18,30,-34,6,32,-36,24,-28,40,-12,-4,-2,10,-22),(-8,20,-14,42),(38,)]')

X.dehn_fill((0,1),1)

Z = X.filled_triangulation()

Kverify = Z.copy()

Kverify.dehn_fill((0,1),1)

Kfill = Kverify.filled_triangulation()

Kfill.identify()
#[s912(0,0), 6_3(0,0), K6_43(0,0), K6a1(0,0)]

Kfill.volume()
#5.6930210913

Z.volume()
#11.5227417526

Z.cusp_translations()
#[(-0.957218273 + 1.060768236*I, 4.013527454), (0.080808253 + 1.426522379*I, 2.984476444)]

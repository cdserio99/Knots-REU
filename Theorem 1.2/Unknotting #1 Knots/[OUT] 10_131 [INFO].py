#!/usr/bin/env/python
# This script was saved by SnapPy on Thu Jul 18 11:17:48 2019.

X = Manifold('DT:[(12,10,-40,22,-32,2,52,50,30,-36,26,-54,6,-44,18,-48,56,-4,46,-20,60,-8,38,-28,16,14),(-24,42,34,-62),(-58,)]')

X.dehn_fill((0,1),1)

Z = X.filled_triangulation()

Kverify = Z.copy()

Kverify.dehn_fill((0,1),1)

Kfill = Kverify.filled_triangulation()

Kfill.identify()
#[10_131(0,0), K10n19(0,0)]

Kfill.volume()
#9.4650216573

Z.volume()
#15.194328389

Z.cusp_translations()
#[(-1.080737750 + 1.000900403*I, 4.381270976), (-0.132285299 + 1.467070653*I, 2.989096590)]

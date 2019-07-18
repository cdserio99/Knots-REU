#!/usr/bin/env/python
# This script was saved by SnapPy on Thu Jul 18 10:53:01 2019.

X = Manifold('DT:[(20,-66,54,-32,58,36,24,-62,28),(-12,-48,18,38,14,-50,-8,44,-4,-64,26,52,30,-56,34,-22,60,-10,-46,6,-42,-16,-40),(-2,)]')

X.dehn_fill((0,1),0)

Z = X.filled_triangulation()

Kverify = Z.copy()

Kverify.dehn_fill((0,1),1)

Kfill = Kverify.filled_triangulation()

Kfill.identify()
#[o9_43592(0,0), 8_13(0,0), K8a7(0,0)]

Kfill.volume()
#8.5312322015

Z.volume()
#15.9901574924

Z.cusp_translations()
#[(1.218279081 + 0.985692807*I, 4.169104616), (0.063838266 + 1.565796572*I, 2.624514899)]

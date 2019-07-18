#!/usr/bin/env/python
# This script was saved by SnapPy on Thu Jul 18 11:21:00 2019.

X = Manifold('DT:[(-14,70,-42,52,-28,-26,-60,36,-72,-44,54,-64,48,-10,-8,58,-68,40,-76,16,-2,32,80,22,-88,12,-30,-82,20,-6,90,-24,84,18,4,-34,78),(74,-38,-66,-56,-46,92,62,-50),(86,)]')

X.dehn_fill((0,1),1)

Z = X.filled_triangulation()

Kverify = Z.copy()

Kverify.dehn_fill((0,1),1)

Kfill = Kverify.filled_triangulation()

Kfill.identify()
#[10_156(0,0), K10n32(0,0)]

Kfill.volume()
#11.1633906422

Z.volume()
#17.8811659923

Z.cusp_translations()
#[(1.103528178 + 1.050660726*I, 3.975337868), (-0.093370687 + 1.520836716*I, 2.746337807)]

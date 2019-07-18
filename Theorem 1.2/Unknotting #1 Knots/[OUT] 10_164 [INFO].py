#!/usr/bin/env/python
# This script was saved by SnapPy on Thu Jul 18 11:21:49 2019.

X = Manifold('DT:[(28,-68,32,72,52,98,38,114,-78,-92,-60,-120,-50),(-8,-100,4,-74,-54,94,20,80,76,36,96,-10,-26,64,116,-88,110,-12,-46,-118,-6,102,-2,66,-56,-16,90,-58,108,106,104,42,-112,-14,-62,48,24,70,-30,86,84,82,-40,18,-44,34),(-22,)]')

X.dehn_fill((0,1),0)

Z = X.filled_triangulation()

Kverify = Z.copy()

Kverify.dehn_fill((0,1),1)

Kfill = Kverify.filled_triangulation()

Kfill.identify()
#[10_165(0,0), K10n38(0,0)]

Kfill.volume()
#12.506687931

Z.volume()
#19.145974711

Z.cusp_translations()
#[(1.119221443 + 1.035853503*I, 4.141917962), (-0.005450803 + 1.501539521*I, 2.770117119)]

#!/usr/bin/env/python
# This script was saved by SnapPy on Thu Jul 18 11:00:35 2019.

X = Manifold('DT:[(36,-20,46,-34,4,52,-40,54,38,26,-48,32,-10,50,-44,-42,-6,22,-28,-12,-16,-30),(-24,8,-2,-18,14,-58),(-56,)]')

X.dehn_fill((0,1),1)

Z = X.filled_triangulation()

Kverify = Z.copy()

Kverify.dehn_fill((0,1),1)

Kfill = Kverify.filled_triangulation()

Kfill.identify()
#[o9_43771(0,0), 9_45(0,0), K9n2(0,0)]

Kfill.volume()
#8.6020311664

Z.volume()
#14.2533007300

Z.cusp_translations()
#[(1.046304217 + 1.004830397*I, 4.339226905), (0.109902015 + 1.446498596*I, 3.014304406)]

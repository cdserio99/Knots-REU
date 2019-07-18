#!/usr/bin/env/python
# This script was saved by SnapPy on Thu Jul 18 11:21:24 2019.

X = Manifold('DT:[(-42,28,-62,18,54,-70,46,-2,64,-36,48,-74,-6,52,-40,72,-56,66,24,-50,14,-60,-58,-30,22,4,-16,-34,10,-44),(38,-26,-8,32,76,-12,-20),(68,)]')

X.dehn_fill((0,1),1)

Z = X.filled_triangulation()

Kverify = Z.copy()

Kverify.dehn_fill((0,1),1)

Kfill = Kverify.filled_triangulation()

Kfill.identify()
#[10_159(0,0), K10n34(0,0)]

Kfill.volume()
#11.7406410379

Z.volume()
#18.1754868743

Z.cusp_translations()
#[(-1.1282527673 + 0.9884171716*I, 4.2512714164), (-0.1056351853 + 1.4962499857*I, 2.8083740749)]

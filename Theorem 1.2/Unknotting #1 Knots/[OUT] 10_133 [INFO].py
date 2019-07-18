#!/usr/bin/env/python
# This script was saved by SnapPy on Thu Jul 18 11:18:35 2019.

X = Manifold('DT:[(20,-26,16,-32,-30,-28,2,-34,6,-36,12,-4,38,-22,-10,-8),(-42,-18,-14,24),(40,)]')

X.dehn_fill((0,1),1)

Z = X.filled_triangulation()

Kverify = Z.copy()

Kverify.dehn_fill((0,1),1)

Kfill = Kverify.filled_triangulation()

Kfill.identify()
#[]

Kfill.volume()
#-5.0 E-7

Z.volume()
#-2.7 E-7

Z.cusp_translations()

#!/usr/bin/env/python
# This script was saved by SnapPy on Thu Jul 18 10:52:55 2019.

X = Manifold('DT:[(-12,14,22,-56,30),(-28,-44,10,-52,26,-38,6,-60,18,-42,-48,-46,58,-24,50,-16,-36,-34,-32,-8,62,-20,40,-4,54),(-2,)]')

X.dehn_fill((0,1),0)

Z = X.filled_triangulation()

Kverify = Z.copy()

Kverify.dehn_fill((0,1),1)

Kfill = Kverify.filled_triangulation()

Kfill.identify()

Kfill.volume()

Z.volume()

Z.cusp_translations()

#!/usr/bin/env/python
# This script was saved by SnapPy on Thu Jul 18 11:03:15 2019.

X = Manifold('DT:[(14,-16,60,-32,78,46),(-10,108,-94,-36,-122,88,56,72,-6,102,-28,-64,84,-126,-116,12,-106,-92,-82,124,22,70,8,-100,20,54,86,-120,-34,-62,-114,4,-104,-90,40,-52,24,68,128,42,74,-112,-110,30,-58,130,-44,-76,-98,-96,18,48,80,-26,-66,-38,50,-118),(2,)]')

X.dehn_fill((0,1),0)

Z = X.filled_triangulation()

Kverify = Z.copy()

Kverify.dehn_fill((0,1),1)

Kfill = Kverify.filled_triangulation()

Kfill.identify()

Kfill.volume()

Z.volume()

Z.cusp_translations()

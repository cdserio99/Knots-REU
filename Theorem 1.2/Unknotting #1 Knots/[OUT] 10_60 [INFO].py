#!/usr/bin/env/python
# This script was saved by SnapPy on Thu Jul 18 11:07:05 2019.

X = Manifold('DT:[(94,18,-110,130,40,-64,82,6,-122,30,-98,140,-54,22,-106,-2,132,60,-146,-116,66,-14,142,-78,-76,-74,100,-24,-46,-90,38,114,-84,-8,-34,-126,-52,-50,-48,58,-112,150,-10,-62,144,70,-124,-20,104,-138,56,-28,96,-4,120,44,-148,86,68,-16,108,32,134,-72),(-42,-118,-92,128,-152,26,-102,-80,-36,88,12),(-136,)]')

X.dehn_fill((0,1),1)

Z = X.filled_triangulation()

Kverify = Z.copy()

Kverify.dehn_fill((0,1),1)

Kfill = Kverify.filled_triangulation()

Kfill.identify()
#[]

Kfill.volume()
#13.980041536

Z.volume()
#21.3939709

Z.cusp_translations()

#!/usr/bin/env/python
# This script was saved by SnapPy on Thu Jul 18 11:07:11 2019.

X = Manifold('DT:[(-26,92,48,-136,-80,-54,78,66,132,88,44,-70),(116,-18,-94,40,104,10,-12,-64,-84,-128,22,-120,-14,38,106,36,-8,122,34,-108,76,-4,114,-20,-96,-30,-50,-56,-60,-110,74,-130,24,-118,-16,86,42,126,124,-82,-62,52,32,98,-46,-90,134,68,58,102,100,-112,72,28,-2),(-6,)]')

X.dehn_fill((0,1),0)

Z = X.filled_triangulation()

Kverify = Z.copy()

Kverify.dehn_fill((0,1),1)

Kfill = Kverify.filled_triangulation()

Kfill.identify()
#[10_71(0,0), K10a10(0,0)]

Kfill.volume()
#13.3852287460

Z.volume()
#20.980063259

Z.cusp_translations()
#[(-1.20741293 + 1.02888753*I, 3.98273121), (0.08662799 + 1.58396689*I, 2.58703796)]

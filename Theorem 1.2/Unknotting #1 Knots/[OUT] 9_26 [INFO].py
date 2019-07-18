#!/usr/bin/env/python
# This script was saved by SnapPy on Thu Jul 18 10:56:49 2019.

X = Manifold('DT:[(-16,-14,-40,70,-50,-28,58,-2,-78,56,-62,32,-6,-80,-52,-72,22,44,-12,84,-20,-60,30,-8,88,66,-36,-76,4,54,74,-24,-46,10,-86,64,-34,42,-18),(-68,90,38,-26,48),(82,)]')

X.dehn_fill((0,1),1)

Z = X.filled_triangulation()

Kverify = Z.copy()

Kverify.dehn_fill((0,1),1)

Kfill = Kverify.filled_triangulation()

Kfill.identify()
#[9_26(0,0), K9a15(0,0)]

Kfill.volume()
#10.5958405150

Z.volume()
#41.6058979927

Z.cusp_translations()
#[(-0.433525346 + 1.247009578*I, 12.255684829), (1.938140883 + 5.136162692*I, 2.162095759)]

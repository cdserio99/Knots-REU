#!/usr/bin/env/python
# This script was saved by SnapPy on Thu Jul 18 11:16:25 2019.

X = Manifold('DT:[(32,-102,-126,88,-46,-116,-36,106,92,50,-84,-42,-122,-98,-112),(4,-60,28,78,-118,-18,68,-8,54,22,-72,-86,44,-124,100,114,-34,-104,-90,-48,82,40,120,-96,-110,52,-20,70,10,-56,24,-74,-108,14,64,-2,58,26,-76,38,12,62,-30,80,94,-16,66),(-6,)]')

X.dehn_fill((0,1),0)

Z = X.filled_triangulation()

Kverify = Z.copy()

Kverify.dehn_fill((0,1),1)

Kfill = Kverify.filled_triangulation()

Kfill.identify()
#[10_114(0,0), K10a77(0,0)]

Kfill.volume()
#15.304904343

Z.volume()
#22.8340278886

Z.cusp_translations()
#[(-1.236636271 + 0.975107974*I, 4.184112378), (-0.082494971 + 1.572672695*I, 2.594285103)]

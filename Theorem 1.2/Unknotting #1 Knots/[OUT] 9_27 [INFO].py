#!/usr/bin/env/python
# This script was saved by SnapPy on Thu Jul 18 10:57:28 2019.

X = Manifold('DT:[(14,-66,54,28,-80,42,2,90,88,68,-36,-62,10,-92,-50,58,-46,84,-20,4,-96,24,72,-32,76,6,-102,30,-74,34,82,-12,98,-86,22,-60,48,-56,-8,94,-44,-70,38,18,16),(-52,78,-26,64,104,-40),(100,)]')

X.dehn_fill((0,1),1)

Z = X.filled_triangulation()

Kverify = Z.copy()

Kverify.dehn_fill((0,1),1)

Kfill = Kverify.filled_triangulation()

Kfill.identify()
#[9_27(0,0), K9a12(0,0)]

Kfill.volume()
#10.9999809583

Z.volume()
#18.1892856391

Z.cusp_translations()
#[(1.1565589859 + 1.0543303948*I, 3.9387743920), (-0.1288451807 + 1.5596923378*I, 2.6625568767)]

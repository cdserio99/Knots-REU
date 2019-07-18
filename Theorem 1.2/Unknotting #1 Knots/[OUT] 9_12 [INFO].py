#!/usr/bin/env/python
# This script was saved by SnapPy on Thu Jul 18 10:54:54 2019.

X = Manifold('DT:[(48,28,-20,32,-16,54,-66,40,-8,44,-4,58,-72,-46,6,-42,10,-56,68,-34,18,-30,22,2,64,62,60,-38,14,26,52,50),(-24,36,-12,-74),(-70,)]')

X.dehn_fill((0,1),1)

Z = X.filled_triangulation()

Kverify = Z.copy()

Kverify.dehn_fill((0,1),1)

Kfill = Kverify.filled_triangulation()

Kfill.identify()
#[9_12(0,0), K9a22(0,0)]

Kfill.volume()
#8.8366423439

Z.volume()
#15.3314046809

Z.cusp_translations()
#[(-1.079330899 + 1.057665191*I, 4.098994827), (0.049835268 + 1.510340125*I, 2.870455519)]

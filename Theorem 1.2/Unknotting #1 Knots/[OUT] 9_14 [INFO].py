#!/usr/bin/env/python
# This script was saved by SnapPy on Thu Jul 18 10:55:17 2019.

X = Manifold('DT:[(48,24,22,20,18,-42,32,-54,10,8,6,4,-46,40,-50,36,-64,14,-58,28,-62,68,-16,2,-26,60,-30,70,-12,52,-38),(-34,56,72,44),(66,)]')

X.dehn_fill((0,1),1)

Z = X.filled_triangulation()

Kverify = Z.copy()

Kverify.dehn_fill((0,1),1)

Kfill = Kverify.filled_triangulation()

Kfill.identify()
#[9_14(0,0), K9a17(0,0)]

Kfill.volume()
#8.9549892620

Z.volume()
#15.381819861

Z.cusp_translations()
#[(1.068552478 + 1.065506391*I, 4.078072890), (-0.068199277 + 1.507467123*I, 2.882459367)]

#!/usr/bin/env/python
# This script was saved by SnapPy on Thu Jul 18 11:19:50 2019.

X = Manifold('DT:[(28,14,-34,-42,-20,46,-50,6,-54,40,-2,-60,48,-62,10,-44,52,-4,56,-30,-8,18,-38,24),(22,36,-16,32,-12,-64,-26),(-58,)]')

X.dehn_fill((0,1),1)

Z = X.filled_triangulation()

Kverify = Z.copy()

Kverify.dehn_fill((0,1),1)

Kfill = Kverify.filled_triangulation()

Kfill.identify()
#[10_143(0,0), K10n26(0,0)]

Kfill.volume()
#9.0708992700

Z.volume()
#15.0179235799

Z.cusp_translations()
#[(-1.1081746796 + 0.9788548873*I, 4.2952099358), (-0.1356740205 + 1.4723452622*I, 2.8555715467)]

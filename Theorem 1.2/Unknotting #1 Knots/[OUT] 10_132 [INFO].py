#!/usr/bin/env/python
# This script was saved by SnapPy on Thu Jul 18 11:18:13 2019.

X = Manifold('DT:[(-28,40,36,-22,-30,44,-38,24,32,-46,14,-6,34,20,-12,-4,26,-16,8),(-18,-48,10,2),(-42,)]')

X.dehn_fill((0,1),1)

Z = X.filled_triangulation()

Kverify = Z.copy()

Kverify.dehn_fill((0,1),1)

Kfill = Kverify.filled_triangulation()

Kfill.identify()
#[m201(0,0), 10_132(0,0), K5_9(0,0), K10n13(0,0)]

Kfill.volume()
#4.0568602242

Z.volume()
#9.5613009739

Z.cusp_translations()
#[(-1.210475037 + 0.926185355*I, 4.379134584), (-0.242883651 + 1.504684904*I, 2.695508081)]

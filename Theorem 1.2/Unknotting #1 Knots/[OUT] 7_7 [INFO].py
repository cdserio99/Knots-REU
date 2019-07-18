#!/usr/bin/env/python
# This script was saved by SnapPy on Thu Jul 18 10:51:49 2019.

X = Manifold('DT:[(-36,18,-44,24,34,-16,46,-28,42,-8,32,30,4,-12,38,22,20,-2,10,-48,26),(-6,-40,14,-52),(-50,)]')

X.dehn_fill((0,1),1)

Z = X.filled_triangulation()

Kverify = Z.copy()

Kverify.dehn_fill((0,1),1)

Kfill = Kverify.filled_triangulation()

Kfill.identify()
#[t12656(0,0), 7_7(0,0), K8_294(0,0), K7a1(0,0)]

Kfill.volume()
#7.64337517236

Z.volume()
#13.9272889591

Z.cusp_translations()
#[(1.023125217 + 1.060889359*I, 4.036595909), (-0.073766028 + 1.472015630*I, 2.909195771)]

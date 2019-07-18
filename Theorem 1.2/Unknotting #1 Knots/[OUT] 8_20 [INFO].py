#!/usr/bin/env/python
# This script was saved by SnapPy on Thu Jul 18 10:54:10 2019.

X = Manifold('DT:[(24,-6,-18,12,-22,16,-26,8,-4,30,-10),(20,-14,2,32),(28,)]')

X.dehn_fill((0,1),1)

Z = X.filled_triangulation()

Kverify = Z.copy()

Kverify.dehn_fill((0,1),1)

Kfill = Kverify.filled_triangulation()

Kfill.identify()
#[m222(0,0), 8_20(0,0), K5_12(0,0), K8n1(0,0)]

Kfill.volume()
#4.12490325181

Z.volume()
#10.4749350302

Z.cusp_translations()
#[(1.0962087188 + 0.9941497249*I, 4.0672327425), (0.0287328591 + 1.4795883392*I, 2.7328130432)]

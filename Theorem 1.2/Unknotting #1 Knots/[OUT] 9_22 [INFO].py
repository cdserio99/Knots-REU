#!/usr/bin/env/python
# This script was saved by SnapPy on Thu Jul 18 10:56:04 2019.

X = Manifold('DT:[(72,-56,14,42,-84,52,64,-30,-74,58,-4,40,82,-50,62,20,-76,46,-86,54,-12,-28,-60,-70,36,8,-24,-66,32,16,-44,-6,-22,80,-48),(68,-34,-18,2,-88,-38,-10,26),(-78,)]')

X.dehn_fill((0,1),1)

Z = X.filled_triangulation()

Kverify = Z.copy()

Kverify.dehn_fill((0,1),1)

Kfill = Kverify.filled_triangulation()

Kfill.identify()
#[9_22(0,0), K9a2(0,0)]

Kfill.volume()
#10.6207270212

Z.volume()
#18.1853958821

Z.cusp_translations()
#[(-1.192435474 + 1.038955240*I, 3.917401318), (0.128358412 + 1.576342117*I, 2.581929763)]

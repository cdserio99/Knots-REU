#!/usr/bin/env/python
# This script was saved by SnapPy on Thu Jul 18 10:57:50 2019.

X = Manifold('DT:[(22,44,76,-70,98,-2,-42,58,-108,-88,-32,64,-104,54,86,12,-40,60,-112,96,20,-30,78,-68,100,-46,-6,74,72,18,-94,38,-10,-50,82,26,56,-28,-84,66,-102,52,-4,14,34,-62,110,-90),(-24,-80,48,8,-114,-16,-36,92),(-106,)]')

X.dehn_fill((0,1),1)

Z = X.filled_triangulation()

Kverify = Z.copy()

Kverify.dehn_fill((0,1),1)

Kfill = Kverify.filled_triangulation()

Kfill.identify()
#[9_28(0,0), K9a5(0,0)]

Kfill.volume()
#11.5631770163

Z.volume()
#19.046259073

Z.cusp_translations()
#[(1.185291778 + 1.029573221*I, 3.990800618), (-0.076183445 + 1.568162523*I, 2.620150263)]

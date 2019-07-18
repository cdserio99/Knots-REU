#!/usr/bin/env/python
# This script was saved by SnapPy on Thu Jul 18 10:55:40 2019.

X = Manifold('DT:[(-14,22,86,-42,50,32),(-10,66,-34,-52,8,-64,56,-80,16,12,-68,46,-54,78,-6,72,-82,-28,2,-70,44,26,-38,-76,-74,40,-48,-30,84,-20,-62,-60,-58,-24,36,18),(4,)]')

X.dehn_fill((0,1),0)

Z = X.filled_triangulation()

Kverify = Z.copy()

Kverify.dehn_fill((0,1),1)

Kfill = Kverify.filled_triangulation()

Kfill.identify()
#[9_21(0,0), K9a21(0,0)]

Kfill.volume()
#10.183265536

Z.volume()
#17.4006534622

Z.cusp_translations()
#[(-1.2346021827 + 0.9818128811*I, 4.2514503287), (-0.1027408301 + 1.5740531773*I, 2.6518346117)]

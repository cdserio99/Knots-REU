#!/usr/bin/env/python
# This script was saved by SnapPy on Thu Jul 18 11:00:11 2019.

X = Manifold('DT:[(-10,20,-28,-26,-14,32,-2,24,-38,4,-34,30,-8,-6,16),(-22,12,40,-18),(36,)]')

X.dehn_fill((0,1),1)

Z = X.filled_triangulation()

Kverify = Z.copy()

Kverify.dehn_fill((0,1),1)

Kfill = Kverify.filled_triangulation()

Kfill.identify()
#[t12271(0,0), 9_44(0,0), K8_280(0,0), K9n1(0,0)]

Kfill.volume()
#7.4067675724

Z.volume()
#12.3912653958

Z.cusp_translations()
#[(0.9049919252 + 1.0587899157*I, 4.2158699664), (-0.0202069826 + 1.3927089244*I, 3.2050635478)]

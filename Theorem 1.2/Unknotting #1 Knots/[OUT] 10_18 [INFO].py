#!/usr/bin/env/python
# This script was saved by SnapPy on Thu Jul 18 11:02:29 2019.

X = Manifold('DT:[(-18,50,38,-26,-22,-34,46,60,-2,68,-14,-76,54,62,-4,72,-12,-78,56,-64,6,74,10,80,58,-66,8,-42,-30),(-20,-52,-40,28,16,-48,82,-36,-24,44,-32),(70,)]')

X.dehn_fill((0,1),1)

Z = X.filled_triangulation()

Kverify = Z.copy()

Kverify.dehn_fill((0,1),1)

Kfill = Kverify.filled_triangulation()

Kfill.identify()
#[10_18(0,0), K10a63(0,0)]

Kfill.volume()
#10.639844271

Z.volume()
#18.3670737022

Z.cusp_translations()
#[(1.2433214529 + 1.0423682216*I, 3.9424117279), (-0.1427901717 + 1.6161654345*I, 2.5427129018)]

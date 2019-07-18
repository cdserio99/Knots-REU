#!/usr/bin/env/python
# This script was saved by SnapPy on Thu Jul 18 10:59:26 2019.

X = Manifold('DT:[(-84,42,14,72,-26,-98,40,-58,-106,82,-2,-12,-70,54,100,-112,86,66,8,-96,-50,-60,108,-80,-4,22,-68,-36,94,48,20,-110,88,-28,10,38,-56,92,90,16,-44,62,30,-102,78,76,74,-6,24,52,-34,114),(118,46,-18,104,-32,-64),(116,)]')

X.dehn_fill((0,1),1)

Z = X.filled_triangulation()

Kverify = Z.copy()

Kverify.dehn_fill((0,1),1)

Kfill = Kverify.filled_triangulation()

Kfill.identify()
#[9_39(0,0), K9a32(0,0)]

Kfill.volume()
#12.8103100033

Z.volume()
#19.7053462827

Z.cusp_translations()
#[(1.170872188 + 1.014896620*I, 4.207861888), (0.044476221 + 1.520051278*I, 2.706006426)]

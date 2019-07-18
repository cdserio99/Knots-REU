#!/usr/bin/env/python
# This script was saved by SnapPy on Thu Jul 18 11:01:22 2019.

X = Manifold('DT:[(-22,-14,42,18,-26,-34,48,-44,56,10,50,-46,-58,-8,-52,2,-60,-6,-54,4,-64,38,30),(-40,-32,24,16,-36,-28,20,12,-66),(-62,)]')

X.dehn_fill((0,1),1)

Z = X.filled_triangulation()

Kverify = Z.copy()

Kverify.dehn_fill((0,1),1)

Kfill = Kverify.filled_triangulation()

Kfill.identify()
#[o9_42320(0,0), 10_9(0,0), K10a110(0,0)]

Kfill.volume()
#8.2940996752

Z.volume()
#15.554195018

Z.cusp_translations()
#[(1.2283230460 + 1.0795621006*I, 3.8589519080), (-0.2363230186 + 1.6181419175*I, 2.5745444097)]

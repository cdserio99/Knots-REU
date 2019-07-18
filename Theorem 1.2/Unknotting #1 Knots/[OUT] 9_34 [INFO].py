#!/usr/bin/env/python
# This script was saved by SnapPy on Thu Jul 18 10:59:02 2019.

X = Manifold('DT:[(-18,-128,-104,114,52,-94,-32,42),(80,-16,88,46,-100,-58,-40,76,-6,98,56,118,-78,4,-124,26,-36,-72,10,-110,120,-22,86,84,82,-44,34,96,-54,-116,106,20,66,64,62,-126,28,-38,74,-8,-112,122,-24,68,-14,30,92,50,-70,12,-108,-90,-48,102,60),(-2,)]')

X.dehn_fill((0,1),0)

Z = X.filled_triangulation()

Kverify = Z.copy()

Kverify.dehn_fill((0,1),1)

Kfill = Kverify.filled_triangulation()

Kfill.identify()
#[9_34(0,0), K9a28(0,0)]

Kfill.volume()
#14.3445813878

Z.volume()
#21.475351231

Z.cusp_translations()
#[(-1.152289744 + 1.031053477*I, 4.015682930), (0.0576416746 + 1.5451603039*I, 2.6795820705)]

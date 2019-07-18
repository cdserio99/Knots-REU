#!/usr/bin/env/python
# This script was saved by SnapPy on Thu Jul 18 10:56:26 2019.

X = Manifold('DT:[(20,-24,-34,80,42,-68,-30,76,-86),(2,-62,18,48,36,-6,58,-14,50,-82,-44,10,-54,70,-84,-74,28,66,-40,-78,32,-22,46,38,-8,56,-64,-26,4,-60,12,-52,72),(-16,)]')

X.dehn_fill((0,1),0)

Z = X.filled_triangulation()

Kverify = Z.copy()

Kverify.dehn_fill((0,1),1)

Kfill = Kverify.filled_triangulation()

Kfill.identify()
#[9_24(0,0), K9a7(0,0)]

Kfill.volume()
#10.833729109

Z.volume()
#18.267396916

Z.cusp_translations()
#[(-1.199483375 + 1.029308414*I, 3.981122363), (0.085189151 + 1.578283557*I, 2.596366620)]

#!/usr/bin/env/python
# This script was saved by SnapPy on Thu Jul 18 11:02:07 2019.

X = Manifold('DT:[(16,30,-46,-56,-68,38,26,-62,72,-40,8,-54,-74,14,-86,-42,6,24,-76,70,58,-4,84,32,20,-10,66,80,-48,-2,88,-12,-36,78,-50,18),(-28,64,52,-22,-34,90,44,60),(82,)]')

X.dehn_fill((0,1),1)

Z = X.filled_triangulation()

Kverify = Z.copy()

Kverify.dehn_fill((0,1),1)

Kfill = Kverify.filled_triangulation()

Kfill.identify()
#[10_17(0,0), K10a107(0,0)]

Kfill.volume()
#8.5367555992

Z.volume()
#15.7033140854

Z.cusp_translations()
#[(1.2520686596 + 1.0400255377*I, 4.0338283306), (-0.0960615737 + 1.6248388294*I, 2.5819696100)]

#!/usr/bin/env/python
# This script was saved by SnapPy on Thu Jul 18 11:20:15 2019.

X = Manifold('DT:[(-62,-40,66,-36,-70,-48,76,-42,-64,38,-68,-50,54,72,-46,-24,52,16,-4,20,8,-26,-58,-12,60,34,32,-44,74,30),(80,22,6,-18,2,14,56,28,10),(78,)]')

X.dehn_fill((0,1),1)

Z = X.filled_triangulation()

Kverify = Z.copy()

Kverify.dehn_fill((0,1),1)

Kfill = Kverify.filled_triangulation()

Kfill.identify()
#[10_146(0,0), K10n23(0,0)]

Kfill.volume()
#10.561016755

Z.volume()
#16.8065290230

Z.cusp_translations()
#[(1.0141388659 + 1.0754289302*I, 3.8604699074), (-0.161035905 + 1.469385062*I, 2.825441152)]

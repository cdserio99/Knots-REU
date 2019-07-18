#!/usr/bin/env/python
# This script was saved by SnapPy on Thu Jul 18 11:04:12 2019.

X = Manifold('DT:[(-18,118,-80,30,-54,132,66,42),(102,-14,128,-114,-76,34,-96,10,-58,-122,-84,70,-104,16,130,-116,-78,-28,94,-8,52,-124,-86,72,-106,2,-46,-22,-112,60,36,98,-4,48,24,74,-110,-108,-32,56,-120,82,-68,-44,20,-92,-90,126,62,38,-100,6,50,26,-88,-64,-40),(12,)]')

X.dehn_fill((0,1),0)

Z = X.filled_triangulation()

Kverify = Z.copy()

Kverify.dehn_fill((0,1),1)

Kfill = Kverify.filled_triangulation()

Kfill.identify()
#[10_31(0,0), K10a69(0,0)]

Kfill.volume()
#11.044264031

Z.volume()
#18.5238040240

Z.cusp_translations()
#[(-1.216369887 + 1.049023780*I, 3.923884898), (0.150397200 + 1.599183315*I, 2.573969181)]

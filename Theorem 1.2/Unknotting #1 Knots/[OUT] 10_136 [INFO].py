#!/usr/bin/env/python
# This script was saved by SnapPy on Thu Jul 18 11:18:40 2019.

X = Manifold('DT:[(-10,28,42,-34),(-4,20,-38,-22,40,-26,32,36,-30,2,-18,12,-8,16,-14,24),(6,)]')

X.dehn_fill((0,1),0)

Z = X.filled_triangulation()

Kverify = Z.copy()

Kverify.dehn_fill((0,1),1)

Kfill = Kverify.filled_triangulation()

Kfill.identify()
#[o9_37080(0,0), 10_136(0,0), K10n3(0,0)]

Kfill.volume()
#7.7462745462

Z.volume()
#13.6241034147

Z.cusp_translations()
#[(1.006570028 + 1.082807243*I, 3.947366942), (-0.137072217 + 1.472027838*I, 2.903639053)]

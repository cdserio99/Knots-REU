#!/usr/bin/env/python
# This script was saved by SnapPy on Thu Jul 18 11:04:35 2019.

X = Manifold('DT:[(-76,-18,86,-102,-56,96,-112,28,74,44,10,-94,114,-62,-80,108,-20,90,120,-88,122,-58,98,-110,-16,84,-104,68,34,4,50,-82,106,-22,-92,116,-60,-2,-100,48,14,-26,-72,-38,-42,8,54,-66,-32,-78),(-36,70,24,-12,-46,30,64,-52,-6,124,40),(118,)]')

X.dehn_fill((0,1),1)

Z = X.filled_triangulation()

Kverify = Z.copy()

Kverify.dehn_fill((0,1),1)

Kfill = Kverify.filled_triangulation()

Kfill.identify()
#[10_32(0,0), K10a55(0,0)]

Kfill.volume()
#12.090936872

Z.volume()
#19.874792747

Z.cusp_translations()
#[(1.289671439 + 0.957139213*I, 4.264755098), (0.133854686 + 1.600453316*I, 2.550505095)]

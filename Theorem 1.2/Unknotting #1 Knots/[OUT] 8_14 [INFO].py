#!/usr/bin/env/python
# This script was saved by SnapPy on Thu Jul 18 10:53:23 2019.

X = Manifold('DT:[(-14,44,-52,68,76,60),(-4,28,-72,64,36,34,50,-58,-42,74,-66,22,20,54,-46,2,-30,16,62,-8,32,-18,-48,12,-26,-70,-38,6,-24,56,40),(10,)]')

X.dehn_fill((0,1),0)

Z = X.filled_triangulation()

Kverify = Z.copy()

Kverify.dehn_fill((0,1),1)

Kfill = Kverify.filled_triangulation()

Kfill.identify()
#[8_14(0,0), K8a1(0,0)]

Kfill.volume()
#9.2178003160

Z.volume()
#16.240487397

Z.cusp_translations()
#[(1.197304130 + 0.973249639*I, 4.245000833), (0.119543057 + 1.538330750*I, 2.685667908)]

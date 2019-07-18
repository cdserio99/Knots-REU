#!/usr/bin/env/python
# This script was saved by SnapPy on Thu Jul 18 10:58:14 2019.

X = Manifold('DT:[(22,68,-34,-80,26,60,-42,-76,110,-50),(-88,8,-96,16,-48,-66,92,-4,32,-58,100,-12,40,74,104,-20,108,30,64,-98,14,-46,72,-90,6,-38,-56,102,-10,94,-2,-54,106,52,82,36,-70,-24,78,44,-62,-28,86,84),(18,)]')

X.dehn_fill((0,1),0)

Z = X.filled_triangulation()

Kverify = Z.copy()

Kverify.dehn_fill((0,1),1)

Kfill = Kverify.filled_triangulation()

Kfill.identify()
#[9_30(0,0), K9a1(0,0)]

Kfill.volume()
#11.9545269682

Z.volume()
#19.1732817344

Z.cusp_translations()
#[(1.159496830 + 1.042578089*I, 3.956831932), (-0.103666251 + 1.555845519*I, 2.651488354)]

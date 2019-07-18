#!/usr/bin/env/python
# This script was saved by SnapPy on Thu Jul 18 10:52:33 2019.

X = Manifold('DT:[(14,-30,58,-36,22,-64),(-44,4,-56,-34,-46,10,-62,-40,52,-2,26,48,-6,18,-54,32,-24,-60,38,-16,-42,28,-50,8,20),(-12,)]')

X.dehn_fill((0,1),0)

Z = X.filled_triangulation()

Kverify = Z.copy()

Kverify.dehn_fill((0,1),1)

Kfill = Kverify.filled_triangulation()

Kfill.identify()
#[t12587(0,0), 8_9(0,0), K8_291(0,0), K8a16(0,0)]

Kfill.volume()
#7.58818022364

Z.volume()
#14.365199086

Z.cusp_translations()
#[(1.157856637 + 1.045262648*I, 4.013758452), (-0.081334541 + 1.557751806*I, 2.6932607448)]

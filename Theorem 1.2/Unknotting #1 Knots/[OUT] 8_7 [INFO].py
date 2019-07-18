#!/usr/bin/env/python
# This script was saved by SnapPy on Thu Jul 18 10:52:12 2019.

X = Manifold('DT:[(26,-10,-30,50,-28,44,56,-22,4,-6,32,-12,46,38,18,42,-54,24,2,-60,20,-16,-36,-58),(8,-40,-62,14,-34,-48),(-52,)]')

X.dehn_fill((0,1),1)

Z = X.filled_triangulation()

Kverify = Z.copy()

Kverify.dehn_fill((0,1),1)

Kfill = Kverify.filled_triangulation()

Kfill.identify()
#[t11034(0,0), 8_7(0,0), K8_236(0,0), K8a6(0,0)]

Kfill.volume()
#7.0221965891

Z.volume()
#14.1226489913

Z.cusp_translations()
#[(-1.168171469 + 1.054960726*I, 3.936722728), (0.134569038 + 1.568265885*I, 2.648203920)]

#!/usr/bin/env/python
# This script was saved by SnapPy on Thu Jul 18 10:54:31 2019.

X = Manifold('DT:[(-18,-8,36,-16,30,22,20,-4,26,-32,12,10,2,-38,14,-24,42),(-28,6,-44,34),(-40,)]')

X.dehn_fill((0,1),1)

Z = X.filled_triangulation()

Kverify = Z.copy()

Kverify.dehn_fill((0,1),1)

Kfill = Kverify.filled_triangulation()

Kfill.identify()
#[v3505(0,0), 8_21(0,0), K7_127(0,0), K8n2(0,0)]

Kfill.volume()
#6.78371351984

Z.volume()
#12.0058342673

Z.cusp_translations()
#[(-0.964959585 + 1.021297381*I, 4.288195704), (-0.0607538637 + 1.4037465258*I, 3.1198816606)]

#!/usr/bin/env/python
# This script was saved by SnapPy on Thu Jul 18 11:19:03 2019.

X = Manifold('DT:[(-10,-44,52,38),(26,-6,42,-48,-32,-30,-28,12,-40,46,-20,-18,-16,50,-24,8,-36,22,-2,34,-14),(4,)]')

X.dehn_fill((0,1),0)

Z = X.filled_triangulation()

Kverify = Z.copy()

Kverify.dehn_fill((0,1),1)

Kfill = Kverify.filled_triangulation()

Kfill.identify()
#[10_137(0,0), K10n2(0,0)]

Kfill.volume()
#9.2505562627

Z.volume()
#14.5981492858

Z.cusp_translations()
#[(-0.92582035 + 1.08879498*I, 4.06919285), (0.10228373 + 1.42553704*I, 3.10796325)]

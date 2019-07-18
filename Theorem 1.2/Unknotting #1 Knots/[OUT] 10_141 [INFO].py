#!/usr/bin/env/python
# This script was saved by SnapPy on Thu Jul 18 11:19:27 2019.

X = Manifold('DT:[(-14,42,60,-20,36,-28),(-4,50,30,-10,54,-44,-16,-12,48,-38,-56,8,-46,24,2,-52,32,18,26,-40,58,-34,22),(6,)]')

X.dehn_fill((0,1),0)

Z = X.filled_triangulation()

Kverify = Z.copy()

Kverify.dehn_fill((0,1),1)

Kfill = Kverify.filled_triangulation()

Kfill.identify()
#[o9_39277(0,0), 10_141(0,0), K10n25(0,0)]

Kfill.volume()
#7.93647422921

Z.volume()
#14.3448469942

Z.cusp_translations()
#[(-1.2062622344 + 0.9348021932*I, 4.4002565209), (-0.2382033444 + 1.5073761591*I, 2.7288274538)]

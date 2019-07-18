#!/usr/bin/env/python
# This script was saved by SnapPy on Thu Jul 18 11:17:16 2019.

X = Manifold('DT:[(-18,-156,-60,130,36,-22,-170,142),(10,90,-16,100,-50,-112,-144,64,-126,2,-98,56,122,-72,114,28,102,166,-118,68,-152,-6,94,32,-160,-40,-134,52,148,-44,26,-110,-108,-106,-104,48,20,-34,-128,58,154,-168,-140,-86,-84,-82,-80,-78,164,-146,42,136,-54,-150,-30,158,4,-96,-38,120,-70,24,12,-88,162,74,-116,66,132,-8,92,-62,124,-46,-76,-138),(-14,)]')

X.dehn_fill((0,1),0)

Z = X.filled_triangulation()

Kverify = Z.copy()

Kverify.dehn_fill((0,1),1)

Kfill = Kverify.filled_triangulation()

Kfill.identify()
#[10_119(0,0), K10a85(0,0)]

Kfill.volume()
#15.938694126

Z.volume()
#33.983233515

Z.cusp_translations()
#[(-0.60358692 + 1.35839861*I, 7.65821018), (0.27846988 + 3.66589868*I, 2.675055650)]

#!/usr/bin/env/python
# This script was saved by SnapPy on Thu Jul 18 11:01:44 2019.

X = Manifold('DT:[(66,-64,-30,-90,-38,24,42,78,100,-74,52,12,-54,10,-6,62,96,-58,-8,56,-22,14,-80,-98,-76,-44,40,-26,82,72,32,-4,-92,88,86,84,34,46,16,-50,20,-36,70,68),(28,2,-102,60,18,-48),(-94,)]')

X.dehn_fill((0,1),1)

Z = X.filled_triangulation()

Kverify = Z.copy()

Kverify.dehn_fill((0,1),1)

Kfill = Kverify.filled_triangulation()

Kfill.identify()
#[10_10(0,0), K10a64(0,0)]

Kfill.volume()
#9.1805736441

Z.volume()
#15.6222720219

Z.cusp_translations()
#[(1.077028686 + 1.067334265*I, 4.085914366), (-0.068682390 + 1.514752769*I, 2.879041711)]

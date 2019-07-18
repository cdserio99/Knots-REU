#!/usr/bin/env/python
# This script was saved by SnapPy on Thu Jul 18 11:00:59 2019.

X = Manifold('DT:[(14,50,-40,-70,60,-30,42,76,74,72,6,-52,36,-56,44,-8,78,26,-66,22,-2,12,-62,-80,-28,4,68,-24,64,-84,10,48,-34,54,-38,20,18,16),(32,-58,-46,86),(82,)]')

X.dehn_fill((0,1),1)

Z = X.filled_triangulation()

Kverify = Z.copy()

Kverify.dehn_fill((0,1),1)

Kfill = Kverify.filled_triangulation()

Kfill.identify()
#[10_7(0,0), K10a65(0,0)]

Kfill.volume()
#9.1159063956

Z.volume()
#15.593958377

Z.cusp_translations()
#[(-1.083062002 + 1.062826251*I, 4.098144575), (0.058034036 + 1.516329446*I, 2.872473158)]

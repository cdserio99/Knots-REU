#!/usr/bin/env/python
# This script was saved by SnapPy on Thu Jul 18 11:20:38 2019.

X = Manifold('DT:[(14,-88,-78,-22,66,-34),(2,-46,-36,-68,52,-6,-80,-58,38,18,-10,48,84,-70,26,-56,-86,-64,32,76,24,-44,-42,72,-28,16,12,-50,82,60,-40,-20,-8,54,74,-30,-62),(-4,)]')

X.dehn_fill((0,1),0)

Z = X.filled_triangulation()

Kverify = Z.copy()

Kverify.dehn_fill((0,1),1)

Kfill = Kverify.filled_triangulation()

Kfill.identify()
#[10_147(0,0), K10n24(0,0)]

Kfill.volume()
#9.4175909160

Z.volume()
#16.182818234

Z.cusp_translations()
#[(1.091047589 + 1.067949348*I, 3.823852045), (-0.181812821 + 1.515864357*I, 2.693961553)]

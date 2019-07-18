X = Manifold('DT:[(14,-88,-78,-22,66,-34),(2,-46,-36,-68,52,-6,-80,-58,38,18,-10,48,84,-70,26,-56,-86,-64,32,76,24,-44,-42,72,-28,16,12,-50,82,60,-40,-20,-8,54,74,-30,-62),(-4,)]')
X.dehn_fill((0,1),0)
Z = X.filled_triangulation()
Kverify = Z.copy()
Kverify.dehn_fill((0,1),1)
Kfill = Kverify.filled_triangulation()
Kfill.identify()
Kfill.volume()
Z.volume()
Z.cusp_translations()

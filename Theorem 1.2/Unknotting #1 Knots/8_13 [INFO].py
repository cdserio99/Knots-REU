X = Manifold('DT:[(20,-66,54,-32,58,36,24,-62,28),(-12,-48,18,38,14,-50,-8,44,-4,-64,26,52,30,-56,34,-22,60,-10,-46,6,-42,-16,-40),(-2,)]')
X.dehn_fill((0,1),0)
Z = X.filled_triangulation()
Kverify = Z.copy()
Kverify.dehn_fill((0,1),1)
Kfill = Kverify.filled_triangulation()
Kfill.identify()
Kfill.volume()
Z.volume()
Z.cusp_translations()

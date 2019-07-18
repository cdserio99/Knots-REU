X = Manifold('DT:[(40,-28,18,-44,2,-20,-24,6,-32,26,-38,-14,-12,-48,34,-16,46,-8,-22),(10,50,36,30,-4),(42,)]')
X.dehn_fill((0,1),1)
Z = X.filled_triangulation()
Kverify = Z.copy()
Kverify.dehn_fill((0,1),1)
Kfill = Kverify.filled_triangulation()
Kfill.identify()
Kfill.volume()
Z.volume()
Z.cusp_translations()

X = Manifold('DT:[(36,-20,46,-34,4,52,-40,54,38,26,-48,32,-10,50,-44,-42,-6,22,-28,-12,-16,-30),(-24,8,-2,-18,14,-58),(-56,)]')
X.dehn_fill((0,1),1)
Z = X.filled_triangulation()
Kverify = Z.copy()
Kverify.dehn_fill((0,1),1)
Kfill = Kverify.filled_triangulation()
Kfill.identify()
Kfill.volume()
Z.volume()
Z.cusp_translations()

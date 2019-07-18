X = Manifold('DT:[(-14,70,-42,52,-28,-26,-60,36,-72,-44,54,-64,48,-10,-8,58,-68,40,-76,16,-2,32,80,22,-88,12,-30,-82,20,-6,90,-24,84,18,4,-34,78),(74,-38,-66,-56,-46,92,62,-50),(86,)]')
X.dehn_fill((0,1),1)
Z = X.filled_triangulation()
Kverify = Z.copy()
Kverify.dehn_fill((0,1),1)
Kfill = Kverify.filled_triangulation()
Kfill.identify()
Kfill.volume()
Z.volume()
Z.cusp_translations()

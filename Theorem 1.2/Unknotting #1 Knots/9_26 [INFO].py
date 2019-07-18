X = Manifold('DT:[(-16,-14,-40,70,-50,-28,58,-2,-78,56,-62,32,-6,-80,-52,-72,22,44,-12,84,-20,-60,30,-8,88,66,-36,-76,4,54,74,-24,-46,10,-86,64,-34,42,-18),(-68,90,38,-26,48),(82,)]')
X.dehn_fill((0,1),1)
Z = X.filled_triangulation()
Kverify = Z.copy()
Kverify.dehn_fill((0,1),1)
Kfill = Kverify.filled_triangulation()
Kfill.identify()
Kfill.volume()
Z.volume()
Z.cusp_translations()

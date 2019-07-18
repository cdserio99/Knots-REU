X = Manifold('DT:[(-84,34,-16,-62,96,-48,-24,78,88,-38,8,70,-92,44,-100,52,-80,-18,64,2,30,-56,-10,72,26,32,-42,98,-50,14,76,-86,36,6,-60,-94,46,-22,-68,90,40),(-82,20,-66,-4,58,12,-74,-28,54,104),(102,)]')
X.dehn_fill((0,1),1)
Z = X.filled_triangulation()
Kverify = Z.copy()
Kverify.dehn_fill((0,1),1)
Kfill = Kverify.filled_triangulation()
Kfill.identify()
Kfill.volume()
Z.volume()
Z.cusp_translations()

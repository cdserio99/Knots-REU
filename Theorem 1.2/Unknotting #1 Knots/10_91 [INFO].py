X = Manifold('DT:[(18,116,-54,-28,126,100,-38,136),(16,-82,110,-48,58,-8,76,96,-106,44,-2,70,-90,-20,-118,32,130,60,-10,78,-30,-128,-102,40,-88,-86,-84,-114,52,26,-124,-98,36,-134,-68,-66,-64,112,-50,-24,-122,4,-72,92,22,120,-34,-132,-62,12,-80,108,-46,56,6,-74,94,-104,42),(14,)]')
X.dehn_fill((0,1),0)
Z = X.filled_triangulation()
Kverify = Z.copy()
Kverify.dehn_fill((0,1),1)
Kfill = Kverify.filled_triangulation()
Kfill.identify()
Kfill.volume()
Z.volume()
Z.cusp_translations()

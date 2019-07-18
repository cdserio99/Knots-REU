#!/usr/bin/env/python
# This script was saved by SnapPy on Thu Jul 18 10:58:37 2019.

X = Manifold('DT:[(-84,34,-16,-62,96,-48,-24,78,88,-38,8,70,-92,44,-100,52,-80,-18,64,2,30,-56,-10,72,26,32,-42,98,-50,14,76,-86,36,6,-60,-94,46,-22,-68,90,40),(-82,20,-66,-4,58,12,-74,-28,54,104),(102,)]')

X.dehn_fill((0,1),1)

Z = X.filled_triangulation()

Kverify = Z.copy()

Kverify.dehn_fill((0,1),1)

Kfill = Kverify.filled_triangulation()

Kfill.identify()
#[9_33(0,0), K9a11(0,0)]

Kfill.volume()
#13.2804556363

Z.volume()
#20.7272442824

Z.cusp_translations()
#[(1.198383541 + 1.007779618*I, 4.079961897), (-0.005367621 + 1.562310228*I, 2.620107795)]

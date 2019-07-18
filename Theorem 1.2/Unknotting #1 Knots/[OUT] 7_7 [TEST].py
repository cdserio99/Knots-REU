#!/usr/bin/env/python
# This script was saved by SnapPy on Thu Jul 18 10:52:06 2019.

X = Manifold('DT:[(-36,18,-44,24,34,-16,46,-28,42,-8,32,30,4,-12,38,22,20,-2,10,-48,26),(-6,-40,14,-52),(-50,)]')

X.dehn_fill((0,1),1)

Z = X.filled_triangulation()

Z.solution_type()
#'all tetrahedra positively oriented'

Z.volume()
#13.9272889591

Kverify = Z.copy()

Kverify.dehn_fill((0,1),1)

Kfill = Kverify.filled_triangulation()

Kfill.solution_type()
#'all tetrahedra positively oriented'

Kfill.identify()
#[t12656(0,0), 7_7(0,0), K8_294(0,0), K7a1(0,0)]

Kfill.volume()
#7.64337517236

Z.dehn_fill((-25,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'contains negatively oriented tetrahedra'

Knprime.volume()
#13.891047507

Knprime.identify()
#[]

Z.dehn_fill((-24,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'contains negatively oriented tetrahedra'

Knprime.volume()
#13.887716328

Knprime.identify()
#[]

Z.dehn_fill((-23,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#13.883905181

Knprime.identify()
#[]

Z.dehn_fill((-22,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'contains negatively oriented tetrahedra'

Knprime.volume()
#13.8795175435

Knprime.identify()
#[]

Z.dehn_fill((-21,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'contains negatively oriented tetrahedra'

Knprime.volume()
#13.8744314470

Knprime.identify()
#[]

Z.dehn_fill((-20,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#13.8684910231

Knprime.identify()
#[]

Z.dehn_fill((-19,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'contains negatively oriented tetrahedra'

Knprime.volume()
#13.8614945977

Knprime.identify()
#[]

Z.dehn_fill((-18,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#13.8531776398

Knprime.identify()
#[]

Z.dehn_fill((-17,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'contains negatively oriented tetrahedra'

Knprime.volume()
#13.8431878799

Knprime.identify()
#[]

Z.dehn_fill((-16,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'contains negatively oriented tetrahedra'

Knprime.volume()
#13.831048245

Knprime.identify()
#[]

Z.dehn_fill((-15,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'contains negatively oriented tetrahedra'

Knprime.volume()
#13.816100373

Knprime.identify()
#[]

Z.dehn_fill((-14,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#13.797416335

Knprime.identify()
#[]

Z.dehn_fill((-13,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#13.773656784

Knprime.identify()
#[]

Z.dehn_fill((-12,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#13.7428358879

Knprime.identify()
#[]

Z.dehn_fill((-11,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#13.701918562

Knprime.identify()
#[]

Z.dehn_fill((-10,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#13.6461051961

Knprime.identify()
#[]

Z.dehn_fill((-9,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#13.5675145774

Knprime.identify()
#[]

Z.dehn_fill((-8,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'contains negatively oriented tetrahedra'

Knprime.volume()
#13.4526788934

Knprime.identify()
#[]

Z.dehn_fill((-7,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'contains negatively oriented tetrahedra'

Knprime.volume()
#13.2776888761

Knprime.identify()
#[]

Z.dehn_fill((-6,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#12.9988980581

Knprime.identify()
#[]

Z.dehn_fill((-5,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#12.5360820033

Knprime.identify()
#[]

Z.dehn_fill((-4,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#11.7420472920

Knprime.identify()
#[]

Z.dehn_fill((-3,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#10.3193955357

Knprime.identify()
#[]

Z.dehn_fill((-2,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#7.64337517236

Knprime.identify()
#[t12656(0,0), 7_7(0,0), K8_294(0,0), K7a1(0,0)]

Z.dehn_fill((-1,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#10.0377298182

Knprime.identify()
#[]

Z.dehn_fill((0,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#11.5294863008

Knprime.identify()
#[]

Z.dehn_fill((1,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#12.3986389407

Knprime.identify()
#[]

Z.dehn_fill((2,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#12.916032407

Knprime.identify()
#[]

Z.dehn_fill((3,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#13.2276199977

Knprime.identify()
#[]

Z.dehn_fill((4,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#13.4212600204

Knprime.identify()
#[]

Z.dehn_fill((5,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#13.546863008

Knprime.identify()
#[]

Z.dehn_fill((6,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#13.6319262884

Knprime.identify()
#[]

Z.dehn_fill((7,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#13.6918085658

Knprime.identify()
#[]

Z.dehn_fill((8,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'contains negatively oriented tetrahedra'

Knprime.volume()
#13.7353925372

Knprime.identify()
#[]

Z.dehn_fill((9,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#13.7680264475

Knprime.identify()
#[]

Z.dehn_fill((10,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'contains negatively oriented tetrahedra'

Knprime.volume()
#13.7930584877

Knprime.identify()
#[]

Z.dehn_fill((11,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#13.812660522

Knprime.identify()
#[]

Z.dehn_fill((12,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#13.8282866130

Knprime.identify()
#[]

Z.dehn_fill((13,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'contains negatively oriented tetrahedra'

Knprime.volume()
#13.8409378206

Knprime.identify()
#[]

Z.dehn_fill((14,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'contains negatively oriented tetrahedra'

Knprime.volume()
#13.8513205370

Knprime.identify()
#[]

Z.dehn_fill((15,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#13.8599442227

Knprime.identify()
#[]

Z.dehn_fill((16,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#13.8671835061

Knprime.identify()
#[]

Z.dehn_fill((17,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#13.873318682

Knprime.identify()
#[]

Z.dehn_fill((18,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#13.878562750

Knprime.identify()
#[]

Z.dehn_fill((19,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#13.8830798545

Knprime.identify()
#[]

Z.dehn_fill((20,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#13.8869981056

Knprime.identify()
#[]

Z.dehn_fill((21,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'contains negatively oriented tetrahedra'

Knprime.volume()
#13.8904186485

Knprime.identify()
#[]

Z.dehn_fill((22,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'contains negatively oriented tetrahedra'

Knprime.volume()
#13.8934221843

Knprime.identify()
#[]

Z.dehn_fill((23,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#13.8960737259

Knprime.identify()
#[]

Z.dehn_fill((24,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#13.8984261143

Knprime.identify()
#[]

Z.dehn_fill((25,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#13.900522650

Knprime.identify()
#[]

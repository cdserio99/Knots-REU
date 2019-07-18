#!/usr/bin/env/python
# This script was saved by SnapPy on Thu Jul 18 10:58:31 2019.

X = Manifold('DT:[(22,68,-34,-80,26,60,-42,-76,110,-50),(-88,8,-96,16,-48,-66,92,-4,32,-58,100,-12,40,74,104,-20,108,30,64,-98,14,-46,72,-90,6,-38,-56,102,-10,94,-2,-54,106,52,82,36,-70,-24,78,44,-62,-28,86,84),(18,)]')

X.dehn_fill((0,1),0)

Z = X.filled_triangulation()

Z.solution_type()
#'all tetrahedra positively oriented'

Z.volume()
#19.173281734

Kverify = Z.copy()

Kverify.dehn_fill((0,1),1)

Kfill = Kverify.filled_triangulation()

Kfill.solution_type()
#'all tetrahedra positively oriented'

Kfill.identify()
#[9_30(0,0), K9a1(0,0)]

Kfill.volume()
#11.9545269682

Z.dehn_fill((-27,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#19.146833701

Knprime.identify()
#[]

Z.dehn_fill((-26,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#19.144604182

Knprime.identify()
#[]

Z.dehn_fill((-25,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#19.142080889

Knprime.identify()
#[]

Z.dehn_fill((-24,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'contains negatively oriented tetrahedra'

Knprime.volume()
#19.139209953

Knprime.identify()
#[]

Z.dehn_fill((-23,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'contains negatively oriented tetrahedra'

Knprime.volume()
#19.135924594

Knprime.identify()
#[]

Z.dehn_fill((-22,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#19.132141231

Knprime.identify()
#[]

Z.dehn_fill((-21,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'contains negatively oriented tetrahedra'

Knprime.volume()
#19.127754165

Knprime.identify()
#[]

Z.dehn_fill((-20,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#19.122628176

Knprime.identify()
#[]

Z.dehn_fill((-19,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#19.116588100

Knprime.identify()
#[]

Z.dehn_fill((-18,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#19.1094038347

Knprime.identify()
#[]

Z.dehn_fill((-17,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#19.100768412

Knprime.identify()
#[]

Z.dehn_fill((-16,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#19.090265174

Knprime.identify()
#[]

Z.dehn_fill((-15,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#19.077317511

Knprime.identify()
#[]

Z.dehn_fill((-14,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#19.0611097688

Knprime.identify()
#[]

Z.dehn_fill((-13,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#19.0404590459

Knprime.identify()
#[]

Z.dehn_fill((-12,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'contains negatively oriented tetrahedra'

Knprime.volume()
#19.0136002633

Knprime.identify()
#[]

Z.dehn_fill((-11,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#18.977811905

Knprime.identify()
#[]

Z.dehn_fill((-10,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#18.928736035

Knprime.identify()
#[]

Z.dehn_fill((-9,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#18.859083399

Knprime.identify()
#[]

Z.dehn_fill((-8,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#18.7560411865

Knprime.identify()
#[]

Z.dehn_fill((-7,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#18.595829564

Knprime.identify()
#[]

Z.dehn_fill((-6,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#18.331899077

Knprime.identify()
#[]

Z.dehn_fill((-5,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#17.8696464157

Knprime.identify()
#[]

Z.dehn_fill((-4,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#17.0158234895

Knprime.identify()
#[]

Z.dehn_fill((-3,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#15.362001378

Knprime.identify()
#[]

Z.dehn_fill((-2,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#11.9545269682

Knprime.identify()
#[9_30(0,0), K9a1(0,0)]

Z.dehn_fill((-1,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#14.9302205128

Knprime.identify()
#[]

Z.dehn_fill((0,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#16.720220425

Knprime.identify()
#[]

Z.dehn_fill((1,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#17.702653761

Knprime.identify()
#[]

Z.dehn_fill((2,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'contains negatively oriented tetrahedra'

Knprime.volume()
#18.240312219

Knprime.identify()
#[]

Z.dehn_fill((3,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#18.5433088536

Knprime.identify()
#[]

Z.dehn_fill((4,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#18.7239532979

Knprime.identify()
#[]

Z.dehn_fill((5,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#18.8382842396

Knprime.identify()
#[]

Z.dehn_fill((6,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#18.914565153

Knprime.identify()
#[]

Z.dehn_fill((7,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#18.9677530352

Knprime.identify()
#[]

Z.dehn_fill((8,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#19.006215207

Knprime.identify()
#[]

Z.dehn_fill((9,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#19.0348829644

Knprime.identify()
#[]

Z.dehn_fill((10,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#19.0567992560

Knprime.identify()
#[]

Z.dehn_fill((11,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#19.073917997

Knprime.identify()
#[]

Z.dehn_fill((12,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#19.0875376628

Knprime.identify()
#[]

Z.dehn_fill((13,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#19.0985472106

Knprime.identify()
#[]

Z.dehn_fill((14,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'contains negatively oriented tetrahedra'

Knprime.volume()
#19.1075712192

Knprime.identify()
#[]

Z.dehn_fill((15,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#19.1150586038

Knprime.identify()
#[]

Z.dehn_fill((16,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#19.121338561

Knprime.identify()
#[]

Z.dehn_fill((17,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#19.126656836

Knprime.identify()
#[]

Z.dehn_fill((18,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#19.1311998247

Knprime.identify()
#[]

Z.dehn_fill((19,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#19.135110941

Knprime.identify()
#[]

Z.dehn_fill((20,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#19.138501964

Knprime.identify()
#[]

Z.dehn_fill((21,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'contains negatively oriented tetrahedra'

Knprime.volume()
#19.141461045

Knprime.identify()
#[]

Z.dehn_fill((22,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#19.1440584476

Knprime.identify()
#[]

Z.dehn_fill((23,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#19.1463507248

Knprime.identify()
#[]

Z.dehn_fill((24,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'contains negatively oriented tetrahedra'

Knprime.volume()
#19.148383808

Knprime.identify()
#[]

Z.dehn_fill((25,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#19.150195308

Knprime.identify()
#[]

Z.dehn_fill((26,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'contains negatively oriented tetrahedra'

Knprime.volume()
#19.1518162616

Knprime.identify()
#[]

Z.dehn_fill((27,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#19.1532724603

Knprime.identify()
#[]

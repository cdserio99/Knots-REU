#!/usr/bin/env/python
# This script was saved by SnapPy on Thu Jul 18 10:56:20 2019.

X = Manifold('DT:[(72,-56,14,42,-84,52,64,-30,-74,58,-4,40,82,-50,62,20,-76,46,-86,54,-12,-28,-60,-70,36,8,-24,-66,32,16,-44,-6,-22,80,-48),(68,-34,-18,2,-88,-38,-10,26),(-78,)]')

X.dehn_fill((0,1),1)

Z = X.filled_triangulation()

Z.solution_type()
#'all tetrahedra positively oriented'

Z.volume()
#18.1853958821

Kverify = Z.copy()

Kverify.dehn_fill((0,1),1)

Kfill = Kverify.filled_triangulation()

Kfill.solution_type()
#'all tetrahedra positively oriented'

Kfill.identify()
#[9_22(0,0), K9a2(0,0)]

Kfill.volume()
#10.6207270212

Z.dehn_fill((-25,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#18.163217450

Knprime.identify()
#[]

Z.dehn_fill((-24,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'contains negatively oriented tetrahedra'

Knprime.volume()
#18.161475355

Knprime.identify()
#[]

Z.dehn_fill((-23,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#18.159519910

Knprime.identify()
#[]

Z.dehn_fill((-22,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#18.157314853

Knprime.identify()
#[]

Z.dehn_fill((-21,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#18.154815887

Knprime.identify()
#[]

Z.dehn_fill((-20,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#18.151968453

Knprime.identify()
#[]

Z.dehn_fill((-19,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#18.148704745

Knprime.identify()
#[]

Z.dehn_fill((-18,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'contains negatively oriented tetrahedra'

Knprime.volume()
#18.144939662

Knprime.identify()
#[]

Z.dehn_fill((-17,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'contains negatively oriented tetrahedra'

Knprime.volume()
#18.1405652444

Knprime.identify()
#[]

Z.dehn_fill((-16,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#18.135442915

Knprime.identify()
#[]

Z.dehn_fill((-15,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#18.129392468

Knprime.identify()
#[]

Z.dehn_fill((-14,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#18.122176169

Knprime.identify()
#[]

Z.dehn_fill((-13,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#18.1134753296

Knprime.identify()
#[]

Z.dehn_fill((-12,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#18.1028550002

Knprime.identify()
#[]

Z.dehn_fill((-11,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'contains negatively oriented tetrahedra'

Knprime.volume()
#18.089709442

Knprime.identify()
#[]

Z.dehn_fill((-10,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'contains negatively oriented tetrahedra'

Knprime.volume()
#18.0731755044

Knprime.identify()
#[]

Z.dehn_fill((-9,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'contains negatively oriented tetrahedra'

Knprime.volume()
#18.051990619

Knprime.identify()
#[]

Z.dehn_fill((-8,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#18.0242515571

Knprime.identify()
#[]

Z.dehn_fill((-7,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#17.9869876785

Knprime.identify()
#[]

Z.dehn_fill((-6,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'contains negatively oriented tetrahedra'

Knprime.volume()
#17.9353706988

Knprime.identify()
#[]

Z.dehn_fill((-5,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'contains negatively oriented tetrahedra'

Knprime.volume()
#17.8611749134

Knprime.identify()
#[]

Z.dehn_fill((-4,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#17.7496091859

Knprime.identify()
#[]

Z.dehn_fill((-3,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#17.5724576139

Knprime.identify()
#[]

Z.dehn_fill((-2,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'contains negatively oriented tetrahedra'

Knprime.volume()
#17.272817956

Knprime.identify()
#[]

Z.dehn_fill((-1,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#16.7327299043

Knprime.identify()
#[]

Z.dehn_fill((0,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'contains negatively oriented tetrahedra'

Knprime.volume()
#15.7166987456

Knprime.identify()
#[]

Z.dehn_fill((1,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#13.7872456518

Knprime.identify()
#[]

Z.dehn_fill((2,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#10.620727021

Knprime.identify()
#[9_22(0,0), K9a2(0,0)]

Z.dehn_fill((3,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'contains negatively oriented tetrahedra'

Knprime.volume()
#14.412126309

Knprime.identify()
#[]

Z.dehn_fill((4,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#16.0642424298

Knprime.identify()
#[]

Z.dehn_fill((5,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#16.9162109039

Knprime.identify()
#[]

Z.dehn_fill((6,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#17.3721130904

Knprime.identify()
#[]

Z.dehn_fill((7,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#17.6295484051

Knprime.identify()
#[]

Z.dehn_fill((8,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#17.7846842319

Knprime.identify()
#[]

Z.dehn_fill((9,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#17.884028058

Knprime.identify()
#[]

Z.dehn_fill((10,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#17.9510060094

Knprime.identify()
#[]

Z.dehn_fill((11,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#17.9981221602

Knprime.identify()
#[]

Z.dehn_fill((12,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#18.0324469942

Knprime.identify()
#[]

Z.dehn_fill((13,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#18.058190847

Knprime.identify()
#[]

Z.dehn_fill((14,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#18.0779760386

Knprime.identify()
#[]

Z.dehn_fill((15,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#18.0935001914

Knprime.identify()
#[]

Z.dehn_fill((16,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#18.1058995269

Knprime.identify()
#[]

Z.dehn_fill((17,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#18.115956787

Knprime.identify()
#[]

Z.dehn_fill((18,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#18.1242249443

Knprime.identify()
#[]

Z.dehn_fill((19,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#18.131103374

Knprime.identify()
#[]

Z.dehn_fill((20,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#18.136886206

Knprime.identify()
#[]

Z.dehn_fill((21,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#18.141793856

Knprime.identify()
#[]

Z.dehn_fill((22,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'contains negatively oriented tetrahedra'

Knprime.volume()
#18.1459940817

Knprime.identify()
#[]

Z.dehn_fill((23,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'contains negatively oriented tetrahedra'

Knprime.volume()
#18.149616363

Knprime.identify()
#[]

Z.dehn_fill((24,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#18.152761903

Knprime.identify()
#[]

Z.dehn_fill((25,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'contains negatively oriented tetrahedra'

Knprime.volume()
#18.155510719

Knprime.identify()
#[]

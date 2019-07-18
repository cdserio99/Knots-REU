#!/usr/bin/env/python
# This script was saved by SnapPy on Thu Jul 18 10:55:34 2019.

X = Manifold('DT:[(48,24,22,20,18,-42,32,-54,10,8,6,4,-46,40,-50,36,-64,14,-58,28,-62,68,-16,2,-26,60,-30,70,-12,52,-38),(-34,56,72,44),(66,)]')

X.dehn_fill((0,1),1)

Z = X.filled_triangulation()

Z.solution_type()
#'all tetrahedra positively oriented'

Z.volume()
#15.381819861

Kverify = Z.copy()

Kverify.dehn_fill((0,1),1)

Kfill = Kverify.filled_triangulation()

Kfill.solution_type()
#'contains negatively oriented tetrahedra'

Kfill.identify()
#[9_14(0,0), K9a17(0,0)]

Kfill.volume()
#8.9549892620

Z.dehn_fill((-26,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#15.3495287798

Knprime.identify()
#[]

Z.dehn_fill((-25,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'contains negatively oriented tetrahedra'

Knprime.volume()
#15.3466874180

Knprime.identify()
#[]

Z.dehn_fill((-24,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#15.3434547531

Knprime.identify()
#[]

Z.dehn_fill((-23,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'contains negatively oriented tetrahedra'

Knprime.volume()
#15.3397556907

Knprime.identify()
#[]

Z.dehn_fill((-22,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'contains negatively oriented tetrahedra'

Knprime.volume()
#15.335496277

Knprime.identify()
#[]

Z.dehn_fill((-21,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#15.330557739

Knprime.identify()
#[]

Z.dehn_fill((-20,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#15.324788211

Knprime.identify()
#[]

Z.dehn_fill((-19,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#15.3179910793

Knprime.identify()
#[]

Z.dehn_fill((-18,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#15.309908268

Knprime.identify()
#[]

Z.dehn_fill((-17,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#15.300195812

Knprime.identify()
#[]

Z.dehn_fill((-16,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#15.2883874039

Knprime.identify()
#[]

Z.dehn_fill((-15,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'contains negatively oriented tetrahedra'

Knprime.volume()
#15.2738387326

Knprime.identify()
#[]

Z.dehn_fill((-14,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'contains negatively oriented tetrahedra'

Knprime.volume()
#15.2556402509

Knprime.identify()
#[]

Z.dehn_fill((-13,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#15.2324765314

Knprime.identify()
#[]

Z.dehn_fill((-12,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'contains negatively oriented tetrahedra'

Knprime.volume()
#15.2023921889

Knprime.identify()
#[]

Z.dehn_fill((-11,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'contains negatively oriented tetrahedra'

Knprime.volume()
#15.162388460

Knprime.identify()
#[]

Z.dehn_fill((-10,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#15.1077011516

Knprime.identify()
#[]

Z.dehn_fill((-9,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'contains negatively oriented tetrahedra'

Knprime.volume()
#15.0304566289

Knprime.identify()
#[]

Z.dehn_fill((-8,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'contains negatively oriented tetrahedra'

Knprime.volume()
#14.9170771116

Knprime.identify()
#[]

Z.dehn_fill((-7,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#14.7431510240

Knprime.identify()
#[]

Z.dehn_fill((-6,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#14.4633982262

Knprime.identify()
#[]

Z.dehn_fill((-5,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'contains negatively oriented tetrahedra'

Knprime.volume()
#13.993463629

Knprime.identify()
#[]

Z.dehn_fill((-4,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#13.1796103273

Knprime.identify()
#[]

Z.dehn_fill((-3,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#11.7252400213

Knprime.identify()
#[]

Z.dehn_fill((-2,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#8.9549892620

Knprime.identify()
#[9_14(0,0), K9a17(0,0)]

Z.dehn_fill((-1,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#11.4108046523

Knprime.identify()
#[]

Z.dehn_fill((0,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'contains negatively oriented tetrahedra'

Knprime.volume()
#12.9870903743

Knprime.identify()
#[]

Z.dehn_fill((1,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#13.8785076404

Knprime.identify()
#[]

Z.dehn_fill((2,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#14.3958573606

Knprime.identify()
#[]

Z.dehn_fill((3,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#14.7024835147

Knprime.identify()
#[]

Z.dehn_fill((4,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#14.8914574499

Knprime.identify()
#[]

Z.dehn_fill((5,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#15.0135254922

Knprime.identify()
#[]

Z.dehn_fill((6,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'contains negatively oriented tetrahedra'

Knprime.volume()
#15.0960180518

Knprime.identify()
#[]

Z.dehn_fill((7,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#15.154022900

Knprime.identify()
#[]

Z.dehn_fill((8,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'contains negatively oriented tetrahedra'

Knprime.volume()
#15.1962120728

Knprime.identify()
#[]

Z.dehn_fill((9,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#15.2277888485

Knprime.identify()
#[]

Z.dehn_fill((10,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#15.2520039307

Knprime.identify()
#[]

Z.dehn_fill((11,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'contains negatively oriented tetrahedra'

Knprime.volume()
#15.2709632158

Knprime.identify()
#[]

Z.dehn_fill((12,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'contains negatively oriented tetrahedra'

Knprime.volume()
#15.2860754051

Knprime.identify()
#[]

Z.dehn_fill((13,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'contains negatively oriented tetrahedra'

Knprime.volume()
#15.298309774

Knprime.identify()
#[]

Z.dehn_fill((14,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#15.3083500103

Knprime.identify()
#[]

Z.dehn_fill((15,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#15.3166890614

Knprime.identify()
#[]

Z.dehn_fill((16,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#15.3236893371

Knprime.identify()
#[]

Z.dehn_fill((17,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'contains negatively oriented tetrahedra'

Knprime.volume()
#15.3296219499

Knprime.identify()
#[]

Z.dehn_fill((18,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'contains negatively oriented tetrahedra'

Knprime.volume()
#15.3346928984

Knprime.identify()
#[]

Z.dehn_fill((19,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#15.339060919

Knprime.identify()
#[]

Z.dehn_fill((20,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#15.3428498944

Knprime.identify()
#[]

Z.dehn_fill((21,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'contains negatively oriented tetrahedra'

Knprime.volume()
#15.3461576262

Knprime.identify()
#[]

Z.dehn_fill((22,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#15.3490621463

Knprime.identify()
#[]

Z.dehn_fill((23,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#15.3516263160

Knprime.identify()
#[]

Z.dehn_fill((24,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#15.3539012263

Knprime.identify()
#[]

Z.dehn_fill((25,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'contains negatively oriented tetrahedra'

Knprime.volume()
#15.355928743

Knprime.identify()
#[]

Z.dehn_fill((26,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#15.3577434337

Knprime.identify()
#[]

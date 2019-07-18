#!/usr/bin/env/python
# This script was saved by SnapPy on Thu Jul 18 11:11:03 2019.

X = Manifold('DT:[(18,116,-54,-28,126,100,-38,136),(16,-82,110,-48,58,-8,76,96,-106,44,-2,70,-90,-20,-118,32,130,60,-10,78,-30,-128,-102,40,-88,-86,-84,-114,52,26,-124,-98,36,-134,-68,-66,-64,112,-50,-24,-122,4,-72,92,22,120,-34,-132,-62,12,-80,108,-46,56,6,-74,94,-104,42),(14,)]')

X.dehn_fill((0,1),0)

Z = X.filled_triangulation()

Z.solution_type()
#'all tetrahedra positively oriented'

Z.volume()
#20.882207797

Kverify = Z.copy()

Kverify.dehn_fill((0,1),1)

Kfill = Kverify.filled_triangulation()

Kfill.solution_type()
#'all tetrahedra positively oriented'

Kfill.identify()
#[10_91(0,0), K10a106(0,0)]

Kfill.volume()
#13.4870224203

Z.dehn_fill((-29,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#20.859902422

Knprime.identify()
#[]

Z.dehn_fill((-28,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#20.858157778

Knprime.identify()
#[]

Z.dehn_fill((-27,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#20.8562004254

Knprime.identify()
#[]

Z.dehn_fill((-26,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#20.853994381

Knprime.identify()
#[]

Z.dehn_fill((-25,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#20.851495730

Knprime.identify()
#[]

Z.dehn_fill((-24,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#20.848650435

Knprime.identify()
#[]

Z.dehn_fill((-23,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#20.8453914135

Knprime.identify()
#[]

Z.dehn_fill((-22,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#20.8416345694

Knprime.identify()
#[]

Z.dehn_fill((-21,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#20.837273359

Knprime.identify()
#[]

Z.dehn_fill((-20,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#20.832171219

Knprime.identify()
#[]

Z.dehn_fill((-19,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#20.826150848

Knprime.identify()
#[]

Z.dehn_fill((-18,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#20.8189787658

Knprime.identify()
#[]

Z.dehn_fill((-17,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#20.810342620

Knprime.identify()
#[]

Z.dehn_fill((-16,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#20.7998170937

Knprime.identify()
#[]

Z.dehn_fill((-15,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#20.786811429

Knprime.identify()
#[]

Z.dehn_fill((-14,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#20.770486390

Knprime.identify()
#[]

Z.dehn_fill((-13,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#20.7496187686

Knprime.identify()
#[]

Z.dehn_fill((-12,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#20.7223724211

Knprime.identify()
#[]

Z.dehn_fill((-11,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#20.6858958050

Knprime.identify()
#[]

Z.dehn_fill((-10,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#20.635582283

Knprime.identify()
#[]

Z.dehn_fill((-9,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#20.563641526

Knprime.identify()
#[]

Z.dehn_fill((-8,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#20.4561900015

Knprime.identify()
#[]

Z.dehn_fill((-7,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#20.287017257

Knprime.identify()
#[]

Z.dehn_fill((-6,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#20.0038075010

Knprime.identify()
#[]

Z.dehn_fill((-5,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#19.498568504

Knprime.identify()
#[]

Z.dehn_fill((-4,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#18.5521280587

Knprime.identify()
#[]

Z.dehn_fill((-3,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#16.7258069720

Knprime.identify()
#[]

Z.dehn_fill((-2,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#13.4870224203

Knprime.identify()
#[10_91(0,0), K10a106(0,0)]

Z.dehn_fill((-1,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#16.878656807

Knprime.identify()
#[]

Z.dehn_fill((0,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#18.619969336

Knprime.identify()
#[]

Z.dehn_fill((1,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#19.5328056845

Knprime.identify()
#[]

Z.dehn_fill((2,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#20.0226478944

Knprime.identify()
#[]

Z.dehn_fill((3,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#20.2981174442

Knprime.identify()
#[]

Z.dehn_fill((4,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#20.4631440169

Knprime.identify()
#[]

Z.dehn_fill((5,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#20.5682368084

Knprime.identify()
#[]

Z.dehn_fill((6,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#20.6387581971

Knprime.identify()
#[]

Z.dehn_fill((7,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#20.6881742303

Knprime.identify()
#[]

Z.dehn_fill((8,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#20.7240586654

Knprime.identify()
#[]

Z.dehn_fill((9,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#20.7508998261

Knprime.identify()
#[]

Z.dehn_fill((10,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#20.7714814674

Knprime.identify()
#[]

Z.dehn_fill((11,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#20.7875992050

Knprime.identify()
#[]

Z.dehn_fill((12,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#20.8004510928

Knprime.identify()
#[]

Z.dehn_fill((13,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#20.810860228

Knprime.identify()
#[]

Z.dehn_fill((14,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#20.8194067093

Knprime.identify()
#[]

Z.dehn_fill((15,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#20.826508629

Knprime.identify()
#[]

Z.dehn_fill((16,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#20.8324733285

Knprime.identify()
#[]

Z.dehn_fill((17,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#20.837530743

Knprime.identify()
#[]

Z.dehn_fill((18,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#20.841855617

Knprime.identify()
#[]

Z.dehn_fill((19,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#20.845582640

Knprime.identify()
#[]

Z.dehn_fill((20,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#20.8488169622

Knprime.identify()
#[]

Z.dehn_fill((21,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#20.851641626

Knprime.identify()
#[]

Z.dehn_fill((22,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#20.854122914

Knprime.identify()
#[]

Z.dehn_fill((23,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#20.8563142391

Knprime.identify()
#[]

Z.dehn_fill((24,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#20.858259034

Knprime.identify()
#[]

Z.dehn_fill((25,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#20.859992899

Knprime.identify()
#[]

Z.dehn_fill((26,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#20.861545243

Knprime.identify()
#[]

Z.dehn_fill((27,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#20.8629405227

Knprime.identify()
#[]

Z.dehn_fill((28,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#20.864199217

Knprime.identify()
#[]

Z.dehn_fill((29,1),0)

Knprime = Z.filled_triangulation()

Knprime.solution_type()
#'all tetrahedra positively oriented'

Knprime.volume()
#20.8653385756

Knprime.identify()
#[]

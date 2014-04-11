from pyplasm import *

base = CUBOID([41.3,18.86])
scalino1 = T([1,2])([0.57,0.57])(CUBOID([40.16,17.72]))
scalino2 = T([1,2])([1.14,1.14])(CUBOID([39.02,16.58]))

piattaforma = STRUCT([base,scalino1,scalino2])
#VIEW(piattaforma)

plinto = CUBOID([1,1])

plintx1 = T([1,2])([1.14,1.14]) (STRUCT([plinto,T(1)(3.16833)]*13))
plintx2 = T([1,2])([1.14,16.7]) (STRUCT([plinto,T(1)(3.16833)]*13))

plinty1 = T([1,2])([1.14,4.30833]) (STRUCT([plinto,T(2)(3.16833)]*4))
plinty2 = T([1,2])([39.12,4.30833]) (STRUCT([plinto,T(2)(3.16833)]*4))

plintiCoppiaDes = T([1,2])([6.42,7.47666]) (STRUCT([plinto,T(2)(3.16833)]*2))
plintiCoppiaSin = T([1,2])([33.6,7.47666]) (STRUCT([plinto,T(2)(3.16833)]*2))

plinti = COLOR([0.72,0.5,0.3])(STRUCT([plintx1,plintx2,plinty1,plinty2,plintiCoppiaSin,plintiCoppiaDes]))

#VIEW(STRUCT([piattaforma,plinti]))

c = CIRCUMFERENCE(0.5)(20)

colonnex1 = T([1,2])([1.64,1.64]) (STRUCT([c,T(1)(3.16833)]*13))
colonnex2 = T([1,2])([1.64,17.2]) (STRUCT([c,T(1)(3.16833)]*13))

colonney1 = T([1,2])([1.64,4.80833]) (STRUCT([c,T(2)(3.16833)]*4))
colonney2 = T([1,2])([39.62,4.80833]) (STRUCT([c,T(2)(3.16833)]*4))

colonneCoppiaDes = T([1,2])([6.92,7.97666]) (STRUCT([c,T(2)(3.16833)]*2))
colonneCoppiaSin = T([1,2])([34.1,7.97666]) (STRUCT([c,T(2)(3.16833)]*2))

colonne = COLOR([0.4,1,0.4])(STRUCT([colonnex1,colonnex2,colonney1,colonney2,colonneCoppiaDes,colonneCoppiaSin]))

#VIEW(STRUCT([piattaforma,plinti,colonne]))

parete1 = T([1,2])([6.42,4.72]) (CUBOID([28.17,0.5]))
parete2 = T([1,2])([6.42,13.21]) (CUBOID([28.17,0.5]))

pareteTrasv = T([1,2])([30.55,5.22])(CUBOID([0.5,7.99]))

pareteEntrataAlta = T([1,2])([10,5.22])(CUBOID([2.07,3]))
pareteEntrataBassa = T([1,2])([10,10.21])(CUBOID([2.07,3]))

pareti = COLOR([0.545,0.27,0])( STRUCT([parete1,parete2,pareteTrasv,pareteEntrataAlta,pareteEntrataBassa]) )

#VIEW(STRUCT([piattaforma,plinti,colonne,pareti]))

travex1 = T([1,2])([1.34,1.34]) (CUBOID([38.62,0.6]))
travex2 = T([1,2])([1.34,16.9]) (CUBOID([38.62,0.6]))

travey1 = T([1,2])([1.34,1.60833])(CUBOID([0.6,15.58]))
travey2 = T([1,2])([39.32,1.60833])(CUBOID([0.6,15.58]))

traveEntrata = T([1,2])([6.62,4.72])(CUBOID([0.6,8.99]))
traveUscita = T([1,2])([33.79,4.72])(CUBOID([0.6,8.99]))

travi = COLOR([0.48,0.627,0.357])( STRUCT([travex2,travex1,travey1,travey2,traveEntrata,traveUscita]) )

#VIEW(STRUCT([piattaforma,plinti,colonne,pareti,travi]))

secondaTravey1 = T([1,2])([1.34,1.35833])(CUBOID([0.6,16.15]))
secondaTravey2 = T([1,2])([39.32,1.35833])(CUBOID([0.6,16.15]))
secondaTraveEntrata = COLOR(BLUE)(T([1,2])([6.62,4.72])(CUBOID([0.6,8.99])))
secondaTraveUscita = T([1,2])([33.79,4.72])(CUBOID([0.6,8.99]))

secondeTravi = COLOR([1,1,0.4])( (STRUCT([secondaTravey1,secondaTravey2,secondaTraveEntrata,secondaTraveUscita])) )

#VIEW(STRUCT([piattaforma,plinti,colonne,pareti,travi,secondeTravi]))


puntiTettoy1 = AA(MK)([[1.1,1.00833],[1.1,17.78833],[1.1,9.39833,3], [1.94,1.00833],[1.94,17.78833],[1.94,9.39833,3]])
tettoy1 = JOIN(puntiTettoy1)

puntiTettoy2 = AA(MK)([[39.08,1.00833],[39.08,17.78833],[39.08,9.39833,3], [39.92,1.00833],[39.92,17.78833],[39.92,9.39833,3]])
tettoy2 = JOIN(puntiTettoy2)

scalino1 = PROD([scalino1,Q(0.8)])
scalino2 = T(3)(0.8)(PROD([scalino2,Q(0.8)]))
piattaforma = COLOR([1,0.8,0]) (STRUCT([base,scalino1,scalino2]) )

def semicirc():
    def sphere1(p): return [COS(p[0]), SIN(p[0])]
    def domain(n): return INTERVALS(PI)(n)
    return ( MAP(sphere1)(domain(32)) )

s = T([1,2])([1,6])(semicirc())
p = CUBOID([2,6])

arco = PROD([JOIN([s,p]),Q(1)])
arco = MAP([S3,S1,S2])(arco)
arco = T([1,2,3])([30.5,8.22,1.6])(arco)

pareti = T(3)(1.6)(PROD([pareti,Q(7)]))
pareti = COLOR([0.545,0.27,0])  ( SKELETON(1)(DIFFERENCE([pareti,arco])) )

plinti = COLOR([0.72,0.5,0.3]) ( SKELETON(1)(T(3)(1.6)(PROD([plinti,Q(0.8)]))) )
colonne = COLOR([0.98,0.941,0.902]) ( SKELETON(1)(T(3)(2.4)(PROD([colonne,Q(7)]))) )
travi = COLOR([0.72,0.5,0.3])( SKELETON(1)(T(3)(9.4)(PROD([travi,Q(1.2)]))) )
secondeTravi = COLOR([1,0.8,0])( SKELETON(1)(T(3)(10.6)(PROD([secondeTravi,Q(1.2)]))) )
tettoy1 = T(3)(11.8)(tettoy1)
tettoy2 = T(3)(11.8)(tettoy2)
tetti = COLOR([0.545,0.27,0])( SKELETON(1)(STRUCT([tettoy1,tettoy2])) )

paretiPrincipali = SKELETON(1)( STRUCT([pareti,plinti,colonne,travi,secondeTravi,tetti]) ) 
piani = COLOR(WHITE) (STRUCT([base,scalino1,scalino2]) )

VIEW(STRUCT([piani,paretiPrincipali]))

VIEW(STRUCT([pareti,piattaforma,plinti,colonne,travi,secondeTravi,tetti]))

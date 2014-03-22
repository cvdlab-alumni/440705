from pyplasm import *

base = (SKELETON(1)( CUBOID([41.3,18.86])) )
scalino1 = SKELETON(1)( T([1,2])([0.57,0.57])(CUBOID([40.16,17.72])) )
scalino2 = SKELETON(1)( T([1,2])([1.14,1.14])(CUBOID([39.02,16.58])) )

piattaforma = STRUCT([base,scalino1,scalino2])
#VIEW(STRUCT([base,scalino1,scalino2]))

plinto = SKELETON(1)( CUBOID([1,1]) )

plintx1 = T([1,2])([1.14,1.14]) (STRUCT([plinto,T(1)(3.16833)]*13))
plintx2 = T([1,2])([1.14,16.7]) (STRUCT([plinto,T(1)(3.16833)]*13))

plinty1 = T([1,2])([1.14,4.30833]) (STRUCT([plinto,T(2)(3.16833)]*4))
plinty2 = T([1,2])([39.02,4.30833]) (STRUCT([plinto,T(2)(3.16833)]*4))

plintiCoppiaDes = T([1,2])([6.42,7.47666]) (STRUCT([plinto,T(2)(3.16833)]*2))
plintiCoppiaSin = T([1,2])([33.6,7.47666]) (STRUCT([plinto,T(2)(3.16833)]*2))

plinti = STRUCT([plintx1,plintx2,plinty1,plinty2,plintiCoppiaSin,plintiCoppiaDes])

VIEW(STRUCT([piattaforma,plinti]))

c = CIRCUMFERENCE(0.5)(20)

colonnex1 = T([1,2])([1.64,1.64]) (STRUCT([c,T(1)(3.16833)]*13))
colonnex2 = T([1,2])([1.64,17.2]) (STRUCT([c,T(1)(3.16833)]*13))

colonney1 = T([1,2])([1.64,4.80833]) (STRUCT([c,T(2)(3.16833)]*4))
colonney2 = T([1,2])([39.52,4.80833]) (STRUCT([c,T(2)(3.16833)]*4))

colonneCoppiaDes = T([1,2])([6.92,7.97666]) (STRUCT([c,T(2)(3.16833)]*2))
colonneCoppiaSin = T([1,2])([34.1,7.97666]) (STRUCT([c,T(2)(3.16833)]*2))

colonne = STRUCT([colonnex1,colonnex2,colonney1,colonney2,colonneCoppiaDes,colonneCoppiaSin])

VIEW(STRUCT([piattaforma,plinti,colonne]))


#a = (MK)([6.42,4.72])
#b = (MK)([35.09,4.72])
#c = (MK)([6.42,5.22])
#d = (MK)([35.09,5.22])
#linea = JOIN([a,b,c,d])

parete1 = T([1,2])([6.42,4.72]) (CUBOID([28.17,0.5]))
parete2 = T([1,2])([6.42,13.21]) (CUBOID([28.17,0.5]))

pareteTrasv = T([1,2])([30.55,5.22])(CUBOID([0.5,7.99]))

pareteEntrataAlta = T([1,2])([10,5.22])(CUBOID([2.07,3]))
pareteEntrataBassa = T([1,2])([10,10.21])(CUBOID([2.07,3]))

pareti = SKELETON(1)(STRUCT([parete1,parete2,pareteTrasv,pareteEntrataAlta,pareteEntrataBassa]))

VIEW(STRUCT([pareti,piattaforma,plinti,colonne]))

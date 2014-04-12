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

def semicirc(r):
    def sphere1(p): return [r*COS(p[0]), r*SIN(p[0])]
    def domain(n): return INTERVALS(PI)(n)
    return ( MAP(sphere1)(domain(32)) )

s = T([1,2])([1,6])(semicirc(1))
p = CUBOID([2,6])

arco = PROD([JOIN([s,p]),Q(1)])
arco = MAP([S3,S1,S2])(arco)
arco = T([1,2,3])([30.5,8.22,1.6])(arco)

pareti = T(3)(1.6)(PROD([pareti,Q(7)]))
pareti = COLOR([0.545,0.27,0])(DIFFERENCE([pareti,arco]))

plinti = COLOR([0.72,0.5,0.3]) ( T(3)(1.6)(PROD([plinti,Q(0.8)])) )
colonne = COLOR([0.98,0.941,0.902]) (T(3)(2.4)(PROD([colonne,Q(7)])) )
travi = COLOR([0.72,0.5,0.3])( T(3)(9.4)(PROD([travi,Q(1.2)])) )
secondeTravi = COLOR([1,0.8,0])( T(3)(10.6)(PROD([secondeTravi,Q(1.2)])) )
tettoy1 = T(3)(11.8)(tettoy1)
tettoy2 = T(3)(11.8)(tettoy2)
tetti = COLOR([0.545,0.27,0])(STRUCT([tettoy1,tettoy2]))

tempio_Agrigento = STRUCT([pareti,piattaforma,plinti,colonne,travi,secondeTravi,tetti])

tempio_Agrigento = T([1,2])([75,55])(tempio_Agrigento)




palazzo_piccolo = COLOR([0.8,0.5,0.2])(CUBOID([5,8,12]))

finestra1 = COLOR([0,0,1])(CUBOID([0,1.5,1.5]))
finestre_destra = T([2,3])([1,4])( STRUCT([finestra1,T(3)(2.5)]*3) )
finestre_sinistra = T(2)(4.5)(finestre_destra)
finestre_davanti = STRUCT([finestre_sinistra,finestre_destra])
finestre_dietro = T(1)(5)(finestre_davanti)

finestra2 = COLOR([0,0,1])(CUBOID([1.5,0,1.5]))
finestre2_destra = T([1,3])([0.5,4])( STRUCT([finestra2,T(3)(2.5)]*3) )
finestre2_sinistra = T(1)(2.5)(finestre2_destra)
finestre2_davanti = STRUCT([finestre2_sinistra,finestre2_destra])
finestre2_dietro = T(2)(8)(finestre2_davanti)

finestre = STRUCT([finestre_davanti,finestre_dietro,finestre2_davanti,finestre2_dietro])

porta = T(2)(3) ( COLOR([0.6,0.2,0])( CUBOID([0,2,3])) )

palazzo1 = STRUCT([palazzo_piccolo,finestre,porta])


palazzo_grande = COLOR([0.8,0.5,0.2])(CUBOID([3,8,18]))

finestreP2_destra = T([2,3])([1,4])( STRUCT([finestra1,T(3)(2.5)]*5) )
finestreP2_sinistra = T(2)(4.5)(finestreP2_destra)
finestreP2_davanti = STRUCT([finestreP2_sinistra,finestreP2_destra])
finestreP2_dietro = T(1)(3)(finestreP2_davanti)

finestre2P2_davanti = T([1,3])([0.75,4])( STRUCT([finestra2,T(3)(2.5)]*5) )
finestre2P2_dietro = T(2)(8)(finestre2P2_davanti)

finestreP2 = STRUCT([finestreP2_davanti,finestreP2_dietro,finestre2P2_davanti,finestre2P2_dietro])

palazzo2 = STRUCT([palazzo_grande,finestreP2,porta])


palazzo3 = T([1,2])([15,21])(palazzo1)
palazzo4 = T(1)(15)(palazzo2)

palazzo1 = R([1,2])(PI)(palazzo1)
palazzo1 = T([1,2])([5,8])(palazzo1)

palazzo2 = R([1,2])(PI)(palazzo2)
palazzo2 = T([1,2])([3,29])(palazzo2)


stradaOriz = T(2)(12)(CUBOID([97,3]))
stradaVert = T(1)(9)(CUBOID([3,60])) 
stradaOriz2 = T([1,2])([97,12])(CUBOID([3,10]))
stradaOriz3 = T([1,2])([97,32])(CUBOID([3,10]))

strade = COLOR([0.502,0.502,0.502]) (STRUCT([stradaOriz,stradaOriz2,stradaOriz3,stradaVert]))



chiesaFaccia1 = CUBOID([7,0,10])
tetto1 = STRUCT( AA(MK)([[3.5,0,15],[0,0,10],[7,0,10]]) )

chiesaFaccia2 = CUBOID([7,20,10])
tetto2 = STRUCT( AA(MK)([[3.5,20,15],[0,20,10],[7,20,10]]) )

base = JOIN([chiesaFaccia1,chiesaFaccia2])
tetto = COLOR(RED)(JOIN([tetto2,tetto1]))

cerchio = R([2,3])(PI/2)(CIRCLE(1)([64,1]))
cerchio = COLOR(BLUE)(T([1,3])([3.5,8])(cerchio))

portone = COLOR([0.6,0.2,0])( T(1)(2)(CUBOID([3,0,5])))

finetraGrande1 =  T([2,3])([3,2]) (STRUCT([CUBOID([0,3,6]),T(2)(6)]*3))
finetraGrande2 =  T(1)(7) (finetraGrande1)
finestraRetro = COLOR([0,0,1])(T([1,2,3])([2.5,20,7])(CUBOID([2,0,2])))
finestreChiesa = STRUCT([finetraGrande1,finetraGrande2,finestraRetro])

chiesa = STRUCT([base,tetto,cerchio,portone,finestreChiesa])
chiesa = R([1,2])(-PI/2)(chiesa)
chiesa = T(1)(60)(chiesa)



citta = STRUCT([palazzo1,palazzo2,palazzo3,palazzo4,strade,chiesa,tempio_Agrigento])




tronco1 = COLOR([0.396,0.263,0.129])(CYLINDER([0.4,3])(50))
foglie1 = COLOR([0.33,0.408,0.196])(T(3)(2.9)(SPHERE(1)([60,60])))

albero1 = T([1,2])([55,60])(STRUCT([tronco1,foglie1]))
alberiSchiera1 = STRUCT([albero1,T(1)(2.5)]*5)
alberiSchiera1 = STRUCT([alberiSchiera1,T(2)(-4.5)]*7)

tronco2 = COLOR([0.396,0.263,0.129])(CYLINDER([0.2,2])(50))
cerchio = T(3)(1.9)(JOIN( AA(MK)(CIRCLE_POINTS(1,36)) ))
punto = T(3)(5)(MK([0,0,0.8]))
foglie2 = COLOR([0.4,1,0])(JOIN([cerchio,punto]))

albero2 = T([1,2])([51,29])(STRUCT([tronco2,foglie2]))
alberiSchiera21 = STRUCT([albero2,T(2)(4)]*5)
alberiSchiera22 = STRUCT([albero2,T(1)(3.5)]*13)

alberi = STRUCT([alberiSchiera1,alberiSchiera21,alberiSchiera22])

roccia = COLOR([0.309,0.309,0.309])( T([1,2])([45,50])(CUBOID([7,15,7])) )

fiume = T([1,2,3])([47.5,50,7])(CUBOID([2,15,0])) 
cascata = T([1,2])([47.5,50])(CUBOID([2,0,7])) 
fiume2 = T([1,2])([47.5,26])(CUBOID([2,24,0])) 
fiume3 = T([1,2])([49,26])(CUBOID([54,2,0])) 

fiume = COLOR([0,0.5,1])( STRUCT([fiume,cascata,fiume2,fiume3]) )

c = AA(MK)(CIRCLE_POINTS(15,50))
lago = COLOR([0,0.5,1])( T([1,2])([118,28])(JOIN(c)) )


piede1Panchina = T([1,2])([1,1])(CUBOID([2,4,3]))
piede2Panchina = T([1,2])([9,1])(CUBOID([2,4,3]))
basePanchina = T(3)(3)(CUBOID([12,6,1]))
schienalePanchina = R([2,3])(-PI/7)(CUBOID([12,1,5]))
schienalePanchina = T([2,3])([5,4])(schienalePanchina)

panchina = COLOR([0.8,0.8,0.8])(STRUCT([piede1Panchina,piede2Panchina,basePanchina,schienalePanchina]))
panchina = S([1,2,3])([0.15,0.15,0.15])(panchina)
panchina = R([1,2])(PI)(panchina)
panchina = T([1,2])([53,25])(panchina)

panchine = STRUCT([panchina,T(1)(9.5)]*5)


asta = CYLINDER([0.1,4])(50)
astaObl = CYLINDER([0.1,1])(50)
astaObl = R([1,3])(PI/6)(astaObl)
astaObl = T(3)(3.7)(astaObl)
pezzoLuce = T([1,2,3])([-1.1,-0.1,4.4])(CUBOID([0.7,0.2,0.2]))
lampadina = COLOR(YELLOW)( T([1,2,3])([-1.05,-0.07,4.39])(CUBOID([0.5,0.15,0.01])) )

lampione = COLOR([0.8,0.8,1])(STRUCT([asta,astaObl,pezzoLuce,lampadina]))
lampioniD = T([1,2])([13,22])( STRUCT([lampione,T(2)(6.5)]*6))

lampione = R([1,2])(PI)(lampione)
lampioniS = T([1,2])([7.5,22])( STRUCT([lampione,T(2)(6.5)]*6))

lampioni = STRUCT([lampioniD,lampioniS])


piolo = COLOR([0.3,0.3,0.3])(CYLINDER([0.1,1.1])(50))
luce = COLOR([1,0.85,0])(T(3)(1)(SPHERE(0.25)([60,60])))
lampioncino = T([1,2])([55,25])(STRUCT([piolo,luce]))
lampioncini = STRUCT([lampioncino,T(1)(9.5)]*5)


ponte = R([2,3])(PI/2)(semicirc(5))
ponte = R([1,2])(-PI/2)(ponte)
ponte = T([1,2])([97,27])(ponte)
ponte = JOIN([ponte,(T(1)(3)(ponte))])
ponte = DIFFERENCE([ponte,(T(3)(-0.1)(ponte))])
ponte = COLOR([0.502,0.502,0.502]) (ponte)


esterno = STRUCT([alberi,roccia,fiume,lago,panchine,lampioncini,lampioni,ponte])

VIEW(STRUCT([citta,esterno]))

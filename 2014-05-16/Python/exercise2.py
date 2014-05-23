from larcc import *
from exercise3 import *

DRAW = COMP([VIEW,STRUCT,MKPOLS])

def colorRGB (r,g,b) :
    r = (float(r)/255)
    g = (float(g)/255)
    b = (float(b)/255)
    return COLOR([r,g,b])

def ruotaSuz (points,a):
    return [[x*COS(a)-y*SIN(a), x*SIN(a)+y*COS(a),z] for x,y,z in points]

def trasparenza(x):
    return MATERIAL([1,1,1,0.1, 0,0,0.8,0.5, 1,1,1,0.1, 1,1,1,0.1, 100])(x)

master = assemblyDiagramInit([11,9,2])([[.3,4,.1,4.5,.1,3,.1,5,.1,4,.3],
                                        [.3,1.5,.1,0.5,.1,2,0.1,3,.3],[.3,2.7]])
V,CV = master

toRemoveTetto = [21,29,33,57,65,69,93,101,105,129,137,141,165,173,177]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemoveTetto)]

toRemoveMuriOriz = [29,22,24,55,57,59,62,90,92,95,121,123,125,156,158]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemoveMuriOriz)]

toRemoveMuriVert = [33,35,37,62,92,126,128,130,134]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemoveMuriVert)]


master,porta1 = mnePortaOFinestra(master,[3,1,2],[[1.5,1,1.5],[.3],[2,.7]],132) #per fare porta
master,finestra1 = mnePortaOFinestra(master,[4,1,3],[[3,.9,.2,.9],[.3],[1,1.4,.3]],113) #per fare finestra
master,porta2 = mnePortaOFinestra(master,[3,1,2],[[3.8,1,0.2],[.3],[2,.7]],110) #per fare porta
master,finestra2 = mnePortaOFinestra(master,[5,1,3],[[.5,.9,.2,.9,.5],[.3],[.4,2,.3]],84) #per fare finestra
master,finestra3 = mnePortaOFinestra(master,[3,1,3],[[1.3,1.9,1.3],[.3],[1,1.4,.3]],55) #per fare finestra
master,porta3 = mnePortaOFinestra(master,[3,1,2],[[1,1,2.5],[.3],[2,.7]],46) #per fare porta
master,porta4 = mnePortaOFinestra(master,[3,1,2],[[1.5,1,1.5],[.3],[2,.7]],24) #per fare porta

master,porta5 = mnePortaOFinestra(master,[1,3,2],[[.3],[.5,1,.5],[2,.7]],63) #per fare porta


#appartamento situato a NordOvest del palazzo
appartamentoNO = master
appartamentoNO,finestra4 = mnePortaOFinestra(appartamentoNO,[1,5,3],[[.3],[.5,.9,.2,.9,.5],[1,1.4,.3]],15) #per fare finestra

porte = COLOR([0.545,0.27,0])(STRUCT([porta1,porta2,porta3,porta4,porta5]))
finestre = COLOR([0,0.5,1])(STRUCT([finestra1,finestra2,finestra3,finestra4]))
pal = (STRUCT(MKPOLS(master)))
VIEW(STRUCT([pal,porte,finestre]))

#appartamento situato a SudEst del palazzo
V1,CV1 = appartamentoNO
V1 = ruotaSuz(V1, PI)
appartamentoSE = V1,CV1
#appartamento situato a NordEst del palazzo
appartamentoNE = master
appartamentoNE = mne(appartamentoNE,[1,3,3],[[.3],[.6,.9,.5],[1,1.4,.3]],144) #per fare finestra
#appartamento situato a SudOvest del palazzo
V1,CV1 = appartamentoNE
V1 = ruotaSuz(V1, PI)
appartamentoSO = V1,CV1



appartamento = master
palazzo = assemblyDiagramInit([2,3,7])([[21.5,21.5],[7.9,4.5,7.9],[3,.3,3,.3,3,.3,3]])
V,CV = palazzo

palazzo = diagram2cell(appartamentoNE,palazzo,41)
palazzo = diagram2cell(appartamentoNE,palazzo,39)
palazzo = diagram2cell(appartamentoNE,palazzo,37)
palazzo = diagram2cell(appartamentoSE,palazzo,27)
palazzo = diagram2cell(appartamentoSE,palazzo,25)
palazzo = diagram2cell(appartamentoSE,palazzo,23)
palazzo = diagram2cell(appartamentoNO,palazzo,20)
palazzo = diagram2cell(appartamentoNO,palazzo,18)
palazzo = diagram2cell(appartamentoNO,palazzo,16)
palazzo = diagram2cell(appartamentoSO,palazzo,6)
palazzo = diagram2cell(appartamentoSO,palazzo,4)
palazzo = diagram2cell(appartamentoSO,palazzo,2)

DRAW(palazzo)

toRemoveCorridoio = [25,10]
palazzo = palazzo[0], [cell for k,cell in enumerate(palazzo[1]) if not (k in toRemoveCorridoio)]
DRAW(palazzo)

palazzo = mne(palazzo,[3,3,1],[[.5,4,17],[.45,7,.45],[.3]],23) #per fare buco per scale
palazzo = mne(palazzo,[3,3,1],[[.5,4,17],[.45,7,.45],[.3]],21) #per fare buco per scale
palazzo = mne(palazzo,[3,3,1],[[.5,4,17],[.45,7,.45],[.3]],19) #per fare buco per scale
palazzo = mne(palazzo,[3,3,1],[[17,4,.5],[.45,7,.45],[.3]],9) #per fare buco per scale
palazzo = mne(palazzo,[3,3,1],[[17,4,.5],[.45,7,.45],[.3]],7) #per fare buco per scale
palazzo = mne(palazzo,[3,3,1],[[17,4,.5],[.45,7,.45],[.3]],5) #per fare buco per scale
'''
hpc = SKEL_1(STRUCT(MKPOLS(palazzo)))
hpc = cellNumbering (palazzo,hpc)(range(len(palazzo[1])),CYAN,2)
VIEW(hpc)
'''
toRemovePareti = [17,16,6,5]
palazzo = palazzo[0], [cell for k,cell in enumerate(palazzo[1]) if not (k in toRemovePareti)]

pal = COLOR([0.545,0.27,0])(STRUCT(MKPOLS(palazzo)))
VIEW(pal)

W,CW = spiralStair(0.6,2.1,0.6,0.2,3.8,5,18)
scale1 = COLOR([1,0.8,0]) (T([1,2])([19,10])(STRUCT(MKPOLS([W,CW]))))
W1 = ruotaSuz (W, 7*PI/6)
scale2 = COLOR([1,0.8,0]) (T([1,2])([24,10])(STRUCT(MKPOLS([W1,CW]))))
VIEW(STRUCT([pal,scale1,scale2]))


dom1D = INTERVALS(1)(32)
dom2D = PROD([dom1D,dom1D])

tavolo = COLOR([0.8,0.5,0.2])(T([1,2])([4,5]) (CUBOID([2,.5,1])))

controls1a = [[.5,4,0],[1,3,0],[4,2.2,0],[7,3,0],[7.5,4,0]]
bezier1a = BEZIER(S1)(controls1a)
controls1b = [[.5,4,1],[1,3,1],[4,2.2,1],[7,3,1],[7.5,4,1]]
bezier1b = BEZIER(S1)(controls1b)

controls2a = [[.5,4,0],[1,2,0],[4,1.2,0],[7,2,0],[7.5,4,0]]
bezier2a = BEZIER(S1)(controls2a)
controls2b = [[.5,4,1],[1,2,1],[4,1.2,1],[7,2,1],[7.5,4,1]]
bezier2b = BEZIER(S1)(controls2b)


bezier1 = MAP( BEZIER(S2)([bezier1a,bezier1b]))(dom2D)
bezier2 = MAP( BEZIER(S2)([bezier2a,bezier2b]))(dom2D)
bezier3 = MAP( BEZIER(S2)([bezier1a,bezier2a]))(dom2D)
bezier4 = MAP( BEZIER(S2)([bezier1b,bezier2b]))(dom2D)

curve = COLOR([0,0.5,1])( T([1,2])([1,1]) (STRUCT([bezier1,bezier2,bezier3,bezier4])))
portineria = T([1,2])([11,7])(R([1,2])(PI)(S([1,2,3])([.8,.8,.8])(STRUCT([tavolo,curve]))))
VIEW(portineria)
''' curve non piu' mostrate
print("attendere ...")

controls1a = [[1,5,0],[2,5.5,0],[3,3,0],[4.5,2,0],[6,3,0],[7,5.5,0],[8,5.5,0],[9,3,0],[10.5,2,0],[12,3,0],[13,5.5,0],[14,5,0]]
bezier1a = BEZIER(S1)(controls1a)

controls1b = [[1,5,.2],[2,5.5,.2],[3,3,.2],[4.5,2,.2],[6,3,.2],[7,5.5,.2],[8,5.5,.2],[9,3,.2],[10.5,2,.2],[12,3,.2],[13,5.5,.2],[14,5,.2]]
bezier1b = BEZIER(S1)(controls1b)

controls2a = [[1,4,0],[2,4.5,0],[3,2,0],[4.5,1,0],[6,2,0],[7,4.5,0],[8,4.5,0],[9,2,0],[10.5,1,0],[12,2,0],[13,4.5,0],[14,4,0]]
bezier2a = BEZIER(S1)(controls2a)

controls2b = [[1,4,.2],[2,4.5,.2],[3,2,.2],[4.5,1,.2],[6,2,.2],[7,4.5,.2],[8,4.5,.2],[9,2,.2],[10.5,1,.2],[12,2,.2],[13,4.5,.2],[14,4,.2]]
bezier2b = BEZIER(S1)(controls2b)

bezier1 = MAP( BEZIER(S2)([bezier1a,bezier1b]))(dom2D)
bezier2 = MAP( BEZIER(S2)([bezier2a,bezier2b]))(dom2D)
bezier3 = MAP( BEZIER(S2)([bezier1a,bezier2a]))(dom2D)
bezier4 = MAP( BEZIER(S2)([bezier1b,bezier2b]))(dom2D)

curve2 = T([1,2])([10,1]) (STRUCT([bezier1,bezier2,bezier3,bezier4]))
VIEW(curve2)


controls1a = [[5,0,0],[1,1.5,0],[9,3,0],[1,4.5,0],[5,6,0]]
bezier1a = BEZIER(S1)(controls1a)
controls1b = [[5,0,2],[1,1.5,2],[9,3,2],[1,4.5,2],[5,6,2]]
bezier1b = BEZIER(S1)(controls1b)

controls2a = [[5,0,0],[9,1.5,0],[1,3,0],[9,4.5,0],[5,6,0]]
bezier2a = BEZIER(S1)(controls2a)
controls2b = [[5,0,2],[9,1.5,2],[1,3,2],[9,4.5,2],[5,6,2]]
bezier2b = BEZIER(S1)(controls2b)

bezier1 = MAP( BEZIER(S2)([bezier1a,bezier1b]))(dom2D)
bezier2 = MAP( BEZIER(S2)([bezier2a,bezier2b]))(dom2D)
bezier3 = MAP( BEZIER(S2)([bezier1a,bezier2a]))(dom2D)
bezier4 = MAP( BEZIER(S2)([bezier1b,bezier2b]))(dom2D)

curve3 = COLOR([0.5,1,0])( T([1,2])([24,7]) (STRUCT([bezier1,bezier2,bezier3,bezier4])))
VIEW(STRUCT([curve3]))
VIEW(STRUCT([tavolo,curve,curve2,curve3]))
'''

vasoSotto = CYLINDER([1,2])(80)
vasoSopra = T(3)(2)(CYLINDER([1.2,0.4])(80))
vaso = colorRGB(205,151,95)(STRUCT([vasoSotto,vasoSopra]))
terra = T(3)(2)(CYLINDER([1.08,0.41])(50))
terra = colorRGB(83,27,0)(terra)
vaso = STRUCT([vaso,terra])

tronco = colorRGB(113,56,0)(T(3)(2)(CYLINDER([.2,3.7])(100)))
linea1 = colorRGB(83,27,0)(T(3)(2.2)(CYLINDER([.201,.05])(80)))
linee = STRUCT (NN (7) ([linea1, T (3) (.5) ]))
linea2 = colorRGB(83,27,0)(T(3)(2.45)(CYLINDER([.201,.05])(80)))
linee2 = STRUCT (NN (6) ([linea2, T (3) (.63) ]))
linea3 = colorRGB(83,27,0)(T(3)(2.65)(CYLINDER([.201,.05])(80)))
linea4 = colorRGB(83,27,0)(T(3)(4)(CYLINDER([.201,.05])(80)))
linea5 = colorRGB(83,27,0)(T(3)(2.9)(CYLINDER([.201,.05])(80)))
linea6 = colorRGB(83,27,0)(T(3)(3.2)(CYLINDER([.201,.05])(80)))
linea7 = colorRGB(83,27,0)(T(3)(3.35)(CYLINDER([.201,.05])(80)))
linea8 = colorRGB(83,27,0)(T(3)(3.4)(CYLINDER([.201,.05])(80)))
linea9 = colorRGB(83,27,0)(T(3)(3.55)(CYLINDER([.201,.05])(80)))
tronco = STRUCT([tronco,linee,linee2,linea1,linea2,linea3,linea4,linea5,linea6,linea7,linea8,linea9])

controls1a = [[0,0,0], [-1,-1,-.35], [-2,-2,-.45], [-2.8,-3,-.75]]
bezier1a = BEZIER(S1)(controls1a)
controls1b = [[-.85,.1,0], [-1.85,-.9,-.35], [-2.5,-2.2,-.45], [-2.8,-3,-.75]]
bezier1b = BEZIER(S1)(controls1b)
bezier1 = MAP( BEZIER(S2)([bezier1a,bezier1b]))(dom2D)
foglia = colorRGB(34,139,34)(bezier1)

f2 = R([1,2])(PI/6)(foglia)
f3 = R([1,2])(PI/6)(f2)
f4 = R([1,2])(PI/6)(f3)
f5 = R([1,2])(PI/6)(f4)
f6 = R([1,2])(PI/6)(f5)
f7 = R([1,2])(PI/6)(f6)
f8 = R([1,2])(PI/6)(f7)
f9 = R([1,2])(PI/6)(f8)
f10 = R([1,2])(PI/6)(f9)
f11 = R([1,2])(PI/6)(f10)
f12 = R([1,2])(PI/6)(f11)


controls1a = [[0,0,0], [-1,-1,.15], [-2,-2,.25], [-2.8,-3,.55]]
bezier1a = BEZIER(S1)(controls1a)
controls1b = [[-.85,.1,0], [-1.85,-.9,.15], [-2.5,-2.2,.25], [-2.8,-3,.55]]
bezier1b = BEZIER(S1)(controls1b)
bezier1 = MAP( BEZIER(S2)([bezier1a,bezier1b]))(dom2D)
foglia2 = colorRGB(34,139,34)(bezier1)

ff2 = R([1,2])(PI/4)(foglia2)
ff3 = R([1,2])(PI/3)(ff2)
ff4 = R([1,2])(PI/3)(ff3)
ff5 = R([1,2])(PI/3)(ff4)
ff6 = R([1,2])(PI/3)(ff5)
ff7 = R([1,2])(PI/3)(ff6)

foglie = T(3)(5.7)(STRUCT([foglia,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,ff2,ff3,ff4,ff5,ff6,ff7]))

pianta = STRUCT([vaso,tronco,foglie]) 
VIEW(pianta)
pianta = T([1,2])([2,8])(S([1,2,3])([.3,.3,.3])(pianta))
pianta2 = T(2)(4.3)(pianta)
piante = STRUCT([pianta,pianta2])

tappeto = T(2)(8.5)(colorRGB(128,0,0)(CUBOID([20,3.3])))

vetrata = CUBOID([0.1,6.5,3])
porta = T(2)(2.75)(CUBOID([0.1,1,2]))
vetrata = T([1,2])([16,6.9])(trasparenza(DIFFERENCE([vetrata,porta])))

ingresso = STRUCT([piante,tappeto,vetrata,portineria])
print("attendere ...")
VIEW(ingresso)


toRemoveParete = [5,4,0]
palazzo = palazzo[0], [cell for k,cell in enumerate(palazzo[1]) if not (k in toRemoveParete)]

pal = COLOR([0.545,0.27,0])(STRUCT(MKPOLS(palazzo)))
print("attendere ...")
VIEW(STRUCT([pal,scale1,scale2,ingresso]))

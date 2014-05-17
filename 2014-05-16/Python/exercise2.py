from larcc import *
from exercise3 import *

DRAW = COMP([VIEW,STRUCT,MKPOLS])

master = assemblyDiagramInit([11,9,2])([[.3,4,.1,4.5,.1,3,.1,5,.1,4,.3],
                                        [.3,1.5,.1,0.5,.1,2,0.1,3,.3],[.3,2.7]])
V,CV = master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)

toRemoveTetto = [21,29,33,57,65,69,93,101,105,129,137,141,165,173,177]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemoveTetto)]

toRemoveMuriOriz = [29,22,24,55,57,59,62,90,92,95,121,123,125,156,158]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemoveMuriOriz)]

toRemoveMuriVert = [33,35,37,62,92,126,128,130,134]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemoveMuriVert)]

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

master = mne(master,[3,1,2],[[1.5,1,1.5],[.3],[2,.7]],132) #per fare porta
master = mne(master,[4,1,3],[[3,.9,.2,.9],[.3],[1,1.4,.3]],113) #per fare finestra
master = mne(master,[3,1,2],[[2.9,1,0.1],[.3],[2,.7]],110) #per fare porta
master = mne(master,[5,1,3],[[.5,.9,.2,.9,.5],[.3],[.4,2,.3]],84) #per fare finestra
master = mne(master,[3,1,3],[[1.3,1.9,1.3],[.3],[1,1.4,.3]],55) #per fare finestra
master = mne(master,[3,1,2],[[1,1,2.5],[.3],[2,.7]],46) #per fare porta
master = mne(master,[3,1,2],[[1.5,1,1.5],[.3],[2,.7]],24) #per fare porta

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
#DRAW(master)


master = mne(master,[1,3,2],[[.3],[.5,1,.5],[2,.7]],63) #per fare porta
master = mne(master,[1,5,3],[[.3],[.5,.9,.2,.9,.5],[1,1.4,.3]],15) #per fare finestra
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
VIEW(hpc)
DRAW(master)




appartamento = master
palazzo = assemblyDiagramInit([2,4,4])([[21.5,21.5],[2.5,7.9,4.5,7.9],[3,3,3,3]])
V,CV = palazzo
hpc = SKEL_1(STRUCT(MKPOLS(palazzo)))
hpc = cellNumbering (palazzo,hpc)(range(len(CV)),CYAN,2)
#VIEW(hpc)
#DRAW(palazzo)

palazzo = diagram2cell(appartamento,palazzo,5)
palazzo = diagram2cell(appartamento,palazzo,5)
palazzo = diagram2cell(appartamento,palazzo,5)
palazzo = diagram2cell(appartamento,palazzo,10)
palazzo = diagram2cell(appartamento,palazzo,10)
palazzo = diagram2cell(appartamento,palazzo,10)
palazzo = diagram2cell(appartamento,palazzo,15)
palazzo = diagram2cell(appartamento,palazzo,15)
palazzo = diagram2cell(appartamento,palazzo,15)
palazzo = diagram2cell(appartamento,palazzo,20)
palazzo = diagram2cell(appartamento,palazzo,20)
palazzo = diagram2cell(appartamento,palazzo,20)

hpc = SKEL_1(STRUCT(MKPOLS(palazzo)))
hpc = cellNumbering (palazzo,hpc)(range(len(CV)),CYAN,2)
VIEW(hpc)
DRAW(palazzo)

toRemoveCorridoio = [0,1,2,3,5,6,7,8,10,11,12,13,15,16,17,18]
palazzo = palazzo[0], [cell for k,cell in enumerate(palazzo[1]) if not (k in toRemoveCorridoio)]

#DRAW(palazzo)


V = [[0,0],[0,22.8],[43,22.8],[43,0]]
FV = [[0,1,2,3,0]]
modelFaces = V,FV
V0 = AA(LIST)([0.3,3.3,6.3,9.3])
C0V = AA(LIST)(range(4))
modelFloor = V0,C0V

mod1D = larModelProduct([modelFaces,modelFloor])
mod1D = COLOR([1,0.8,0]) (STRUCT(MKPOLS(mod1D)))

VIEW(STRUCT([mod1D,hpc]))
pal = COLOR([0.545,0.27,0])(STRUCT(MKPOLS(palazzo)))
VIEW(STRUCT([mod1D,pal]))

def spiralStair(width=0.2,R=1.,r=0.5,riser=0.1,pitch=2.,nturns=2.,steps=18):
   V,CV = larSolidHelicoid(width,R,r,pitch,nturns,steps)()
   W = CAT([[V[k],V[k+1],V[k+2],V[k+3]]+
      [SUM([V[k+1],[0,0,-riser]]),SUM([V[k+3],[0,0,-riser]])]
      for k,v in enumerate(V[:-4]) if k%4==0])
   for k,w in enumerate(W[:-12]):
      if k%6==0: W[k+1][2] = W[k+10][2]; W[k+3][2] = W[k+11][2]
   nsteps = len(W)/12
   CW =[SUM([[0,1,2,3,6,8,10,11],[6*k]*8]) for k in range(nsteps)]
   return W,CW

W,CW = spiralStair(0.6,2.1,0.6,0.2,3.8,5,18)

def ruotaSuz (points,a):
    return [[x*COS(a)-y*SIN(a), x*SIN(a)+y*COS(a),z] for x,y,z in points]

W = ruotaSuz (W, PI/4)
scale = T([1,2])([27.5,12.4])(STRUCT(MKPOLS([W,CW])))
VIEW(STRUCT([mod1D,pal,scale]))



print("attendere ...")
dom1D = INTERVALS(1)(32)
dom2D = PROD([dom1D,dom1D])

tavolo = COLOR([0.8,0.5,0.2])(T([1,2])([4,5]) (CUBOID([2,.5,1])))

controls1a = [[.5,4,0],[0,1.8,0],[2,1,0],[4,.5,0],[7,1.8,0],[7.5,3,0],[7,4,0]]
bezier1a = BEZIER(S1)(controls1a)
#VIEW(bezier1a)

controls1b = [[.5,4,1],[0,1.8,1],[2,1,1],[4,.5,1],[7,1.8,1],[7.5,3,1],[7,4,1]]
bezier1b = BEZIER(S1)(controls1b)
#VIEW(bezier1b)


controls2a = [[.5,4,0],[1.5,2,0],[2,2.5,0],[4,2,0],[6,2.5,0],[6.2,3.2,0],[7,4,0]]
bezier2a = BEZIER(S1)(controls2a)
#VIEW(bezier2a)

controls2b = [[.5,4,1],[1.5,2,1],[2,2.5,1],[4,2,1],[6,2.5,1],[6.2,3.2,1],[7,4,1]]
bezier2b = BEZIER(S1)(controls2b)
#VIEW(bezier2b)


bezier1 = MAP( BEZIER(S2)([bezier1a,bezier1b]))(dom2D)
bezier2 = MAP( BEZIER(S2)([bezier2a,bezier2b]))(dom2D)
bezier3 = MAP( BEZIER(S2)([bezier1a,bezier2a]))(dom2D)
bezier4 = MAP( BEZIER(S2)([bezier1b,bezier2b]))(dom2D)

curve = COLOR([0,0.5,1])( T([1,2])([1,1]) (STRUCT([bezier1,bezier2,bezier3,bezier4])))
VIEW(STRUCT([tavolo,curve]))

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
VIEW(STRUCT([tavolo,curve,curve2,hpc]))

toRemoveParete = [2,0]
palazzo = palazzo[0], [cell for k,cell in enumerate(palazzo[1]) if not (k in toRemoveParete)]


pal = COLOR([0.545,0.27,0])(STRUCT(MKPOLS(palazzo)))
VIEW(STRUCT([tavolo,curve,curve2,pal]))


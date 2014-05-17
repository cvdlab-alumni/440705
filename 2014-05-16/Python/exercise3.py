from larcc import *

DRAW = COMP([VIEW,STRUCT,MKPOLS])
'''
master = assemblyDiagramInit([11,9,2])([[.3,4,.1,4.5,.1,3,.1,5,.1,4,.3],
                                        [.3,1.5,.1,0.5,.1,2,0.1,3,.3],[.3,2.7]])
V,CV = master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)
#VIEW(hpc)

toRemoveTetto = [21,29,33,57,65,69,93,101,105,129,137,141,165,173,177]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemoveTetto)]
#DRAW(master)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

toRemoveMuriOriz = [29,22,24,55,57,59,62,90,92,95,121,123,125,156,158]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemoveMuriOriz)]
#DRAW(master)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

toRemoveMuriVert = [33,35,37,62,92,126,128,130,134]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemoveMuriVert)]
#DRAW(master)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
'''
'''
toMerge = 46 #per fare la porta
diagram = assemblyDiagramInit([3,1,2])([[1,1,2.5],[.3],[2,.7]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

toRemove = [160]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
'''


def mne (master,shape,sizePattern,toMerge):
    [x,y,z] = shape
    lung = len(master[1])
    diagram = assemblyDiagramInit(shape)(sizePattern)
    master = diagram2cell(diagram,master,toMerge)

    matrice = []
    
    if x == 1 :
        x = y
    for i in range (x) :
        colonna = []
        for j in range (z) :
            colonna.insert(j,lung-1)
            lung += 1
        matrice.insert(i,colonna)
    
    ii = [1]
    numElem = x/2
    while(numElem > 1):
        a = 0
        ii.append(ii[a] + 2)
        a += 1
        numElem -= 1

    if z%2 == 0 :
        jj = [0]
    else:
        jj = [1]
        
    numElem = z/2
    while(numElem > 1):
        a = 0
        jj.append(jj[a] + 2)
        a += 1
        numElem -= 1


    toRemove = [];
    for i in range (len(ii)) :
        for j in range (len(jj)) :
            toRemove.append(matrice[ii[i]][jj[j]])

    master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
    
    return master



'''
master = mne(master,[3,1,2],[[1,1,2.5],[.3],[2,.7]],46)
DRAW(master)
master = mne(master,[4,1,3],[[3,0.9,.2,.9],[.3],[1,1.4,.3]],112)
DRAW(master)
'''

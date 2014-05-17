from larcc import *

DRAW = COMP([VIEW,STRUCT,MKPOLS])

master = assemblyDiagramInit([11,9,2])([[.3,4,.1,4.5,.1,3,.1,5,.1,4,.3],
                                        [.3,1.5,.1,0.5,.1,2,0.1,3,.3],[.3,2.7]])
V,CV = master

toRemoveTetto = [21,29,33,57,65,69,93,101,105,129,137,141,165,173,177]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemoveTetto)]

toRemoveMuriOriz = [29,22,24,55,57,59,62,90,92,95,121,123,125,156,158]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemoveMuriOriz)]

toRemoveMuriVert = [33,35,37,62,92,126,128,130,134]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemoveMuriVert)]

toMerge = 46 #per fare la porta
diagram = assemblyDiagramInit([3,1,2])([[1,1,2.5],[.3],[2,.7]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
VIEW(hpc)

toRemove = [160]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]

toMerge = 112 #per fare finestre
diagram = assemblyDiagramInit([4,1,3])([[3,0.9,.2,.9],[.3],[1,1.4,.3]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
VIEW(hpc)

toRemove = [166,172]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
DRAW(master)

from larcc import *

def daListaDiListeALista (listaDiListe) :
    lista = []
    for i in range (len(listaDiListe)) :
        for j in range (len(listaDiListe[i])) :
            lista.append(listaDiListe[i][j])
    return lista

def mne (master,shape,sizePattern,toMerge):
    [x,y,z] = shape
    lung = len(master[1])
    diagram = assemblyDiagramInit(shape)(sizePattern)
    master = diagram2cell(diagram,master,toMerge)

    matrice = []
    
    if x == 1 :
        x = y
    elif z == 1:
        z = y
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


def mnePortaOFinestra (master,shape,sizePattern,toMerge):
    [x,y,z] = shape
    lung = len(master[1])
    diagram = assemblyDiagramInit(shape)(sizePattern)
    master = diagram2cell(diagram,master,toMerge)

    matrice = []
    
    if x == 1 :
        x = y
    elif z == 1:
        z = y
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


    #qui ci sono le modifiche per ritornare i punti della/delle porta/e e finestra/e
    V,CV = master
    if (len(toRemove) != 0) :
        puntiDaEliminare = []
        posPuntiDaEliminare = []
        posPuntiDaEliminare.append(CV[toRemove[0]])
        posPuntiDaEliminare = daListaDiListeALista(posPuntiDaEliminare)
        for p in range (len(posPuntiDaEliminare)) :
            puntiDaEliminare.append(V[posPuntiDaEliminare[p]])
        punti = AA(MK)(puntiDaEliminare)
        portaOFinestra = (JOIN(punti))

    for k in range (1,len(toRemove)) :
        puntiDaEliminare = []
        posPuntiDaEliminare = []
        posPuntiDaEliminare.append(CV[toRemove[k]])
        posPuntiDaEliminare = daListaDiListeALista(posPuntiDaEliminare)
        for p in range (len(posPuntiDaEliminare)) :
            puntiDaEliminare.append(V[posPuntiDaEliminare[p]])
        punti = AA(MK)(puntiDaEliminare)
        portaOFinestra2 = (JOIN(punti))
        portaOFinestra = STRUCT([portaOFinestra,portaOFinestra2])

    #fine modifiche
    master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
    
    return master,portaOFinestra


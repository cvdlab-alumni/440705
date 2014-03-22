from pyplasm import *

gradini1 = STRUCT([CUBOID([120,25,16]),T([2,3])([25,16])]*7)
VIEW(gradini1)

pianerottolo1 = T([2,3])([175,112])(CUBOID([120,120]))

VIEW(STRUCT([pianerottolo1,gradini1]))

gradini2 = R([1,2])(PI*0.5)(gradini1)
gradini2 = T([2,3])([175,112])(gradini2)

VIEW(STRUCT([pianerottolo1,gradini1,gradini2]))



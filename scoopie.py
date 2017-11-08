import numpy as np
from itertools import product

#inputToList vraagt input aan en zet het om in een array met index.
def inputToList():
    n = 0;
    pt = []
    #eiwitInput = raw_input("voer de eiwit in: ")
    eiwitInput = "hhphhhph"

    for i in eiwitInput.upper():
        if i != 'H' and i != 'P':
            print "Het eiwit mag geen", i, "bevatten"
            return "Het eiwit mag geen", i, "bevatten"
        pt.append(i + str(n))
        n +=1

    return pt

#counterFirst berekent beginscore eiwit, +1 voor alle H's die naast elkaar staan.
def counterFirst(inputList):
    counter  = 0
    for i in range(len(inputList)-1):
        if inputList[i][0] == "H" and inputList[i+1][0] == "H":
            counter += 1
    return counter

#makeGrid maakt een Array aan de hand van de ingegeven eiwit string.
def makeGrid(inputList):
    grid = [["_"]* ((len(inputList)*2)-1) for i in (range(len(inputList*2)-1))]
    grid[7][7] = inputList[0]
    grid = np.array(grid)

    return grid

#moveAmino plaats een nieuwe aminozuur in de grad adh van opgegeven richting
def moveAmino(point, direction):
    newPoint = (0,0)

    if direction == "l":
        newPoint = (point[0], point[1]-1)
    elif direction == "r":
        newPoint = (point[0], point[1]+1)
    elif direction == "u":
        newPoint = (point[0]-1, point[1])
    elif direction == "d":
        newPoint = (point[0]+1, point[1])

    return newPoint

def bruteForce():
    print list(product(["l", "r", "u", "d"], repeat=7))


print inputToList()

print counterFirst(inputToList())

#print makeGrid(inputToList())

gridje = makeGrid(inputToList())

punt = (7,7)
for i in inputToList()[1:]:
    while True:
        richting = raw_input("welke richting")
        if richting != "l" and richting !=  "u" and richting != "r" and richting != "d":
            print 'moet input aanleveren als u,l,r of d'
        else:
            punt = moveAmino(punt, richting)
            gridje[punt[0]][punt[1]] = i
            print  gridje
            break
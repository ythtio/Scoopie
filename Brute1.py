import numpy as np
from itertools import product
import time

start_time = time.clock()

#Functie vraagt input aan en zet het om in een array met index.
def inputToList():
    n = 0;
    pt = []
    #eiwitInput = raw_input("voer de eiwit in: ")
    eiwitInput = "hhphhhph"
    #eiwitInput = "hhphhhphpphhhpp"

    for i in eiwitInput.upper():
        if i != 'H' and i != 'P':
            print "Het eiwit mag geen", i, "bevatten"
            return "Het eiwit mag geen", i, "bevatten"
        pt.append(i + str(n))
        n +=1

    return pt

#Deze functie heeft een +1 score voor elke H's die naast elkaar staan.
def counterFirst():
    counter  = 0
    for i in range(len(inputToList())-1):
        if inputToList()[i][0] == "H" and inputToList()[i+1][0] == "H":
            counter += 1
    return counter

def counterScore(grids):
    scoreGrids = []
    highScoreGrids = []
    scores = []
    for i in grids:
        score = 0
        #print i
        for j in range(len(i)-1):
            #print i[j]
            for k in range(len(i[j])-1):
                #print i[j][k], '-', i[j+1][k], '-', i[j][k+1]
                if i[j][k] != '_' and i[j][k][0] == 'H':
                    if i[j+1][k] != '_' and i[j+1][k][0] == 'H':
                        score += 1
                    if i[j][k+1] != '_' and i[j][k+1][0] == 'H':
                        score += 1

        scores.append(score - counterFirst())
        scoreGrids.append(i)

        #print 'score:', (score - counterFirst())

    for i in range(len(scores)):
        if scores[i] == max(scores):
            highScoreGrids.append(scoreGrids[i])

    print "oplossingen:", max(scores)
    return highScoreGrids


#Functie maakt een Array aan de hand van de ingegeven eiwit string.
def makeGrid(inputList):
    grid = [["_"]* ((len(inputList)*2)-1) for i in (range(len(inputList*2)-1))]
    grid[len(inputToList())-1][len(inputToList())-1] = inputList[0]
    grid = np.array(grid)

    return grid

#Deze functie plaats een nieuwe aminozuur in de grid adh van opgegeven richting
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

#Deze functie returnt een lijst met alle mogelijke vertakkingen van de verschillende richtingen.
def posibilitys():
    aminzoZuur = inputToList()
    lengthAminozuur = len(aminzoZuur)
    posibilityList  = []
    posibilityList = list(product(["l", "r", "u", "d"], repeat= lengthAminozuur-2))

    return posibilityList

#Hier worden alle mogelijkheden bekeken.
def bruteForce():
    teller = 0
    gridStart = makeGrid(inputToList())
    grids = []
    paden = posibilitys()

    for i in paden:
        gridResult =np.copy(gridStart)
        punt = (7, 7)
        punt = moveAmino(punt, "r")
        gridResult[punt[0]][punt[1]] = inputToList()[1]
        for j in range(len(i)):
            punt = moveAmino(punt, i[j])
            if gridResult[punt[0]][punt[1]] != '_':
                break
            gridResult[punt[0]][punt[1]] = inputToList()[j+2]
        if inputToList()[-7] in gridResult:
            grids.append(gridResult)
            #print gridResult

        teller += 1
    print len(grids)
    print len(paden)
    return grids


#counterScore(bruteForce())

posibilitys()
print len(posibilitys())
#print len(posibilitys())
#print len(inputToList())

#print inputToList()

#print counterFirst()

print time.clock() - start_time, "seconds"



#print makeGrid(inputToList())
'''
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
'''





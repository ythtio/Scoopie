import numpy as np
from itertools import product
import time
from random import randint


start_time = time.clock()

class EiwitStreng:
    def __init__(self, grid, score):
        self.grid = grid
        self.score = score


#Functie vraagt input aan en zet het om in een array met index.
def inputToList():
    n = 0;
    pt = []
    #eiwitInput = raw_input("voer de eiwit in: ")
    eiwitInput = "hhphhhph"
    #eiwitInput = "HPHPPHHPHPPHPHHPPHPH"

    for i in eiwitInput.upper():
        if i != "H" and i != "P":
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

#Functie maakt een Grid-Array aan de hand van de ingegeven eiwit string.
def makeGrid(inputList):
    grid = [["_"]* ((len(inputList)*2)-1) for i in (range(len(inputList*2)-1))]
    grid[len(inputToList())-1][len(inputToList())-1] = inputList[0]
    grid = np.array(grid, dtype='S256')

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

def counterScore(grid):

    score = 0
    #print i
    for j in range(len(grid)-1):
        #print i[j]
        for k in range(len(grid[j])-1):
            #print i[j][k], '-', i[j+1][k], '-', i[j][k+1]
            if grid[j][k] != '_' and grid[j][k][0] == 'H':
                if grid[j+1][k] != '_' and grid[j+1][k][0] == 'H':
                    score += 1
                if grid[j][k+1] != '_' and grid[j][k+1][0] == 'H':
                    score += 1

        #print 'score:', (score - counterFirst())

    return score - counterFirst()

#Deze functie gaat alle mogelijkheden af waarin het eiwit zich kan vouwen.
def cproduct():
    aListOfList = [["l", "r", "u", "d"] for aantal in range(len(inputToList())-2)]
    teller = [0,0]
    gridStart = makeGrid(inputToList())
    punt = ((len(inputToList()) - 1), (len(inputToList()) - 1))
    print punt
    punt = moveAmino(punt, "r")
    gridStart[punt[0]][punt[1]] = inputToList()[1]
    print gridStart
    highScore = 0
    highScoreList = []
    indexes = [0] * len(aListOfList)

    while True:
        teller[0] += 1
        #yield [l[i] for l, i in zip(aListOfList, indexes)]
        gridResult = np.copy(gridStart)
        punt = ((len(inputToList()) - 1), (len(inputToList())))
        #zm = [l[i] for l, i in zip(aListOfList, indexes)]
        index = -1
        for l, i in zip(aListOfList, indexes):
            index += 1
            punt = moveAmino(punt, l[i])

            if gridResult[punt[0]][punt[1]] != '_':
                for i in enumerate(indexes[index+1:]):
                    if indexes[i[0]+(index+1)] != 3:
                        indexes[i[0] + (index + 1)] = 3
                break
            gridResult[punt[0]][punt[1]] = inputToList()[index + 2]
        if inputToList()[-1] in gridResult:
            teller[1] += 1
            #print zm
            #print counterScore(gridResult)
            #print gridResult
            if counterScore(gridResult) > highScore:
                highScore = counterScore(gridResult)
                highScoreList = []
                highScoreList.append(EiwitStreng(gridResult, highScore))
            if counterScore(gridResult) == highScore:
                highScoreList.append(EiwitStreng(gridResult, highScore))
        j = len(indexes) - 1
        while True:
            indexes[j] += 1
            if indexes[j] < len(aListOfList[j]):
                break
            indexes[j] = 0
            j -= 1
            if j < 0:
                return highScoreList

def Monte(n):
    counter = 0
    directions = ["l", "r", "u", "d"]
    highScore = 0
    highScoreList = []
    gridStart = makeGrid(inputToList())
    punt = ((len(inputToList()) - 1), (len(inputToList()) - 1))
    print punt
    punt = moveAmino(punt, "r")
    gridStart[punt[0]][punt[1]] = inputToList()[1]
    print gridStart

    for i in range(n):
        gridResult = np.copy(gridStart)
        puntStart = ((len(inputToList()) - 1), (len(inputToList())))
        for i in inputToList()[2:]:
            forbidDirection = []
            while True:
                punt = puntStart
                direction = (randint(0, 3))
                punt = moveAmino(punt, directions[direction])
                #print directions[direction]
                #print counter
                if gridResult[punt[0]][punt[1]] == '_':
                    #print gridResult
                    break
                forbidDirection.append(directions[direction])
                if len(forbidDirection) > 4:
                    break
            #print directions[direction]
            gridResult[punt[0]][punt[1]] = i
            puntStart = punt


        if counterScore(gridResult) > highScore:
            highScore = counterScore(gridResult)
            highScoreList = []
            highScoreList.append(EiwitStreng(gridResult, highScore))
        if counterScore(gridResult) == highScore:
            highScoreList.append(EiwitStreng(gridResult, highScore))

        #print gridResult
        #counter +=1
        #print counter
    return highScoreList


print len(inputToList())

uitkomst = cproduct()

print len(uitkomst)
for i in uitkomst:
    print i.score
    print i.grid



print time.clock() - start_time, "seconds"

start_time = time.clock()

monteUitkomst = Monte(1000)
print len(monteUitkomst)
for i in monteUitkomst:
    print i.score
    print i.grid

print time.clock() - start_time, "seconds"


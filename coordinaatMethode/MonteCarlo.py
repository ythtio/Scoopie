import time
from random import randint

import networkx as nx
import pylab as plt

from Eiwitstreng import *

start_time = time.clock()

#Functie om het pad te visualiseren.
def visualPath(protein):


    G = nx.Graph()
    for i in range(len(protein.streng)):
        G.add_node(protein.streng[i], pos = (protein.coordinates[i][0], protein.coordinates[i][1]))
    G.add_path(protein.streng)
    '''
    for i in range(len(proteinString)):
        xas, yas = np.where(grid == proteinString[i])
        G.add_node(proteinString[i], pos=(xas[0], yas[0]))
    G.add_path(proteinString)
    '''

    nx.draw(G, nx.get_node_attributes(G, 'pos'), with_labels=True)
    plt.show()

# Functie vraagt input aan en zet het om in een array met index.
def inputToList():
    n = 0;
    pt = []
    # eiwitInput = raw_input("voer de eiwit in: ")
    #eiwitInput = "hhphhhph"
    #eiwitInput = "HPHPPHHPHPPHPHHPPHPH"
    eiwitInput = "PPPHHPPHHPPPPPHHHHHHHPPHHPPPPHHPPHPP"

    for i in eiwitInput.upper():
        if i != "H" and i != "P":
            print "Het eiwit mag geen", i, "bevatten"
            return "Het eiwit mag geen", i, "bevatten"
        pt.append(i + str(n))
        n += 1

    #eiwit = EiwitStreng(pt, counterFirst(pt), [])

    return pt

    return eiwit


# Deze functie heeft een +1 score voor elke H's die naast elkaar staan.
def counterFirst(indexList):
    counter = 0
    for i in range(len(indexList) - 1):
        if indexList[i][0] == "H" and indexList[i + 1][0] == "H":
            counter += 1
    return counter


# Deze functie plaats een nieuwe aminozuur in de grid adh van opgegeven richting
def moveAmino(point, direction):
    newPoint = (0, 0)

    if direction == "l":
        newPoint = (point[0], point[1] - 1)
    elif direction == "r":
        newPoint = (point[0], point[1] + 1)
    elif direction == "u":
        newPoint = (point[0] - 1, point[1])
    elif direction == "d":
        newPoint = (point[0] + 1, point[1])

    return newPoint


def finalScore(coordinateList, protein):
    score = 0
    for i in range(len(coordinateList)):
        if ([coordinateList[i][0], coordinateList[i][1] + 1]) in coordinateList:
            j = coordinateList.index([coordinateList[i][0], coordinateList[i][1] + 1])
            if protein.streng[i][0] == 'H' and protein.streng[j][0] == 'H':
                score += 1
        if ([coordinateList[i][0] + 1, coordinateList[i][1]]) in coordinateList:
            j = coordinateList.index([coordinateList[i][0] + 1, coordinateList[i][1]])
            if protein.streng[i][0] == 'H' and protein.streng[j][0] == 'H':
                score += 1
                # print i[j]

    # print 'beginscore =',protein.score
    return score - protein.score


def Monte(n):
    directions = ["l", "r", "u", "d"]
    highScore = 0
    highScoreList = []
    protein = EiwitStreng(inputToList(), counterFirst(inputToList()), [])
    coordinateStart = protein.coordinates[:]
    print protein.streng
    print protein.score
    print protein.coordinates, '\n -----------------------------'

    for i in range(n):
        coordinates = protein.coordinates[:]
        # print 'startcoordinaten:', coordinateStart
        puntStart = protein.pointStart[:]
        for i in range(len(protein.streng[2:])):
            # print i
            # print puntStart
            forbidDirection = []

            punt = puntStart
            direction = (randint(0, 3))
            punt = moveAmino(punt, directions[direction])
            # print punt

            while True:
                punt = puntStart
                direction = (randint(0, 3))
                punt = moveAmino(punt, directions[direction])
                # print directions[direction]
                if ([punt[0], punt[1]]) not in coordinates:
                    # print gridResult
                    break
                if directions[direction] not in forbidDirection:
                    forbidDirection.append(directions[direction])
                if len(forbidDirection) == 4:
                    break
            #print coordinates
            if len(forbidDirection) != 4:
                coordinates[i + 2] = [punt[0], punt[1]]
                puntStart = punt

        # print coordinates
        # print 'score:', finalScore(coordinates, protein)

        if len(forbidDirection) != 4:
            if finalScore(coordinates, protein) > highScore:
                highScore = finalScore(coordinates, protein)
                highScoreList = []
                highScoreList.append(EiwitStreng(protein.streng[:], highScore, coordinates))
            if finalScore(coordinates, protein) == highScore:
                highScoreList.append(EiwitStreng(protein.streng[:], highScore, coordinates))

                # print gridResult
                # counter +=1
                # print counter
    return highScoreList


hogescore = Monte(10)

print 'lengte: ', len(hogescore)
for i in hogescore:
    print i.score
    print i.coordinates
    print i.streng
    visualPath(i)

print time.clock() - start_time, "seconds"

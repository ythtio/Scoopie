import numpy as np
from itertools import product
import time

# functie zet een eiwit om in een array met aminozuren en index
def eiwitList():

    index = 0
    eiwit = []
    
    # eiwitInput bevat de eiwitstreng
    eiwitInput = "HHPHHHPH"

    # voegt aan elk aminozuur een index toe en zet het in de eiwit array
    for i in eiwitInput.upper():
        if i != 'H' and i != 'P':
            print ("Het eiwit mag geen", i, "bevatten")
            return "Het eiwit mag geen", i, "bevatten"
        eiwit.append(i + str(index))
        index +=1

    return eiwit

# functie stelt een beginscore op voor opeenvolgende H's in de streng
def startScore():
    score = 0

    for i in range(len(eiwitList()) - 1):
        if eiwitList()[i][0] == "H" and eiwitList()[i+1][0] == "H":
            score += 1

    return score

# functie maakt een Grid-Array aan de hand van de ingevoerde eiwit
def makeGrid(eiwit):

    # de grid krijgt 2 maal de lengte van het eiwit - 1 en plaatst het eerste aminozuur in
    # het midden van de grid
    grid = [["_"] * ((len(eiwit) * 2) - 1) for i in (range(len(eiwit * 2) - 1))]
    grid[len(eiwitList()) - 1][len(eiwitList()) - 1] = eiwit[0]

    # de grid wordt omgezet in een numpy array
    grid = np.array(grid)

    return grid

# functie plaats een nieuw aminozuur in de grid adhv de opgegeven richting
def moveAmino(point, direction):

    # maakt een variabele aan voor het punt van het nieuwe aminozuur
    newPoint = (0,0)

    # plaatst het nieuwe aminozuur
    if direction == "l":
        newPoint = (point[0], point[1] - 1)
    elif direction == "r":
        newPoint = (point[0], point[1] + 1)
    elif direction == "u":
        newPoint = (point[0] - 1, point[1])
    elif direction == "d":
        newPoint = (point[0] + 1, point[1])

    return newPoint
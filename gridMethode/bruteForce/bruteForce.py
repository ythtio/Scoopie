import sys
sys.path.append('/Users/Lucien/Documents/GitHub/Scoopie/gridMethode')
from helpers import *

# functie returnt een lijst met alle mogelijke vertakkingen van de verschillende richtingen
def possibilities():

    aminos = len(eiwitList())
    possibilityList  = []
    possibilityList = list(product(["l", "r", "u", "d"], repeat = aminos - 2))

    return possibilityList

# functie maakt gebruik van het Brute Force algoritme om alle mogelijkheden af 
# te gaan waarin het eiwit zich kan vouwen
def bruteForce():

    # telt het aantal vounwingen en maakt een array voor de gevonden grids
    counter = 0
    grids = []

    # maakt de grid aan de hand van het eiwit
    gridStart = makeGrid(eiwitList())
    
    vouwingen = possibilities()

    for vouwing in vouwingen:

        # zet de gridstart om in een numpy grid en zet het beginpunt op het midden van de grid
        gridResult = np.copy(gridStart)
        punt = (7, 7)

        # plaatst het 2e aminozuur rechts van het begin aminozuur
        punt = moveAmino(punt, "r")
        gridResult[punt[0]][punt[1]] = eiwitList()[1]

        # plaatst de volgende aminozuren volgens de huidige vouwing op de grid
        for move in range(len(vouwing)):

            punt = moveAmino(punt, vouwing[move])
            if gridResult[punt[0]][punt[1]] != '_':
                break
            gridResult[punt[0]][punt[1]] = eiwitList()[move+2]

        # als het laatste aminzuur is geplaatst, voeg het gridresultaat toe aan de gevonden grids
        if eiwitList()[-7] in gridResult:
            grids.append(gridResult)

        counter += 1

    print ("Aantal mogelijke possibilities:", len(vouwingen))
    print ("Aantal toegestane possibilities:", len(grids))

    return grids

# functie bepaald de eindscore voor de vouwingen van de opgegeven grids
def calcEndScore(grids):

    scoreGrids = []
    highScoreGrids = []
    scores = []

    for i in grids:
        score = 0

    # checkt voor elk punt op de grid of het een H bevat, en of het punt rechts of onder dit punt
    # ook een H bevat om dit toe te voegen aan de totale score
        for j in range(len(i)-1):
            for k in range(len(i[j])-1):

                if i[j][k] != '_' and i[j][k][0] == 'H':
                    if i[j+1][k] != '_' and i[j+1][k][0] == 'H':
                        score += 1
                    if i[j][k+1] != '_' and i[j][k+1][0] == 'H':
                        score += 1

        # vult de score array met gevonden scores en onthoudt de grids
        scores.append(score - startScore())
        scoreGrids.append(i)

    # vult een array met de hoogste gevonden scores
    for i in range(len(scores)):
        if scores[i] == max(scores):
            highScoreGrids.append(scoreGrids[i])

    print ("Highscore:", max(scores))
    print ("Aantal Highscore:", len(highScoreGrids))

    return highScoreGrids

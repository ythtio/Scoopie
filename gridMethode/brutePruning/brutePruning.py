import sys
sys.path.append('/Users/Lucien/Documents/GitHub/Scoopie/gridMethode')
from helpers import *

class EiwitStreng:
    def __init__(self, grid, score):
        self.grid = grid
        self.score = score

# functie bepaald de eindscore van de vouwing van het eiwit
def endScore(grid):

    score = 0

    # checkt voor elk punt op de grid of het een H bevat, en of het punt rechts of onder dit punt
    # ook een H bevat om dit toe te voegen aan de totale score
    for j in range(len(grid) - 1):
        for k in range(len(grid[j]) - 1):

            if grid[j][k] != '_' and grid[j][k][0] == 'H':
                if grid[j+1][k] != '_' and grid[j+1][k][0] == 'H':
                    score += 1
                if grid[j][k+1] != '_' and grid[j][k+1][0] == 'H':
                    score += 1

    # berekent de totale score door de eindscore van de beginscore af te trekken
    totalScore = startScore() - score 

    return totalScore

# functie maakt gebruik van het Brute Force algoritme om alle mogelijkheden af 
# te gaan waarin het eiwit zich kan vouwen
def brutePruning():

    # maakt een list of list voor de mogelijke moves per aminozuur
    movesList = [["l", "r", "u", "d"] for amino in range(len(eiwitList()) - 2)]

    # telt het aantal geprobeerde en het aantal geslaagde vounwingen
    counter = [0,0]
    
    # maakt de grid aan de hand van het eiwit
    gridStart = makeGrid(eiwitList())

    # zet het beginpunt op het midden van de grid en plaatst het tweede aminozuur rechts 
    # van het eerste aminozuur om de rotatie-symmetrische oplossingen te prunen
    punt = ((len(eiwitList()) - 1), (len(eiwitList()) - 1))
    punt = moveAmino(punt, "r")
    gridStart[punt[0]][punt[1]] = eiwitList()[1]

    # houdt de best gevonden score bij van de gevonden eiwit vouwingen en voegt deze vouwing 
    # toe aan de lijst van best gevonden scores
    highScore = 0
    highScoreList = []

    # maakt de vouwing aan en zet deze allemaal op 0 (=links)
    vouwing = [0] * len(movesList)

    while True:

        # voegt een geprobeerde vouwing toe
        counter[0] += 1

        # zet de gridstart om in een numpy grid en reset het punt op het beginpunt (=het tweede aminozuur)
        gridResult = np.copy(gridStart)
        punt = ((len(eiwitList()) - 1), (len(eiwitList())))

        index = -1

        # loop die het eiwit alle mogelijke vouwingen laat doorlopen
        for move, i in zip(movesList, vouwing):
            index += 1
            punt = moveAmino(punt, move[i])

            # als het nieuwe punt al bezet is door een ander aminozuur betekent dit een foutieve oplossing,
            # er wordt vanaf de index van de stap waar het fout gaat gekeken, en alle indexen die daarop 
            # volgen worden 3 gemaakt, waardoor deze foutieve tak van vouwingen wordt gepruned
            if gridResult[punt[0]][punt[1]] != '_':
                for i in enumerate(vouwing[index + 1:]):
                    if vouwing[i[0] + (index + 1)] != 3:
                        vouwing[i[0] + (index + 1)] = 3
                break

            # als het nieuwe punt niet al bezet is, gaat de loop door naar het volgende aminozuur
            gridResult[punt[0]][punt[1]] = eiwitList()[index + 2]

        # als het laatste aminozuur voorkomt in de grid
        if eiwitList()[-1] in gridResult:

            # voegt een geslaagde vouwing toe
            counter[1] += 1

            # als de eindscore beter is dan de huidige beste score
            if endScore(gridResult) < highScore:

                # maak van deze eindscore de nieuwe beste score
                highScore = endScore(gridResult)

                # leeg de lijst van voorgaande best gevonden vouwingen
                highScoreList = []

                # en voeg de niewe beste vouwing toe aan de lijst van best gevonden vouwingen
                highScoreList.append(EiwitStreng(gridResult, highScore))

            # als de eindscore net zo goed is als de huidige beste score
            if endScore(gridResult) == highScore:

                # voeg de niewe beste vouwing toe aan de lijst van best gevonden vouwingen
                highScoreList.append(EiwitStreng(gridResult, highScore))

        j = len(vouwing) - 1
        while True:
            vouwing[j] += 1
            if vouwing[j] < len(movesList[j]):
                break
            vouwing[j] = 0
            j -= 1
            if j < 0:
                print ("Aantal geprobeerde vouwingen:", counter[0])
                print ("Aantal geslaagde vouwingen:", counter[1])
                print ("Highscore:", highScore)
                return highScoreList
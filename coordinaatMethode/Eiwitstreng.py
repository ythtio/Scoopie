class EiwitStreng:
    def __init__(self, streng, score, coordinates):
        self.streng = streng
        self.score = score
        self.coordinates = coordinates
        if self.coordinates == []:
            self.coordinates = self.eiwitCoordinates()
        self.pointStart = (self.coordinates[1][0], self.coordinates[1][1])

    def eiwitCoordinates(self):
        self.coordinates = [['_', '_'] for i in self.streng[2:]]
        self.coordinates = [[len(self.streng), len(self.streng)],
                            [len(self.streng) + 1, len(self.streng)]] + self.coordinates

        return self.coordinates
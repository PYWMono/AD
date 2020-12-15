from Data import *
from Goast import *

class body():
    def __init__(self, x, y):
        self.location = [x, y]
        self.direction = 68
        self.prevloc = [x, y]
        self.prevspace = 0
        self.point = 0

    def dirupdate(self, input):
        self.direction = input

    def locupdate(self, ispac):
        condir = dirdoc[self.direction]
        conloc = self.location[:]
        conloc[condir[0]] += condir[1]
        self.prevspace = map[conloc[0]][conloc[1]]
        if ispac == True:
            self.prevspace = 0
            if map[conloc[0]][conloc[1]] == 7:
                self.point += 1
        elif ispac == False:
            self.prevspace = map[conloc[0]][conloc[1]]
            if map[conloc[0]][conloc[1]] == 9 or map[conloc[0]][conloc[1]] == 2:
                self.prevspace = 0
        if  map[conloc[0]][conloc[1]] != 1:
            self.prevloc[0] = self.location[0]
            self.prevloc[1] = self.location[1]
            self.location[condir[0]] += condir[1]

class maploader(body, goast):

    def __init__(self):
        self.playbody = body(15, 9)
        self.goast1 = body(7, 9)
        self.finder = goast(self.goast1, self.playbody)
        self.playable = False

    def mapupdate(self):
        map[self.playbody.prevloc[0]][self.playbody.prevloc[1]] = self.playbody.prevspace
        map[self.goast1.prevloc[0]][self.goast1.prevloc[1]] = self.goast1.prevspace
        map[self.playbody.location[0]][self.playbody.location[1]] = 9
        map[self.goast1.location[0]][self.goast1.location[1]] = 2
        if self.playbody.point > 60:
            map[self.goast2.prevloc[0]][self.goast2.prevloc[1]] = self.goast2.prevspace
            map[self.goast2.location[0]][self.goast2.location[1]] = 2
        if self.playbody.point > 120:
            map[self.goast3.prevloc[0]][self.goast3.prevloc[1]] = self.goast3.prevspace
            map[self.goast3.location[0]][self.goast3.location[1]] = 2

    def update(self, key):
        self.goast1.dirupdate(self.finder.finding())
        self.goast1.locupdate(False)
        if self.playbody.point > 60:
            self.goast2.dirupdate(self.finder2.finding())
            self.goast2.locupdate(False)
        if self.playbody.point > 120:
            self.goast3.dirupdate(self.finder3.finding())
            self.goast3.locupdate(False)
        self.playbody.dirupdate(int(key))
        self.playbody.locupdate(True)
        self.mapupdate()

    def goastsec(self):
        if self.playbody.location == [1, 1]:
            self.goast2 = body(1, 17)
        else:
            self.goast2 = body(1, 1)
        self.finder2 = goast(self.goast2, self.playbody)

    def goastthi(self):
        if self.playbody.location == [1, 17]:
            self.goast3 = body(1, 1)
        else:
            self.goast3 = body(1, 17)
        self.finder3 = goast(self.goast3, self.playbody)

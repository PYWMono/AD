from Data import dirdoc, map

class goast():
    def __init__(self, goast, pac):
        self.goast = goast
        self.pac = pac

    def finding(self):
        dirable = []
        distance = []
        for i in dirdoc.keys():
            branch = self.goast.location[:]
            branch[dirdoc[i][0]] += dirdoc[i][1]
            if map[branch[0]][branch[1]] != 1 and map[branch[0]][branch[1]] != 2:
                dirable.append(i)
                distance.append(self.pita(branch))
        if len(dirable) == 1:
            return dirable[0]
        elif len(dirable) >= 2:
            dist = 0
            for i in range(1,len(dirable)):
                if distance[i]<distance[dist]:
                    dist=i
            return dirable[dist]
    def pita(self, branch):
        return (self.pac.location[0]-branch[0])*(self.pac.location[0]-branch[0])+(self.pac.location[1]-branch[1])*(self.pac.location[1]-branch[1])



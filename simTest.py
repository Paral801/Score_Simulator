import random
import math

stdTwo = 5.5
stdThree = 3.3
stdFpg = 4
stdPa = 8.2

class Team:
    def __init__(self, name, two, three, fpg, twoPct, threePct, foulPct, pa):
        self.name = name
        self.two = two
        self.three = three
        self.fpg = fpg
        self.twoPct = twoPct
        self.threePct = threePct
        self.foulPct = foulPct
        self.pa = pa

lightning = Team("Lightning", 60.23, 11.72, 9.78, .544, .412, .986, 82.45)
senators = Team("Senators", 58.67, 10.76, 7.87, .523, .423, .993, 83.43)

team1Two = (random.gauss(lightning.two, stdTwo) * lightning.twoPct * 2)
team1Three = (random.gauss(lightning.three, stdThree) * lightning.threePct * 3)
team1One = (random.gauss(senators.fpg, stdFpg) * lightning.foulPct)
team1SubTotal = team1One + team1Two + team1Three
team1Total = math.sqrt(team1SubTotal * random.gauss(senators.pa,stdPa))

team2Two = (random.gauss(senators.two, stdTwo) * senators.twoPct * 2)
team2Three = (random.gauss(senators.three, stdThree) * senators.threePct * 3)
team2One = (random.gauss(lightning.fpg, stdFpg) * senators.foulPct)
team2SubTotal = team1One + team1Two + team1Three
team2Total = math.sqrt(team1SubTotal * random.gauss(lightning.pa,stdPa))

winner = ""
if team1Total > team2Total:
    winner = lightning.name
elif team2Total > team1Total:
    winner = senators.name

team1Score = round(team1Total,0)
team2Score = round(team2Total,0)

print("Lightning: " + str(team1Score) + "\n" + "Senators: " + str(team2Score) + "\n" + winner + " wins!")


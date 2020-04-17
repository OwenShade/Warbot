from time import sleep
from random import randint, choice

competitors = []
verbs = ["destroyed", "demolished", "dismantled", "ended", "crushed", "wiped out", "butchered",
"slayed", "eradicated", "killed", "assassinated", "executed", "slaughtered"]
causesOfDeath = ["poisoning them", "throwing them from the top of the boyd orr building", "shooting them",
"suffocating them", "tricking them into killing themselves", "throwing one fatal punch",
"crawling inside them via their mouth and then wearing them as a trendy new jacket"]

print("How many competitors would you like in this battle?")
number = int(input())

while (number % 2 != 0):
    print("Please enter an even number of competitors")
    number = int(input())

for i in range(0, number):
    print("What is the name of Competitor #", i+1, "?")
    temp = str(input())
    competitors.append(temp)


def battle(competitor1, competitor2):
    verb = choice(verbs)
    causeOfDeath = choice(causesOfDeath)
    print("FIGHT!")
    loser = randint(0,1)
    if loser == 1:
        sleep(2)
        print(competitor1, "has", verb, competitor2 , "by", causeOfDeath)
        print("---------------------------")
        return competitor2
    else:
        sleep(2)
        print(competitor2, "has", verb, competitor1 , "by", causeOfDeath)
        print("---------------------------")
        return competitor1

battlenumber = 1
while(len(competitors) > 2):
    competitor1 = choice(competitors)
    competitor2 = choice(competitors)
    while competitor1 == competitor2:
        competitor2 = choice(competitors)
    print("Battle #", battlenumber, " is between ", competitor1, " and ", competitor2)
    sleep(2)
    loser = battle(competitor1, competitor2)
    competitors.remove(loser)
    battlenumber += 1

print("And now for the final battle, between" , competitors[0], "and", competitors[1])
sleep(1)
loser = battle(competitors[0], competitors[1])
if loser == competitors[0]:
    print(competitors[1], "reigns over them all")
else:
    print(competitors[0], "reigns over them all")






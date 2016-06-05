t = [[ 0,  0,  0,  0,  0,  0], #Cooldowns
     [ 0,  0,  0,  0,  0,  0], #Haste Amount
     [ 0,  0,  0,  0,  0,  0], #Current
     ["", "", "", "", "", ""]] #Names

shortcuts = [["chinese", "dragonbound", "dragoncaller", "single orb", "double orb"], #Names
             [9, 10, 7, 7, 9], #Cooldowns
             [1,  1, 1, 1, 1]] #Haste Amount

def displayInfo():
    print""
    print ("------ Turn " + str(turnCount) + " -----").center(78)
    print""
    for i in range(6):
        if t[2][i] == 0:
            line1 = "Slot " + str(i + 1) + " \"" + str(t[3][i]) + "\" : charged"
        else:
            line1 = "Slot " + str(i + 1) + " \"" + str(t[3][i]) + "\" : in " + str(t[2][i]) + " turns"
        
        print line1.center(78)
    print""
        

print"        __ __         __        _____     __         __     __                "    
print" ____  / // /__ ____ / /____   / ___/__ _/ /_____ __/ /__ _/ /____  ____  ____"
print"/___/ / _  / _ `(_-</ __/ -_) / /__/ _ `/ / __/ // / / _ `/ __/ _ \/ __/ /___/"
print"     /_//_/\_,_/___/\__/\__/  \___/\_,_/_/\__/\_,_/_/\_,_/\__/\___/_/         "
print""
    
#escape characters, 78 characters wide

print "Input : ".center(78)

for i in range(6):
    t[3][i] = raw_input("Card #" + str(i+1) + "'s Name / Type : ")
    if t[3][i] in shortcuts[0]:
        t[0][i] = shortcuts[1][shortcuts[0].index(t[3][i])]
        t[1][i] = shortcuts[2][shortcuts[0].index(t[3][i])]
    else:
        t[0][i] = int(input(t[3][i] + "'s Active Cooldown : "))
        t[1][i] = int(input(t[3][i] + "'s Haste Turns     : "))

turnCount = 0
skillBoosts = int(input("Total Skill Boosts : "))

#add boosts
for i in range(len(t[0])):
    t[2][i] = t[0][i] - skillBoosts
    if (t[2][i] < 0):
        t[2][i] = 0

print "Simulation : ".center(78)

displayInfo()

while turnCount < 100:
    activated = int(input("Press Button (0 for Pass) :"))
    if activated != 0: #0 : pass
        activated -= 1
        t[2][activated] = t[0][activated]
        for i in range(len(t[1])): #haste other cds
            t[2][i] -= t[1][activated]
            if (t[2][i] < 0):
                t[2][i] = 0
        t[2][activated] += t[1][activated] #haste doesn't affect self cd
    else:
        for i in range(len(t[1])):
            t[2][i] -= 1
            if (t[2][i] < 0):
                t[2][i] = 0
        turnCount += 1
    displayInfo()

t = [[ 0,  0,  0,  0,  0,  0], #Cooldowns
     [ 0,  0,  0,  0,  0,  0], #Haste Amount
     [ 0,  0,  0,  0,  0,  0], #Current
     ["", "", "", "", "", ""]] #Names

shortcuts = [["chinese", "dragonbound", "dragoncaller", "single orb", "double orb"], #Names
             [9, 10, 7, 7, 9], #Cooldowns
             [1,  1, 1, 1, 1]] #Haste Amount

print"     ___  ________   ________  ___  ___  _________    " 
print"    |\  \|\   ___  \|\   __  \|\  \|\  \|\___   ___\  "
print"    \ \  \ \  \\\ \  \ \  \|\  \ \  \\\\\  \|___ \  \_|  "
print"     \ \  \ \  \\\ \  \ \   ____\ \  \\\\\  \   \ \  \   "
print"      \ \  \ \  \\\ \  \ \  \___|\ \  \\\\\  \   \ \  \  "
print"       \ \__\ \__\\\ \__\ \__\    \ \_______\   \ \__\ "
print"        \|__|\|__| \|__|\|__|     \|_______|    \|__| "
print""
#escape characters

for i in range(6):
    t[3][i] = raw_input("Card #" + str(i+1) + "'s Name : ")
    if t[3][i] in shortcuts[0]:
        t[0][i] = shortcuts[1][shortcuts[0].index(t[3][i])]
        t[1][i] = shortcuts[2][shortcuts[0].index(t[3][i])]
    t[0][i] = int(input(t[3][i] + "'s Active Cooldown : "))
    t[1][i] = int(input(t[3][i] + "'s Haste Turns     : "))

turnCount = 0
skillBoosts = int(input("Total Skill Boosts               : "))

for i in range(len(t[0])):
    t[2][i] = t[0][i] - skillBoosts
    if (t[2][i] < 0):
        t[2][i] = 0
print t[2]

while turnCount < 100:
    turnCount += 1
    activated = int(input("Button Pressed:"))
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
    print t[2]

t = [[7, 7, 9, 9, 10, 7], #Cooldowns
     [1, 1, 1, 1, 0, 1], #Haste Amount
     [0, 0, 0, 0, 0, 0]] #Current

turnCount = 0
skillBoosts = 10

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

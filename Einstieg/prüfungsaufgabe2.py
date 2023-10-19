sitze = [[True, True, True, False, True, True, False, False, False, False, True, False, True, True, True, False, False, True, True, False, False, False, False, False, True, False, True, True, True, False], [True, True, True, False, True, True, True, True, True, False, True, False, True, True, False, False, False, True, True, True, True, True, True, False, True, False, True, True, True, False], [True, False, False, False, False, True, False, True, True, False, True, False, True, True, False, False, False, False, False, False, True, False, True, True, True, False, True, True, True, False], [True, True, True, True, False, True, False, True, True, False, True, False, False, False, False, True, True, True, True, False, True, False, True, True, True, False, False, False, True, False], [True, True, True, False, False, True, False, True, True, True, True, True, False, False, True, True, True, True, False, False, True, False, True, True, True, True, False, False, True, False], [True, False, False, False, False, True, False, False, False, True, True, True, False, False, True, True, False, False, False, False, True, False, False, False, True, True, True, True, True, False], [True, False, False, False, True, True, True, False, False, True, True, True, True, True, True, True, False, False, False, True, True, True, False, False, True, True, True, True, True, False]]
anzahl = int(input("anzahl der personen: "))
save = []
counter = 0
x = 0
y = 0
end = False

for i in range (0,7):
    for j in range (0,30):
        if sitze[i][j] == True:
            y = (i + 1) * 100
            x = j + 1
            save.append(y+x)
            counter += 1
            if counter == anzahl:
                end = True
                break
        else:
            counter = 0
            save = []
    if end == True:
        break

print(save)
counter = 0
g = 0
stream = open("C:/Users/dzygm/OneDrive/Desktop/Schule/Python/Einstieg/Texte/Namen.txt", mode="rt", encoding="UTF-8")
zeile = stream.readlines()
gruppe = [[]]

for z in zeile:
    z = z.replace("\n","")
    if counter != 4:
        gruppe[g].append(z)
        counter += 1
    else:
        counter = 1
        g += 1
        gruppe.append([])
        gruppe[g].append(z)

print(gruppe)
try:
    stream = open("C:/Users/dzygm/OneDrive/Desktop/Schule/Python/Einstieg/Texte/verein.csv", mode="rt", encoding="UTF-8")
    previous = None
    data = []
    zeile = stream.readline()
    initialized = False
    while zeile != '':

        z = zeile.split(';')
        z[4] = z[4].replace("\n","")
        z[1] = int(z[1])
        z[2] = int(z[2])
        z[3] = float(z[3])
        z[4] = int(z[4])

        if previous is None:
            previous = z

        if previous[2] == z[2]:
            if initialized is True:
                previous[4] += z[4]
            else:
                initialized = True
        else:
            data.append(previous)
            previous = z

        zeile = stream.readline()
    data.append(previous)
    for entity in data:
        print(entity)
except Exception as e:
    print(e)
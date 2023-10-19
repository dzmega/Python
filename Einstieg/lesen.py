eingabe = input("namen eingeben: ")
eingabe.lower()
try:
    stream = open("C:/Users/dzygm/OneDrive/Desktop/Schule/Python/Einstieg/Texte/" + eingabe + ".txt", mode="rt", encoding="UTF-8")
    print(stream.read())
    stream.close()
except Exception as e:
    print(e)
dictionary = {"cat":"chat","dog":"chien"}

try:
    for key, value in dictionary.items():
        print(key," ",value)
except:
    print("Fehler")
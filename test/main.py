stream = open("C:/Users/dzygm/OneDrive/Desktop/Schule/Python/test/blacklist.txt")
list = stream.readlines()
eingabe = input("eingabe: ")
stop = False
new = ""

for i in range(len(list)):
    element = list[i].replace("\n","")
    if element in eingabe:
        l = len(element)
        censored = element[0] + element [1]
        for j in range(2,l):
            censored += '*'
        eingabe = eingabe.replace(element, censored)
        i = 0
        censored = ""

print(eingabe)
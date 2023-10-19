wort = input("geben sie ein wort ein: ")
wort = wort.replace(" ","")
edit = wort[::-1]

if wort == edit:
    print("es ist ein palindrom")
else:
    print("es ist kein palindrom")
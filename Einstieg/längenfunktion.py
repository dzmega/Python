wort1 = len(input("geben sie ein wort ein: "))
wort2 = len(input("geben sie ein wort ein: "))

if wort1 > wort2:
    print("das erste wort ist länger")
elif wort2 > wort1:
    print("das zweite wort ist länger")
else:
    print("beide wörter sind gleich lang")
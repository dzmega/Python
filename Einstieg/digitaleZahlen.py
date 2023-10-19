def ausprinten(arr):
    for row in arr:
        for element in row:
            print(element)
        print()

null = [
    ["#  #  #"],
    ["#     #"],
    ["#     #"],
    ["#     #"],
    ["#  #  #"]
]
eins = [
    ["      #"],
    ["      #"],
    ["      #"],
    ["      #"],
    ["      #"]
]
zwei = [
    ["#  #  #"],
    ["      #"],
    ["#  #  #"],
    ["#      "],
    ["#  #  #"]
]
drei = [
    ["#  #  #"],
    ["      #"],
    ["   #  #"],
    ["      #"],
    ["#  #  #"],
]
vier = [
    ["#     #"],
    ["#     #"],
    ["#  #  #"],
    ["      #"],
    ["      #"],
]
funf = [
    ["#  #  #"],
    ["#      "],
    ["#  #  #"],
    ["      #"],
    ["#  #  #"],
]
sechs = [
    ["#  #  #"],
    ["#      "],
    ["#  #  #"],
    ["#     #"],
    ["#  #  #"],
]
sieben = [
    ["#  #  #"],
    ["      #"],
    ["      #"],
    ["      #"],
    ["      #"],
]
acht = [
    ["#  #  #"],
    ["#     #"],
    ["#  #  #"],
    ["#     #"],
    ["#  #  #"],
]
neun = [
    ["#  #  #"],
    ["#     #"],
    ["#  #  #"],
    ["      #"],
    ["#  #  #"],
]

zahl = int(input("geben sie eine zahl ein: "))
res = [int(x) for x in str(zahl)]
i = len(res)
for z in range(i):
    if res[z] == 0:
        ausprinten(null)
    if res[z] == 1:
        ausprinten(eins)
    if res[z] == 2:
        ausprinten(zwei)
    if res[z] == 3:
        ausprinten(drei)
    if res[z] == 4:
        ausprinten(vier)
    if res[z] == 5:
        ausprinten(funf)
    if res[z] == 6:
        ausprinten(sechs)
    if res[z] == 7:
        ausprinten(sieben)
    if res[z] == 8:
        ausprinten(acht)
    if res[z] == 9:
        ausprinten(neun)
    print()
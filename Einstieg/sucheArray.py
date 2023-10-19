array = [1, 2, 3]
zahl = int(input("geben sie eine gesuchte zahl ein: "))
print(array)

if zahl in array:
    z = len(array)
    i = 0
    while(i < z):
        if array[i] == zahl:
            print("die zahl befindet sich an der stelle ",i)
            i += 1
        else:
            i += 1
else:
    print("zahl kommt nicht im array vor")
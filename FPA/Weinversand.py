def ermittlePrüfziffer(arr):
    sum = (arr[0]*1) + (arr[1]*3) + (arr[2]*1) + (arr[3]*3) + (arr[4]*1) + (arr[5]*3) + (arr[6]*1) + (arr[7]*3) + (arr[8]*1)
    ziffer = sum - (sum % 10)
    return ziffer

def sucheTopseller(krit):
    absatz = [[123, 456, 78, 9, 46], [333, 125, 20, 4, 998], [123, 666, 21, 1, 5646], [333, 125, 22, 2, 9981]]
    previous = absatz[0]
    top = absatz[0]
    for i in absatz:
        if krit == 0:
            if previous[4] < i[4] and i[0] == krit:
                top = i
        if krit == 1:
            if previous[4] < i[4] and i[1] == krit:
                top = i
        if krit == 2:
            if previous[4] < i[4] and i[2] == krit:
                top = i
        if krit == 3:
            if previous[4] < i[4] and i[3] == krit:
                top = i
    top.remove(top[4])
    kette = str(top[0]) + "-" + str(top[1]) + "-" + str(top[2]) + "-" + str(top[3])
    return kette

array = [1,2,3,4,5,6,7,8,9]
kriterium = int(input("geben sie ein kriterium ein: "))

p = ermittlePrüfziffer(array)
k = sucheTopseller(kriterium)

print(p)
print(k)
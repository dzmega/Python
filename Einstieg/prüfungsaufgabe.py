string = "QQQQRRRRRRTTTTTTTTTTLLLLLLLLLLLMNNNVVVVVVVVVVVAAAAAAAAAAAAA"
b = string[0]
counter = 0
data = ""

for i in range(len(string)):
    j = string[i]
    if j == b:
        counter += 1
    else:
        if counter > 3:
            data += "$" + str(counter) + string[i-1]
        else:
            for x in range(counter):
                data += string[i-1]
        b = j
        counter = 1

print(data)
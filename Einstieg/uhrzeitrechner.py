h = int(input("starting time (hours): "))
m = int(input("starting time (minutes): "))
d = int(input("event duration (minutes): "))

d += m

h += d / 60
h = int(h % 24)
m = d % 60

print("enduhrzeit: ",h, ":",m)
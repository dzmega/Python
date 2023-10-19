pw = input("passwort: ")
points = 0

if len(pw) >= 8:
    points += 1

if len(pw) < 8:
    points = 0
kg = float(input("geben sie ihr gewicht in kilo an: "))
gr = float(input("geben sie ihre größe an: "))

bmi = kg / gr * gr

if bmi >= 35 and bmi <= 39.9:
    print("Adipositas Grad 2")
elif bmi >= 30 and bmi <= 34.9:
    print("Adipositas Grad 1")
elif bmi >= 25 and bmi <= 29.9:
    print("Übergewicht")
elif bmi >= 18.5 and bmi <= 24.9:
    print("Normalgewicht")
else:
    print("Untergewicht")
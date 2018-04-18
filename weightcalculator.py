mass = float(input("Please give the mass of the object in kilograms: "))

weight = round(mass * 9.8, 9)

if mass > 500:
    print("Object too large")
elif weight < 100:
    print("Object too small")
else:
    print("The object's weight is:", weight, " Newtons")

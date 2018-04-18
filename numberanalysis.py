print("Enter 20 numbers")

var1 = float(input("1: "))
var2 = float(input("2: "))
var3 = float(input("3: "))
var4 = float(input("4: "))
var5 = float(input("5: "))
var6 = float(input("6: "))
var7 = float(input("7: "))
var8 = float(input("8: "))
var9 = float(input("9: "))
var10 = float(input("10: "))
var11 = float(input("11: "))
var12 = float(input("12: "))
var13 = float(input("13: "))
var14 = float(input("14: "))
var15 = float(input("15: "))
var16 = float(input("16: "))
var17 = float(input("17: "))
var18 = float(input("18: "))
var19 = float(input("19: "))
var20 = float(input("20: "))

list = [var1, var2, var3, var4, var5, var6, var6, var7, var8, var9, var10, var11, var12, var13, var14, var15, var16, var17, var18, var19, var20]
total = 0
current = 0
highest = 0
lowest = 0
max = 0
min = 99999999

for i in range(len(list)):
    total += list[i]

    if list[i] > max:
        max = list[i]
        highest = list[i]

    if list[i] < min:
        min = list[i]
        lowest = list[i]

avg = total / 20

print("The total sum of those numbers is: ", total)
print("The average number is: ", avg)
print("The highest number is: ", highest)
print("The lowest number is: ", lowest)

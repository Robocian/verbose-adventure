print("Please enter 10 different numbers below")

num1 = float(input("A: "))
num2 = float(input("B: "))
num3 = float(input("C: "))
num4 = float(input("D: "))
num5 = float(input("E: "))
num6 = float(input("F: "))
num7 = float(input("G: "))
num8 = float(input("H: "))
num9 = float(input("I: "))
num10 = float(input("J: "))

list1 = [num1, num2, num3, num4, num6, num7, num8, num9, num10]

# Declaring variables to be used
total = 0
highest = 0
lowest = 0
max = 0
min = 99999999


for i in range(len(list1)):
    total += list1[i]

    if list1[i] > max:
        max = list1[i]
        highest = list1[i]

    if list1[i] < min:
        min = list1[i]
        lowest = list1[i]

avg = total / 10

print("The lowest number is: ", lowest)
print("The highest number is: ", highest)
print("The total sum of the numbers is: ", total)
print("The average value of the numbers is: ", avg)

num = int(input("Give a number: "))

romnum = "Empty"

if num == 1:
    romnum = "I"
elif num == 2:
    romnum = "II"
elif num == 3:
    romnum = "III"
elif num == 4:
    romnum = "IV"
elif num == 5:
    romnum = "V"
elif num == 6:
    romnum = "VI"
elif num == 7:
    romnum = "VII"
elif num == 8:
    romnum = "VIII"
elif num == 9:
    romnum = "IX"
elif num == 10:
    romnum = "X"
else:
    romnum = "ERROR"

print("In roman numerals your number is: ", romnum)

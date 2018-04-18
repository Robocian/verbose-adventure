digits = str(input("Enter a line of digits with no separating spaces: "))

digit_count = len(digits)

sum = 0

for current_digit in range(digit_count):
    var = int(digits[current_digit])
    sum += var


print("The sum of those digits is: ", sum)

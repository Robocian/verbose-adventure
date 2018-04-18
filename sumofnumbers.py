number_file = open("numbers.txt", "r")

##read_file = number_file.read()

##print(read_file)

line1 = int(number_file.readline())
line2 = int(number_file.readline())
line3 = int(number_file.readline())
line4 = int(number_file.readline())
line5 = int(number_file.readline())
line6 = int(number_file.readline())
line7 = int(number_file.readline())
line8 = int(number_file.readline())
line9 = int(number_file.readline())
line10 = int(number_file.readline())


number_file.close()

total_sum = line1 + line2 + line3 + line4 + line5 + line6 + line7 + line8 + line9 + line10

print("The total sum is equal to: ", total_sum)

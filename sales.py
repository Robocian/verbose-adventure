print("How many sales were made on the following days?")

monday = int(input("Monday: "))
tuesday = int(input("Tuesday: "))
wednesday = int(input("Wednesday: "))
thursday = int(input("Thursday: "))
friday = int(input("Friday: "))
saturday = int(input("Saturday: "))
sunday = int(input("Sunday: "))

sales_list = [monday, tuesday, wednesday, thursday, friday, saturday, sunday]

week_sales = 0

for i in range(len(sales_list)):
    week_sales += sales_list[i]

print("The total sales this week amounts to: ", week_sales)

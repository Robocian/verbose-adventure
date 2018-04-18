print("Please enter the amount of rainfall that occured in each of the following months")

jan = int(input("January: "))
feb = int(input("February: "))
mar = int(input("March: "))
apr = int(input("April: "))
may = int(input("May: "))
jun = int(input("June: "))
jul = int(input("July: "))
aug = int(input("August: "))
sep = int(input("September: "))
oct = int(input("October: "))
nov = int(input("November: "))
dec = int(input("December: "))

# Declaring important things
month_list = [jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec]
total_rainfall = 0
current_month = 0
top_month = 0
bottom_month = 0
max = 0
min = 99999999

# The calculating machine
for i in range(len(month_list)):
    total_rainfall += month_list[i]

# Current month naming machine
    if i == 0:
        current_month = "January"
    elif i == 1:
        current_month = "February"
    elif i == 2:
        current_month = "March"
    elif i == 3:
        current_month = "April"
    elif i == 4:
        current_month = "May"
    elif i == 5:
        current_month = "June"
    elif i == 6:
        current_month = "July"
    elif i == 7:
        current_month = "August"
    elif i == 8:
        current_month = "September"
    elif i == 9:
        current_month = "October"
    elif i == 10:
        current_month = "November"
    else:
        current_month = "December"

    # Max finder
    if month_list[i] > max:
        top_month = current_month
        max = month_list[i]

    # Min finder
    if month_list[i] < min:
        bottom_month = current_month
        min = month_list[i]

avg_rainfall = total_rainfall / 12

print("The total rainfal this year was: ", total_rainfall)
print("The average rainfall per month this year was: ", avg_rainfall)
print("The month with the most rainfall was: ", top_month)
print("The month with the least rainfall was: ", bottom_month)

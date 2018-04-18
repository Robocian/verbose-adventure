date = input("Give the name in the format 'dd/mm/yyyy': ")

day = date[0:2]
year = date[6:10]

month = int(date[3:5])

if month == 1:
    month = "January"
elif month == 2:
    month = "February"
elif month == 3:
    month = "March"
elif month == 4:
    month = "April"
elif month == 5:
        month = "May"
elif month == 6:
        month = "June"
elif month == 7:
        month = "July"
elif month == 8:
            month = "August"
elif month == 9:
            month = "September"
elif month == 10:
                month = "October"
elif month == 11:
                month = "November"
elif month == 12:
                month = "December"


print("The date is ", month, " ", day, ", ", year )

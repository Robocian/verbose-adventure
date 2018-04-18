years = int(input("How many years have passed: "))

while (years == int):
    season = 1

    while (season <= 4):
        seasonal_rainfall = int(input("How many inches of rainfall has been had this season? "))
        season += 1

    years += 1
    print(seasonal_rainfall)
#total_rainfall =
#avg_monthly_rainfall =

print(years)
print(seasonal_rainfall)

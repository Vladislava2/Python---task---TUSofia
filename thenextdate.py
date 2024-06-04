year = int(input("Input a year: "))
if year % 4 == 0:
    leap_year = True
elif year % 100 == 0:
    leap_year = False
elif year % 400 == 0:
    leap_year = True
else: 
    leap_year = False 


month = int(input("Input a month: "))
if month in ()


day = int(input("Input a day: "))

nextDay = day + 1 

if month > 12:
    print("ERROR! Please input a valid month!")
if day > 31:
    print("ERROR! Please input a valid day!")
else:
    print("The next date is: " + str(year) + "-" + str(month) + "-" + str(nextDay))




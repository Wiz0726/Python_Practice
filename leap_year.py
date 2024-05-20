# This program is to check wheather a year is a leap year or not
year = int(input("Enter the year you want to check for leap year: "))

# divided by 100 means it is a century year (ending wit 00)
# if a century year is divisible by 400 it is a leap year
if year % 4 == 0 and year % 100 == 0:
    print(year, "is a leap year")

# not divided by 100 means it is not a century year
# if it is not a century year and is divisible by 4 it is a leap year
elif year % 4 ==0 and year % 100 != 0:
    print(year, "is a leap year")

# if it is not divisible by 4 and 400 it is not a leap year
else:
    print(year, "is not a leap year")
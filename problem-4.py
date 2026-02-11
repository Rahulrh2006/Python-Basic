#to find leap year (if elif else)

year = int(input("Enter a year: "))

if (year % 400 == 0):
    print(" is a leap year.")
elif (year % 100 == 0):
    print(" is not a leap year.")
elif (year % 4 == 0):
    print(" is a leap year.")
else:
    print(" is not a leap year.")

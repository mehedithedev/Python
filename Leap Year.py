#This program is gonna check if a year is leap year or not.
year = int(input("Choose a year to check if it's leap year or not: "))
if year%4==0:
    if year%100==0:
        if year % 400 == 0:
            print("Leap year")
    else:
        print("Leap year")

else:
    print("Not leap year")




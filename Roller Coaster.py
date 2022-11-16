print("Welcome to the Roller Coaster")
height=float(input("What's your height in feet? "))
if height>=5 :
    print("You are eligible to ride on the Roller Coaster!")
    age=int(input("How old are you? "))
    if age <= 12:
        bill=5
        #print("You have to pay $5 to proceed further.")
    elif age <18:
        bill=10
        #print("You have to pay $10. ")
    elif age <22:
        bill=12
        #print("You have to pay $12")
    else:
        bill=16
        #print("You have to pay adult fees, which is $16 in order to proceed further.")
    taking_photo = str(input("Whould you like to take some photos? Say yes or no."))
    if taking_photo=="yes":
        print(f"You have to pay {bill+3}$ in order to proceed further. ")
    else:
        print(f"Now you have to pay {bill}$")
else:
    print("You have to wait more to achive the required height.")

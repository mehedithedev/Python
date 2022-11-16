pizza_size=input("What size of pizza would you like to have? Choose one of them: S,M or L: ")
add_paperoni=input("Do you need to have paperoni? Yes or No? ")
add_cheese=input("Do you need extra cheese with your pizza? Yes or No? ")
if pizza_size=="S":
    price=25
elif pizza_size=="M":
    price=35
elif pizza_size=="L":
    price=40
else:
    print("Choose between S, M or L")
if add_paperoni=="Yes":
    if pizza_size=="S":
        price+=5
    elif pizza_size=="M":
        price+=8
    elif pizza_size=="L":
        price+=10
else:
    print("Choose a valid value. ")
if add_cheese=="Yes":
    price += 10
else:
    print("Choose a valid value. ")
print(f"Your bill is ${price}")

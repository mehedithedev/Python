your_name=input("What's your name? \n").lower()
partner_name=input("What's the name of your partner? \n").lower()
#Check for the character that came on the phrase: TRUE LOVE
t=your_name.count("t")
r=your_name.count("r")
u=your_name.count("u")
e=your_name.count("e")
true=str(t+r+u+e)

l=partner_name.count("l")
o=partner_name.count("o")
v=partner_name.count("v")
e=partner_name.count("e")
love=str(l+o+v+e)
#Combine both of those strings
true_love=int(true+love)
if true_love<=10 or true_love>=90:
    print(f"Your score is {true_love}, it's like mentos and coka-cola")
elif true_love<=55 and true_love>=40:
    print(f"Your score is {true_love}, you both hava a perfect bonding.")
else:
    print(f"Your true love score is {true_love}")
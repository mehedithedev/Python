height = float(input("What is your height in metres? "))
weight = int(input("What is your weight in Kilogram?"))
bmi= round(weight/(height**2))
if bmi<18.5:
    print("You are underweight. You have to eat more healthy foods.")
elif bmi<24:
    print("Normal weight")
elif bmi<30:
    print("Overweight")
elif bmi<35:
    print("obsessed")
else:
    print("Clinically Obsessed")

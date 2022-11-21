import random
import Random
# Rock Paper Scissors ASCII Art

user_input=int(input("Enter 0 for Rock\n"
                     "1 for Paper\n"
                     "2 for Scissors\n"))
print("You choose: ")
if user_input==0:
    # Rock
    print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)
elif user_input==1:
    # Paper
    print("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)
elif user_input==2:
    # Scissors
    print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)

pc_output=random.randint(0,2)
print("Your Computer choose: ")
if pc_output==0:
    # Rock
    print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)
elif pc_output==1:
    # Paper
    print("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)
elif pc_output==2:
    # Scissors
    print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)


if user_input==pc_output:
    print("It's a draw!")
elif user_input==0 and pc_output==1:
    print("You loose")
elif user_input==0 and pc_output==2:
    print("You won")
elif user_input==1 and pc_output==0:
    print("You won")
elif user_input==1 and pc_output==2:
    print("You loose")
elif user_input==2 and pc_output==0:
    print("You loose")
elif user_input==2 and pc_output==1:
    print("You won")
else:
    print("Enter a valid value!")
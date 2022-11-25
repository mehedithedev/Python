def eligible_username(username):
    if len(username)<5:
        print("Your username must have above 5 characters. ")
    else:
        password=input("Enter your password: ")
        print("Your credentials are valid. You are good to go.")
name_of_user=input("Insert your username: ")
eligible_username(name_of_user)



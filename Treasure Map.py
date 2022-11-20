row1=["😀","😀","😀"]
row2=["😀","😀","😀"]
row3=["😀","😀","😀"]
# Here goes a map which has been built on top of a nested arrey which has 3 rows and 3 columns
nested_arrey=[row1,row2,row3]
print(f"Here is the outlook of that arrey: \n"
      f"{row1}\n{row2}\n{row3}\n")
# Now the user is needed to provide the place where he wants to left his treasure

user_input=input("In which place would you like to store your treasure?\n")
vertical_index=int(user_input[0]) #2
horizontal_index=int(user_input[len(user_input)-1])  #1
print(horizontal_index)


selected_row= nested_arrey[vertical_index-1]
selected_row[horizontal_index-1]="X"


print(f"Here is the outlook of that arrey: \n"
      f"{row1}\n{row2}\n{row3}\n")

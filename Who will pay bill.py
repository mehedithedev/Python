import random
import math
# Here we are taking the list of people using "Split" method
names=input("Who are willing to pay the bills? \n")
if type(names)==str:
    names_arrey=names.split()
else:
    print("Enter some name with a space between!")
# Here we are using seed to generate a random number to make sure who is going to pay the bill.
insert_seed= float(input("Enter a seed number: \n"))
if type(insert_seed)==int or type(insert_seed)==float:
    random.seed(insert_seed)
    index_of_billpaye=random.randint(0,(len(names_arrey)-1))
else:
    print("Enter a exact number! ")
# print(index_of_billpaye)

# Here we are printing out the name of the person who has been chosen as the bill payer randomly:
bill_payer=names_arrey[index_of_billpaye]
print(f"Today the bill for food is going to payed by: {bill_payer} ")


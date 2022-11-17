import random

random_seed= int(input("Enter a seed number:"))
random.seed(random_seed)
random_int=random.randint(1,2)
#print(random_int)
# random_seed=123: random_int=1
# random_seed=545: random_int=2
# random_seed=anything else: random_int=anything .

if random_int==1:
    print("It's Head!")
elif random_int==2:
    print("It's Tail!")
else:
    print("Alas! There's nothing here for you..")

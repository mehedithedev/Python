# This program can be used to convert miles into kilometres and to calculate the full distance covered by the round trip.
def convert_distances(miles):
    return miles*1.6

user_mile=50
km=convert_distances(user_mile)
# miles=input("Tell the number of miles you want to convert into KM?\n")
#Now convert miles into km by using convert_distances function:
print(f"Converted mile is: {km} KM ")

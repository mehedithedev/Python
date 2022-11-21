# These are the average height of students of some students in a particular school in centimeter.
# height_of_students=[180,170,160,152,145,168,182,169,152,138,151,130,140,150,167,168,128,120]
# for average_height in height_of_students:
#     # print(average_height)
#     # print(type(average_height))
#     print(height_of_students)

height_of_students= input("Insert a list of students heights?")
for n in range(0, len(height_of_students)):
    height_of_students[n]=int(height_of_students[n])
print(height_of_students)
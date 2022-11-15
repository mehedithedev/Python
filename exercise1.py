#add four digit number 
userNum= input("Write down a four digit number")
digit1= userNum[0]
digit2= userNum[1]
digit3= userNum[2]
digit4= userNum[3]
# print(type(userNum))
# That means we have to convert userNum from string to number in order to add them 
sumOfNum= int(digit1)+ int(digit2)+ int(digit3)+ int(digit4)
print(sumOfNum)

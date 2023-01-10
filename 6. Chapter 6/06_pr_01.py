# # my method to sort the greatest number entered by the user
# num1= int(input("Enter No 1 :"))
# num2= int(input("Enter No 2: "))
# num3= int(input("Enter No 3: "))
# num4= int(input("Enter No 4: "))

# numset= [num1,num2,num3,num4]
# numset.sort()
# print ("The greatest number you entered is ", numset[3])

# harrys method to find greatest number
num1= int(input("Enter No 1 :"))
num2= int(input("Enter No 2: "))
num3= int(input("Enter No 3: "))
num4= int(input("Enter No 4: "))

if (num4>num3):
    f1= num4
else:
    f1= num1

if (num3>num2):
    f2= num3
else: 
    f2= num2

if (f2>f1):
    print (f2, "is the greatest number")
else :
    print (f1, "is the greatest number")

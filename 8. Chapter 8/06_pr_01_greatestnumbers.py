# ## my method to find the greatest number using function
# num1= int(input("Enter num 1: "))
# num2= int(input("Enter num 2: "))
# num3= int(input("Enter num 3: "))
# num4= int(input("Enter num 4: "))
# num5= int(input("Enter num 5: "))
# num6= int(input("Enter num 6: "))

# list = [num1,num2,num3]
# list2= [num4,num5,num6]

# def great(num):
#     num.sort()
#     a= num[2]
#     print (" The greatest of the numbers you entered is :",a)

# great(list)
# great(list2)
##----------------------------------------------------------------------------
## harrys method to find the greatest number using function:
num1= int(input("Enter num 1: "))
num2= int(input("Enter num 2: "))
num3= int(input("Enter num 3: "))
def great(num1,num2,num3):
    if num1>num2:
        if num1>num3:
            return num1
        return num3
    if num2>num3:
        return num2
    return num3

print ( "The greatest of the numbers entered is :", great(25,65,101))
##----------------------------------------------------------------------------
# ## harrys method to find the greatest number using function:
# num1= int(input("Enter num 1: "))
# num2= int(input("Enter num 2: "))
# num3= int(input("Enter num 3: "))

# def great(num1,num2,num3):
#     if num1>num2:
#         if num1>num3:
#             return num1
#         return num3
#     if num2>num3:
#         return num2
#     return num3
# m= great(num1,num2,num3)
# print ( "The greatest of the numbers entered is :"+ str(m))
# print ( "The greatest of the numbers entered is :", m)

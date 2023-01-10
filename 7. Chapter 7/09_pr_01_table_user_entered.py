# # program to generate a table for user entered number(my method)
# num1= int(input ("enter the number to generate the table: \n"))
# for i in range (1,11):
#     print (num1,"x",i,"=",i*num1)
# print ("your table is complete")


# # program to generate a table for user entered number(harrys method)
# num1= int(input ("enter the number to generate the table: \n"))
# for i in range (1,11):
#     print (str(num1) + "x" + str(i) + "=" + str(num1*i))
# print ("done")


# program to generate a table for user entered number(harrys method) using f strings
num1= int(input ("enter the number to generate the table: \n"))
for i in range (1,11):
    print (f"{num1}x{i}={num1*i}")
print ("done")


# # my method to print tables from the first entered value till last entered value: using f strings
# num1= int(input ("enter the number to generate the table: \n")) # input taken from user
# num2= int (input(" Enter the last table to be displayed: \n")) # input taken from user
# while num1 <= num2:
#     print (f"The table {num1} is:" )
#     for i in range (1,11):
#         print (f"{num1}x{i}={num1*i}") # f strings is used
#     print (f"The table for {num1} is complete")
#     num1 = num1 + 1 # adding 1 to the original number  
# print ("done")



# no need of adding breaks
# if num1 == num2+1 :
#     break
    
##  % operator is used to divide the number and give out the remainder as an output.
# a=14
# b=5
# print (a%b)

# ## example for understanding the next problem
# for i in range (2,10):
#     print (i)



# #example error code - when else is inside the for loop:
# num= int (input ("enter the number:"))
# for i in range (2,num):  # Here if the num is 11 the range will search till 10 only. range is searched one number lesser than that entered in the bracket
#     if (num%i==0): #  % operator is used to divide the number and give out the remainder as an output.
#         print (i)
#         print (f"The number is not a prime number as it is divisible by {i}")
#         break
#     else: 
#         print (" the number is a prime")
#         print (i)

# ## if 'else' is inside the 'for loop': it checks for every number starting with 2 and /
# # returns that the number is prime if it is not divisible by 2 
# # example if the number is 25 it will print the number to be prime when it is divided by 2 
# # again it will print the number to be prime when divided by 3 and 4 and the finally when it is divided by 5 
# # it will retun that the number is prime number as it is exactly divided by 5.
# # so to avoid this scenario we can stop the printing of " this number is a prime number " by taking the /
# # else out of the for loop. So now the loop will check for all the numbers in the range and will print the number /
# # to be a prime only when it completely checks the range.


# correct method: When else is outside the for loop (along with exception handled for 0 and 1 )
num= int (input ("enter the number:"))
if (num == 0):
    print (f'The number is not a prijme number')
elif (num == 1):
    print (f'The number is not a prijme number')
else:
    for i in range (2,num):  # Here if the num is 11 the range will search till 10 only. range is searched one number lesser than that entered in the bracket
        if (num%i==0): #  % operator is used to divide the number and give out the remainder as an output.
            print (i)
            print (f"The number is not a prime number as it is divisible by {i}")
            break
    else: 
        print (" the number is a prime") # if I enter the num as 1 it will print 'the number to be a prime number' as it it out of the range and the for loop is skipped 


# # Harrys method": 1 and 0 shows as prime; no exception handling given.
# num= int (input ("enter the number:"))
# prime = True
# for i in range (2,num):  
#     if (num%i==0):
#         prime = False
#         break
# if prime:
#     print (" the number is a prime")
# else: 
#     print (f"The number is not a prime number as it is divisible by {i}")
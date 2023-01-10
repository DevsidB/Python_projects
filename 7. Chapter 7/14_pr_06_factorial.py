# # factorial of entered number using while loop
# digit= int(input(" enter the number of digits you want to sum : \n"))
# count = 1
# a=digit
# while (count<=a) :
#     digit = digit * count
#     count = count + 1
#     if (count==a):
#         break
# print (digit)

# factorial using for loop
n= int(input(" enter the number of digits you want to sum : \n"))
for i in range (1,n):
    n = n*i 
print (n)

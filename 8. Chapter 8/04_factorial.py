## My method- both are same same methods- here print is inside the def
n= int(input(" Enter the number to find the factorial: "))
def factorial_iter(n):
    product = 1
    for i in range (n):
        product = product * (i+1)
    print (product)
factorial_iter(n)

# ##  Harry method- both are same same methods- here print is outside the def
# n= int(input(" Enter the number to find the factorial: "))
# def factorial_iter(n):
#     product = 1
#     for i in range (n):
#         product = product * (i+1)
#         return (product)   
# print (factorial_iter(n))

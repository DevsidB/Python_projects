# a=7
# def star_func(n):
#     for i in range (n ,0,-1):
#         print ("*" * n)
#         n=n-1
# star_func(a)

a=7
def star_func(n):
    for i in range (n):
        print ("*" * (n-i))
star_func(a)
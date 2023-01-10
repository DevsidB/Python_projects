# A function written inside a function that calls for itself 

def factorial(n=4):  ##takes in a default value n=4
    if n==0 or n==1:
        return 1
    return n * (factorial(n-1))
print (factorial())
#---------------------------------------------------------------
# return n * factorial(n-1)
# This will return
# 5 x factorial (4)
# 5 x (4 x factorial (3))
# 5 x 4 x (3 x factorial (2))
# 5 x 4 x 3 x (2 x factorial (1))
# 5 x 4 x 3 x 2 x (1)   ---------------as factorial 1 will return 1 as handled in if statement
#---------------------------------------------------------------

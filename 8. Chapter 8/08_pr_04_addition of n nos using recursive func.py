num1= 6
def add(n):
    if n==1:                # removal of if function may cause recursive error 
        return 1
    return (n + add(n-1))   # recursive functions works with if only. 
print (add(num1))
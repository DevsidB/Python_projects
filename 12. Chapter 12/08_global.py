a = 54 # Global variable
def func1():
    global a # <1> using global keyword uses the same global variable without creating another instance.
    # print(f"Print statement 1: {a}") # <1>d<2>d or <1>e<2>d  cant print if global is not specified in func and value of local variable is assigned after this line.'a' referenced before assignment error. 
    a = 8 # <2> Local Variable if global keyword is not used
    print(f"Print statement 2: {a}")

func1()
print(f"Print statement 3: {a}") # <1> global variable changes on using global keyword inside a function.

'''will print the global variable if global keyword is not used in funct. 
Else it will update the value of the global variable to the new value of local variable specified in the func.'''
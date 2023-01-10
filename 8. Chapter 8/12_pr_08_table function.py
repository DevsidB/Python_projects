# program to generate a table using function
num1= int(input ("enter the number to generate the table: \n"))
num2= int(input ("enter the number to generate the table: \n"))
def table(n):
    for i in range (1,11):
        print (f"{n}x{i}={n*i}")
table(num1)
table(num2)


# program to generate a table for user entered number(harrys method) using f strings
num1= int(input ("enter the number to generate the table: \n"))
for i in range (10,0,-1):
    print (f"{num1}x{i}={num1*i}")
print ("done")
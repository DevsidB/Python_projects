# program to generate a table for user entered number(harrys method) using f strings
num1= int(input ("enter the number to generate the table: \n"))
count = 1
while count <= 10:
    print (f"{num1}x{count}={num1*count}")
    count = count + 1

print ("done")

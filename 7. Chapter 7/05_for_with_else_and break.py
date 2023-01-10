# my trial example
num1=int(input('enter the desired number1:\n'))
num2=int(input('enter the desired number2:\n'))
num3=int(input('enter the desired number3:\n'))
num4=int(input('enter the desired number4:\n'))

numset= [num1,num2,num3,num4]
numset.sort()
print (numset)

for sanket in range (101):
    print (sanket)
    if sanket == numset[3]:
        break

else :
    print ('no number less than 100 found')
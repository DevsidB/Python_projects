try: 
    a= int (input(" Enter a number 1 :"))
    b= int (input(" Enter a number 2:"))
    num = a/b
    print (f" Result : {num}")
except ZeroDivisionError as e:
    print (" Please do not put thee value of 'num2' as 'zero'")
try:
    a = int(input("Enter any number: "))
    c = 1/a
    print(c)

except ValueError as e:
    print(f"Please Enter a valid value. {e} ") 
    exit() # <1>

except ZeroDivisionError as e:
    print(f"Make sure you are not dividing by 0 {e} ") 
    

print("Thanks for using this code!") # will print for Zero D err. Wont print for value error because of exit <1>
print (__name__)   
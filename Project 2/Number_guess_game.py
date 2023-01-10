import random
number = random.randint(1,10)
list = []

while True:
    
    usernum= int (input ("Enter any number between 1 to 10: "))
    list.append(usernum)

    if number > usernum:
        print (" Try entering a larger number")
    elif number < usernum:
        print (" Try entering a smaller number")
    else:
        print (f"You win. You entered the correct number {number}\n You took {len(list)} chances to guess.")
        print (list)
        break
    

    



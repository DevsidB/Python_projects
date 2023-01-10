## Adding counter to the game ---self task is remaining ******************
import random

def gamewin(you,comp):
    if you==comp:
        return None
    elif comp=="s":
        if you == "w":
            return False
        elif you == "g":
            return True
    elif comp == "w":
        if you== "g":
            return False 
        elif you == "s":
            return True
    elif comp== "g":
        if you == "s":
            return False 
        elif you == "w":
            return True
while True:
    print ("Comp Turn: Enter Snake(s), Water(w) or Gun(g):")
    you = input ("Your Turn : Enter Snake(s), Water(w) or Gun(g): ")

    rand= random. randint(1,3)
    if rand == 1:
        comp= "s"
    elif rand== 2:
        comp = "w"
    elif rand==3:
        comp= "g"

    print (f"You entered {you}")
    print (f"Computer entered {comp}")

    a= gamewin(you, comp)

    if a == None:
        print ("The game is a Tie!")
    elif a== True:
        print ("You Win !")
    elif a == False:
        print ("You Lose! ")
    




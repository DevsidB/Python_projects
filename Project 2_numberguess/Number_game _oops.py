import random
number = random.randint(1,100)
# print (number)
class Game:
    import random
    number = random.randint(1,10)

    def __init__(self):
        print ("Loading...The game is started")

    def play_game(self):
        list= []
        while True:
            
            usernum= int (input ("Enter any number between 1 to 100: "))
            list.append(usernum)

            if number > usernum:
                print ("Try entering a larger number")
            elif number < usernum:
                print ("Try entering a smaller number")
            else:
                print ("\n")
                print (f"******You win. You entered the correct number: {number}******\n**************You took {len(list)} chances to guess.**************")
                print (list)

                with open ("highscore.txt", "r") as f:
                    highscore= (f.read())
                    print (highscore)

                if highscore=='':
                    print ("-----------------------------------------------------------------------------------")
                    print (f"*****Hey! You just broke an High Score! You took {len(list)} chances to guess.****")
                    print ("-----------------------------------------------------------------------------------")
                    with open ("highscore.txt", "w") as f:
                        f.write(str(len(list)))

                elif (int(len(list))<int(highscore)):
                    print ("-----------------------------------------------------------------------------------")
                    print (f"****Hey! You just broke an High Score! You took {len(list)} chances to guess.****")
                    print ("-----------------------------------------------------------------------------------")
                    with open ("highscore.txt", "w") as f:
                        f.write(str(len(list)))
                
                break

        

atu=Game()
atu.play_game()

    



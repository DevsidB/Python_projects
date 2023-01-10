class Train():

    def __init__(self, name, fare, seats ):
        self.name= name
        self.fare= fare
        self.seats=seats

    def getStatus(self):
        print (f"The name of the train is  {self.name}")
        print (f"The seats available in the train are  {self.seats}")
        
    def getFare(self):
        print (f"The fare for your train is {self.fare}")

    def bookTicket(self):
        if self.seats>0:
            print (f"Ticket booked for {self.name}. Your ticket no is : {self.seats}")
            self.seats-=1
        else :
            print ("No seats available. Please try for tatkaal booking !")
        

shatabdi = Train("Janashatabdi", 1000,50)

shatabdi.getStatus()
shatabdi.getFare()
Train.getStatus(shatabdi)
shatabdi.bookTicket()
shatabdi.getStatus()
shatabdi.bookTicket()
shatabdi.getStatus()
shatabdi.bookTicket()
shatabdi.getStatus()
shatabdi.bookTicket()


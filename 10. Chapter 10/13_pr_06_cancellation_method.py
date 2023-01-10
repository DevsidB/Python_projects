class Train():

    # seats = {4,3,2,1,8,8,7}
    # lenseats= int(len(seats))

    def __init__(self, name, fare,seats):
        self.name= name
        self.fare= fare
        self.seats= seats

    def getStatus(self):
        print (f"The name of the train is  {self.name}")
        print (f"The seats available in the train are  {len(self.seats)}")
        print (f"You can select the seats fom seat number:  {self.seats}")
        
    def getFare(self):
        print (f"The fare for your train is {self.fare}")

    def bookTicket(self):
        if len(self.seats)>=1:
            print (f"Ticket booked for {self.name}. Your ticket no is : {self.seats.pop()}")
            print (self.seats)
            # print (len(self.seats))

        else :
            print ("No seats available. Please try for tatkaal booking !")
    
    def cancelTicket(self,seatNo):
        print (f"You have requested to cancel the seat for seat Number {seatNo}")
        if seatNo not in self.seats:
            self.seats.add(seatNo)
            print (f"Your seat is cancelled for seat Number : {seatNo}")
        else: 
            print ("The seat Number you entered is wrong. Please check the entered Number.")
        print (self.seats)

        

shatabdi = Train("Janashatabdi", 1000, {1,3,2,4,6,5,7,8,10,3})
kokankanya = Train("Kokan Kanya", 500, {56,78,45,54,53,52,51})

kokankanya.bookTicket()

# Train.getStatus(shatabdi) ## Alternative method to get the status.
# shatabdi.bookTicket()
# shatabdi.getStatus()
# shatabdi.bookTicket()
# shatabdi.getStatus()
# shatabdi.bookTicket()
# shatabdi.getStatus()
# shatabdi.bookTicket()
# shatabdi.getStatus()
# shatabdi.bookTicket()
# shatabdi.getStatus()
# shatabdi.bookTicket()
# shatabdi.getStatus()
# shatabdi.bookTicket()
# shatabdi.getStatus()
# shatabdi.bookTicket()
# shatabdi.cancelTicket(4)
# shatabdi.cancelTicket(1)
# shatabdi.cancelTicket(3)
# shatabdi.cancelTicket(6)
# shatabdi.cancelTicket(4)
# shatabdi.cancelTicket(1)
# shatabdi.cancelTicket(3)
# shatabdi.cancelTicket(6)
# shatabdi.bookTicket()
# shatabdi.getStatus()

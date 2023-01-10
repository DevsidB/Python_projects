class Programmer:
    company= "Microsoft"
    def __init__(self,name,product):
        self.name = name
        self.product = product

    def getDetails(self):
        print (f"The name of the company is {self.company} and the programmer {self.name} works for {self.product}")
    
sid= Programmer("Sid", "Skype")
bob= Programmer ("Bob", "Network")
ajay = Programmer("Ajay", "Sql")

sid.getDetails()
bob.getDetails()
ajay.getDetails()


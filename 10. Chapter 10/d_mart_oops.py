class Dmart:

    def __init__(self,name,price,quantity):

        self.name=name
        self.price=price
        self.quantity= quantity
    
    def getDetails(self):
        print (f"The name of product is {self.name}")
        # print (f"The price of product is {self.price}")
        print (f"The quantity of product is {self.quantity}")
    
    def addProduct (self,numberof):
        self.quantity=self.quantity+ numberof

    def sellProduct (self,numberof):
        if self.quantity>=1:
            self.quantity=self.quantity-numberof
        else:
            print ("Quantity is not sufficient")


maggi= Dmart("maggi", 15,10)
maggi.getDetails()
maggi.addProduct(5)
maggi.getDetails()
maggi.sellProduct(2)
maggi.getDetails()
maggi.sellProduct(10)
maggi.getDetails()
maggi.sellProduct(3)
maggi.getDetails()
maggi.sellProduct(3)
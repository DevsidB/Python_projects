
class RailwayForm:
    formType = "RailwayForm"
    train= "shatabdi"
    name= "Somebody"
    def printData(me): # using self is not mandatory, any other variable can be used here. 
        print(f"Name is {me.name}")
        print(f"Train is {me.train}")
        print(f"Address is {me.address}")

harrysApplication = RailwayForm()
# harrysApplication.name = "Harry"
# harrysApplication.train = "Rajdhani Express"
harrysApplication.address= "Delhi"
harrysApplication.printData()
# class Calculator:

#     def __init__(self,number):
#         self.number=number

#     def square(self):
#         squared= self.number*self.number
#         print (f"The square of the number is {squared} : ")

#     def cube(self):
#         cubed= self.number*self.number*self.number
#         print (f" The cube of the number is : {cubed} ")

#     def squareRoot(self):
#         squarerooted= self.number**(1/2)
#         print (f"The square root of the number is :{squarerooted}")
    
# calculate= Calculator(2)
# calculate.square()
# calculate.cube()
# calculate.squareRoot()


##Other Method
class Calculator:
    def __init__(self,num):
        self.number= num

    def square(self):
        print (f"The value of {self.number} square is : {self.number**2}")

    def squareRoot(self):
        print (f"The value of {self.number} squareroot is : {self.number**3}")

    def cube(self):
        print (f"The value of {self.number} cube is : {self.number**0.5}")

a= Calculator(9)
a.square()
a.squareRoot()
a.cube()






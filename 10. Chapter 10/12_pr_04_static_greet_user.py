# class Calculator:
#     def __init__(self,num):
#         self.number= num
#         print ("Hello !")

#     def square(self):
#         print (f"The value of {self.number} square is : {self.number**2}")

#     def squareRoot(self):
#         print (f"The value of {self.number} squareroot is : {self.number**3}")

#     def cube(self):
#         print (f"The value of {self.number} cube is : {self.number**0.5}")

# a= Calculator(9)
# a.square()
# # a.squareRoot()
# # a.cube()


class Calculator:
    # def __init__(self,):
    #     self.number= num

    def square(num1):
        print (f"The value of {num1} square is : {num1}")

    def squareRoot(self):
        print (f"The value of {self.number} squareroot is : {self.number**3}")

    def cube(self):
        print (f"The value of {self.number} cube is : {self.number**0.5}")

    @staticmethod
    def greet(name):
        print (f"Hello {name}, WELCOME TO THE CALCULATOR !")

num1 = 9
a= Calculator()
a.greet("sid")
# a.square(num1) ## This will give 2 positional arguments--> got converted to --> Calculator.square(a,num1)
Calculator.square(num1)
# a.squareRoot() 
# a.cube()
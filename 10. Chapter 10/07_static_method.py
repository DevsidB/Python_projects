class Employee: ## This is a class
    company = "Google" # This is a class Variable

    def getSalary(self, signature, large1,large2): #This is a method /function
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}\n{large1}\n{large2}")

    @staticmethod # This is a static method
    def greet(name):
        print(f"Good Morning,{name} Sir")

    @staticmethod
    def time():
        print("The time is 9AM in the morning")

sid=Employee() ## This is an object assigned to a class. Here 'sid' is an object
harry = Employee() 

sid.salary= 2000000  # This is =-->> Object variable/object property/object attribute
harry.company = "Amazon" ## Also known as instance attribute/instance variable
harry.salary = 100000

harry.getSalary("Thanks!","we will meet soon","hope that helps") # Employee.getSalary(harry)
harry.greet("Sid") # Employee.greet()
harry.time() ## This is a function calling/method calling--> calling a blank method with object i.e without assigning any variable to be printed.
# sid.getSalary("Regards", "Have a nice day","Hope I assisted you well!")


# class Employee:
#     company = "Google"
#     def getSalary(me):
#         print(f"Salary for this employee working in {me.company} is {me.salary}")

# harry = Employee()
# harry.salary = 100000
# harry.getSalary() # Employee.getSalary(harry)
company= "Amz"
salary=1000
class Employee:
    company = "Google"
    salary = 10

    def getSalary(self):
        print(f"Salary for this employee working in {self}") # is {self.salary}")

    def empty():
        print("This is an empty funtion without static command and self")

    @staticmethod
    def staticEmpty():
        print("This is an empty funtion with static command")

harry = Employee()
sid= Employee()
harry.salary = 100000  ##priority is given to the object attribute first and then to the class attribute.
sid.salary=50000
amount=90000

# harry.getSalary() # Employee.getSalary(harry)
# sid.getSalary() #this gets converted to the syntax mentioned below
Employee.getSalary("sid") # another way of writing the syntax mentioned above

Employee.getSalary(amount) ## Self is used to avoid the positional argument. It takes the attributes inside the class to satisfy the conditions incase if object attribute is not provided to avoid the error. 
Employee.empty()  # This can print an empty function without static and self but the below wont work and takes positional argument 1 given.
# sid.empty() #Returns positional argument as 1 argument is given ->> same as Employee.empty(sid) as nothing should be substituted in the bracket.
sid.staticEmpty() ## Static function enables us to use the function for an object which cannot be done for a normal function inside a class as mentioned in the above line. 
Employee.staticEmpty() ## Executing a static function without an argument/object/variable is same as executing it with an object.
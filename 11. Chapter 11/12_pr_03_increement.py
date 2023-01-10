class Employee:
    salary= 50000
    increement = 2500

    @property 
    def salaryAfterIncreement(self):
        return self.salary + self.increement
    
    @salaryAfterIncreement.setter #{1}
    def salaryAfterIncreement(self,val):
        self.increement = val -  self.salary # This is valid
        self.salary = val - self.increement # This is valid
        # val = self.increement + self.salary # this is not valid

e = Employee()

print (e.salaryAfterIncreement)
print (e.salary) # {1--} shows class salary if setter disabled
print(e.increement) #{1--} shows class increement if setter disabled
e.salaryAfterIncreement= 60000 # {1} can be set this way only once a setter is used

print (e.salaryAfterIncreement)
print (e.salary) # {1--} shows class salary if setter disabled
print(e.increement) #{1--} shows class increement if setter disabled

print (Employee.salary)
print (Employee.increement)
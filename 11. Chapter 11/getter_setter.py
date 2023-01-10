class Employee:
    ename= "Sid"
    e_salary= 1000

    @property
    def name(self):
        return self.ename

    @name.setter
    def name(self,val):
        self.ename= val

    @property
    def salary(self):
        return self.e_salary

    @salary.setter
    def salary(self,val):
        self.e_salary= val


e=Employee()

print(e.name)
e.name = "Bob"
print(e.name)
print(e.ename)
print(Employee.ename)

# print(e.e_salary)
# e.salary=2000
# print(e.salary)
# print(e.e_salary)

# class Sample:
#     a = 2
#     def value(self):
#         print (f"The value you entered is : {self.a}")

# object= Sample()
# object.a= 0 ## class attribute
# object.value()


##other method
class Sample:
    a = 2
    print (a) # This will print line 20 2 times. Also it will initially print 'a' inside the class and then replace it with instance variable and print the other one.

object= Sample()
object.a= 0 # instance attribute
Sample.a= "Sid" ## This will change the class attribute

print (Sample.a) ## changing instance attribute doesn't change a class attribute.
# print (object.a) 
Sample.a ## When a class is called it doesn't execute itself but function does.


# class Number:
#     def __init__(self, num1,num2):
#         self.num1 = num1
#         self.num2=num2

#     def __add__(self,num3):
#         print("Lets add")
#         # return 300
#         return self.num1 + self.num2

#     # def __add__(self,num3):
#     #     print("Lets ")
#     #     # return 300
#     #     return self.num1 + num3.num1
    


# n1 = Number(1,5)
# n2 = Number(1,3)
# n3= Number(3,5)
# # print (n2+1)## Whenever + symbol is used with any of the object --> __add__ function returns values.
# print (n1+1)
# # print (n1+n2)
# # print (n2+n3)

class Number:
    def __init__(self, num1):
        self.num1 = num1

    def __add__(self,num2):
        print("Lets add")
        # return 300
        return self.num1 + num2.num1

    # def __add__(self,num3):
    #     print("Lets ")
    #     # return 300
    #     return self.num1 + num3.num1
    


n1 = Number(6)
n2 = Number(1)
n3= Number(3)
# print (n2+1)## Whenever + symbol is used with any of the object --> __add__ function returns values.
print (n3+n2)
# print (n1+n2)
# print (n2+n3)
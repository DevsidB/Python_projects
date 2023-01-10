class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, num2): ## Here add enables us to use + operator which is an inbuilt function.
        print("Lets add")
        print (self.num)                   
        print (num2.num)
        return self.num + num2.num ## Here the eoprator can be changed accordingly
     

    def __mul__(self, num3): ## Here mul enables us to use * operator which is an inbuilt function.
        print("Lets multiply")
        return self.num + num3.num ## Here the eoprator can be changed accordingly

n1 = Number(4)
n2 = Number(6)
n3= Number(8)
sum = n2 + n3
# mul = n1 * n2
print(sum)
# print(mul)
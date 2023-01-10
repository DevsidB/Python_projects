class Vector:
    def __init__(self, vec):
        self.vec= vec
    
    def __str__(self):
        str= ""
        # count = 0
        for i in range (len(self.vec)):
            str+= f"{self.vec[i]}a{i} + "
        return str[:-3]

    def __add__(self,vec2):
        newList= []
        for i in range (len(self.vec)):
            newList.append (self.vec[i] + vec2.vec[i])
        return Vector(newList)

    def __mul__(self,vec2):
        sum=0
        for i in range (len(self.vec)):
            sum += (self.vec[i] * vec2.vec[i])
        return sum


v1= Vector([2,3,4,5])
v2= Vector([5,6,-7,1])
# print (v1.__str__())

print (v1+v2)
print (v1*v2)
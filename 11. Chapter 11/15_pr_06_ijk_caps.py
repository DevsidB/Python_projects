class Vector:
    def __init__(self, vec):
        self.vec= vec
    
    def __str__(self):
        str=""
        caps= ["i","j","k","l"]
        for i in range (len(self.vec)):
            str += f"{self.vec[i]}{caps[i]} + "
        return str[:-3]
        
    def __add__(self,vec2):
        if len(self.vec)==len(vec2.vec):

            newList= []
            for i in range (len(self.vec)):
                newList.append (self.vec[i] + vec2.vec[i])
            return Vector(newList) # This command prints the addition of vectors. Code runs from the very beginning after this line as values of newlist as an input parameter to Vector class. 
        else :
            return "The length of two vectors does not match."

    def __len__(self): #{1}
        return len (self.vec)

v1= Vector([2,3,8])
v2= Vector([2,0,6])
print (v1) # runs the __str__dender
print (v2)
print (v1+v2) # runs the __add__ dender

# print (len(v1)) # can be used only when the len dender method is used in a class.
# print (len(v1.vec)) # can be used to call a length without using dender method.
# print (len(v2.vec))

# v2= Vector([5,6,-7,1])
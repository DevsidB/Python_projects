class V2d:
    def __init__(self,i,j):
        self.i=i
        self.j= j
        # {1} print (f"{self.i}i + {self.j}j") # This line prints right after tye class variable is defined. No need to call for the function.
    def __str__(self):
        # print (f"{self.i}i + {self.j}j") ## {2} This line is printed once the function is called in print as 'str' is used. No need to call the function. Just use the object name inside print cmd.
        return f"{self.i}i + {self.j}j" # {3} For printing the object as a variable. Can only be used under '__str__' dender method.

class V3d(V2d):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k= k
        
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"

v2=V2d(2,3) #{1}
v3= V3d(4,5,6)
# v2.__str__() # {2} calling a dender function.
print (v2) # {3}
print (v3) # {3}


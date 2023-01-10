# (a+bi)(c+di) = (ac−bd) + (ad+bc)i

class Complex():
    def __init__(self,i,j):
        self.i= i
        self.j= j
    
    def __add__(self,c):
        addreal= self.i + c.i
        addimg= self.j + c.j
        return Complex (addreal,addimg)
        # return f"{addreal} + {addimg}i"

    def __mul__(self,c):
        mulreal= (self.i * c.i) - (self.j * c.j)
        mulimg= (self.i* c.j) + (self.j * c.i)
        return Complex(mulreal, mulimg)

    # def __str__(self):
    #     return f"{self.i} + {self.j}i" # This will print the values like (5+ -10i) to avoid this use the string function with if else below.

    def __str__(self):
        if self.j<0:
            return f'{self.i} - {-self.j}i' #'''in cases where imaginary part is -ve without this statement  
                                               # will print as (2 - -5i) or (2+ -5i). So to avoid this we will
                                               # remove the minus sign that comes with the imaginary part.''' 
        else:
            return f"{self.i} + {self.j}i"
        

c1= Complex(-5,-10)
c2= Complex(-2,-50)
print (c1+c2)
print (c1*c2)
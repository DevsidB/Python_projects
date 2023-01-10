
class C2dVec:
    def __init__(self, i, j):
        self.icap = i
        self.jcap = j
        print( f"{self.icap}i + {self.jcap}j")
    # def __str__(self):
    #     return f"{self.icap}i + {self.jcap}j"
        
class C3dVec(C2dVec):
    pass
    
    
v2d = C2dVec(1, 3)
v3d = C3dVec(1, 9)
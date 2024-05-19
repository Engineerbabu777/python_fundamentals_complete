


class A:
    x = None
    
    def __init__(self,x=10):
        self.x = x
        
    
    def getter(self):
        print(f"x:{self.x}")
        return self.x
    

obj = A(59)
obj.getter()

from Field import FieldElement

class ECPoint():
    def __init__(self, x=None, y=None, a=None, b=None, p=None, use_defaults=True):    
        """
        Using defaults will override the provided value(s) is any.
        """
        self.use_defaults = use_defaults

        # Handling the Elliptic Curve
        if use_defaults:
            self.p = (2**256 - 2**32 - 2**9 - 2**8 - 2**7 - 2**6 - 2**4 - 1)
            self.a = FieldElement(0, self.p, self.use_defaults)
            self.b = FieldElement(7, self.p, self.use_defaults)
        else:
            self.p = p
            self.a = FieldElement(a, self.p, self.use_defaults)
            self.b = FieldElement(b, self.p, self.use_defaults)
        
        # Checking for Curve Validity
        if not self.valid_curve():
            raise ValueError("Curve has singular Points. Not valid!")
        
        
        # Checking Point validity
        if x == 'inf' and y == 'inf':
            self.x = None
            self.y = None
        else:
            try:
                self.x = FieldElement(x, self.p, self.use_defaults)
                self.y = FieldElement(y, self.p, self.use_defaults)
            except:
                raise ValueError("x and y must be both valid or both 'inf'")

        if not self.point_on_curve():
            raise ValueError("Point Specified must be on the Curve")
            
    def valid_curve(self):
        return bool(
            FieldElement(4, self.p, self.use_defaults) * self.a**3 + 
            FieldElement(27%self.p, self.p, self.use_defaults) * self.b**2
        )
    
    def point_on_curve(self):
        if self.x == None and self.y == None:
            return True
        else:    
            return (
                self.y**2 == 
                self.x**3 + self.a*self.x + self.b
            )
    
    def __add__(self, other):
        pass

    def __mul__(self, other):
        pass

point1 = ECPoint('inf', 'inf')
point2 = ECPoint(x=4, y=8, use_defaults=False, a=0, b=0, p=107)
print(type(FieldElement(5, 7, False)) == type(FieldElement(0, 1, False)))
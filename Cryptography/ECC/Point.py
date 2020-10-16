from Field import FieldElement

class ECPoint():
    def __init__(self, x=None, y=None, a=None, b=None, p=None, use_defaults=True, internal=False):    
        """
        Using defaults will override the provided value(s) is any.
        """
        self.use_defaults = use_defaults

        # Handling the Elliptic Curve
        if use_defaults:
            self.p = (2**256 - 2**32 - 2**9 - 2**8 - 2**7 - 2**6 - 2**4 - 1)
            if not internal:
                self.a = FieldElement(0, self.p, self.use_defaults)
                self.b = FieldElement(7, self.p, self.use_defaults)
            else:
                self.a = a
                self.b = b
        else:
            self.p = p
            if not internal:
                self.a = FieldElement(a, self.p, self.use_defaults)
                self.b = FieldElement(b, self.p, self.use_defaults)
            else:
                self.a = a
                self.b = b

        # Checking for Curve Validity
        if not self.valid_curve():
            raise ValueError("Curve has singular Points. Not valid!")
        
        
        # Checking Point validity
        if x == 'inf' and y == 'inf':
            self.x = None
            self.y = None
        else:
            try:
                if not internal:
                    self.x = FieldElement(x, self.p, self.use_defaults)
                    self.y = FieldElement(y, self.p, self.use_defaults)
                else:
                    self.x = x
                    self.y = y
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
        try:
            if self.a != other.a or self.b != other.b or self.p != other.p:
                raise TypeError("Points do not lie on the same curve")
        except AttributeError:
            raise AttributeError("Points must both be objects")
        
        # checking either x or y is sufficient, since the point is only accepted
        # if both are valid or both are 'inf'
        if self.x == None and other.x != None:
            return other
        # dont care if self is None or not, if other is None, we return self.
        # in essence, combined the 2 cases
        elif other.x == None:
            return self
        
        # the actual addition takes place now-onwards
        if self.x != other.x:
            m = (self.y-other.y)/(self.x-other.x)
        else:
            if self.y:
                m = (FieldElement(3, self.p, self.use_defaults)*self.x**2 + self.a)/(FieldElement(2, self.p, self.use_defaults)*self.y)
            else:
                return self.__class__('inf', 'inf', self.a, self.b, self.p, self.use_defaults, internal=True)

        x = m**2 - self.x - other.x
        y = m*(self.x - x) - self.y
        return self.__class__(x, y, self.a, self.b, self.p, self.use_defaults, internal=True)


    def __mul__(self, other):
        pass

point1 = ECPoint('inf', 'inf', use_defaults=False, a=0, b=0, p=107)
point2 = ECPoint(x=4, y=8, use_defaults=False, a=0, b=0, p=107)
point3 = ECPoint(x=9, y=27, use_defaults=False, a=0, b=0, p=107)
point4= ECPoint(x=9, y=27, use_defaults=False, a=0, b=0, p=97)
# print(type(FieldElement(5, 7, False)) == type(FieldElement(0, 1, False)))

point5 = point2+point2
print(point5.x);print(point5.y)

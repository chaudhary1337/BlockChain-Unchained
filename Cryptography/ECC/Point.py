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
            self.a = 0
            self.b = 7
        else:
            self.p = p
            self.a = a
            self.b = b

        # Checking for Curve Validity
        if not self.valid_curve():
            raise ValueError("Curve has singular Points. Not valid!")
         
        # Checking Point validity
        if x == 'inf' and y == 'inf':
            self.x = None
            self.y = None
        elif x != 'inf' and y != 'inf':
            self.x = x
            self.y = y
        else:
            raise ValueError("x and y must be both valid or both 'inf'")

        if not self.point_on_curve():
            raise ValueError("Point Specified must be on the Curve")
            
    def valid_curve(self):
        return bool(4 * self.a**3 + 27 * self.b**2)
    
    def point_on_curve(self):
        if self.x == None and self.y == None:
            return True
        else:
            return (self.y**2 == self.b + self.a*self.x + self.x**3)

    def __repr__(self):
        if self.x is None:
            return 'Point(infinity)'
        elif isinstance(self.x, FieldElement):
            return f"Point({self.x},{self.y})\ta, b: {self.a}, {self.b}\tover: Z({self.p})"
        else:
            return f"Point({self.x},{self.y})\ta, b: {self.a}, {self.b}"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y \
            and self.a == other.a and self.b == other.b

    def __ne__(self, other):
        return not (self == other)

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
                m = (3*self.x**2 + self.a)/(2*self.y)
            else:
                return self.__class__('inf', 'inf', self.a, self.b, self.p, self.use_defaults)

        x = m**2 - self.x - other.x
        y = m*(self.x - x) - self.y
        return self.__class__(x, y, self.a, self.b, self.p, self.use_defaults)

    def __mul__(self, other):
        pass

# point1 = ECPoint('inf', 'inf', use_defaults=False, a=0, b=7, p=223)
# point2 = ECPoint(x=FieldElement(47, 223), y=FieldElement(71, 223), use_defaults=False, a=0, b=7, p=223)
# point3 = ECPoint(x=FieldElement(17, 223), y=FieldElement(56, 223), use_defaults=False, a=0, b=7, p=223)

# point4 = point3+point2    

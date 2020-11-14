from Field import FieldElement

class ECPoint():
    def __init__(self, x=None, y=None, a=None, b=None, p=None, use_defaults=True):    
        """
        inputs:
            x: x coordinate
            y: y coordinate
            a: the coefficient of x in the function
            b: the constant term in the function
            p: the prime number over which the fields are defined
            use_defaults:
                Using defaults will override the provided value(s) if any,
                exceot for x and y values. 
                and assign with secp256k1 standard (used in BitCoin).
        """
        self.use_defaults = use_defaults

        # Handling the Elliptic Curve
        if use_defaults:
            self.p = (2**256 - 2**32 - 2**9 - 2**8 - 2**7 - 2**6 - 2**4 - 1)
            self.a = 0
            self.b = 7
            if x == None and y == None:
                x = 0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798
                y = 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8
            if x != None and y == None:
                y = self.get_ordinate()
            self.x = FieldElement(x, self.p)
            self.y = FieldElement(y, self.p)
            self.n = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141
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

            if not self.is_point_on_curve():
                raise ValueError("Point Specified must be on the Curve")
            
            # if points are on the curve, we can get the order
            self.n = self.get_order()

    def __repr__(self):
        """
        How the point is represented when the point object is printed
        """
        if self.x is None:
            return 'Point(infinity)'
        elif isinstance(self.x, FieldElement):
            return f"Point(\n\tx: {self.x}\n\ty: {self.y}\n) a, b: {self.a}, {self.b}\tover: Z({self.p})"
        else:
            return f"Point({self.x},{self.y})\ta, b: {self.a}, {self.b}"

    def __eq__(self, other):
        """
        checks whether two points are equal
        """
        return self.x == other.x and self.y == other.y \
            and self.a == other.a and self.b == other.b and self.p == other.p

    def __ne__(self, other):
        """
        checks whether two points are NOT equal
        """
        return not (self == other)

    def __add__(self, other):
        """
        adds two point objects
        """
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
                m = (self.a + 3*self.x**2)/(2*self.y)
            else:
                return self.__class__('inf', 'inf', self.a, self.b, self.p, self.use_defaults)

        x = m**2 - self.x - other.x
        y = m*(self.x - x) - self.y
        return self.__class__(x, y, self.a, self.b, self.p, self.use_defaults)

    def __rmul__(self, coeff):
        """
        scalar multiplication using binary exponentiation
        """
        current = self
        result = self.__class__('inf', 'inf', self.a, self.b, self.p, self.use_defaults)

        while coeff:
            if coeff & 1:
                result += current
            current += current
            coeff >>= 1
        
        return result
    
    def valid_curve(self):
        """
        input:
            point object
        return:
            True or False
        checks whether the curve is non-singular;
        without cusps/self-intersections/isolated points
        """
        return bool(4 * self.a**3 + 27 * self.b**2)
    

    def is_point_on_curve(self):
        """
        input:
            point object
        return:
            True or False
        checks whether the point is on the curve or not
        """
        if self.x == None and self.y == None:
            return True
        else:
            return (self.y**2 == self.b + self.a*self.x + self.x**3)

    def get_order(self):
        """
        input:
            point object
        return:
            The order of the point
        Usually less than the size of the group itself
        """
        i = 2
        point = i*self
        while (point != self):
            i += 1
            point = i*self
        return i

    def get_ordinate(self):
        """
        Gets the y for a given x. Overrides the original y, if provided
        """
        # TODO: WRITE THIS SH!T. Its been pending for too long :(
        return 0

# point1 = ECPoint('inf', 'inf', use_defaults=False, a=0, b=7, p=223)
# point2 = ECPoint(x=FieldElement(47, 223), y=FieldElement(71, 223), use_defaults=False, a=0, b=7, p=223)
# point3 = ECPoint(x=FieldElement(17, 223), y=FieldElement(56, 223), use_defaults=False, a=0, b=7, p=223)

# point4 = point3+point2    
# print(point4)
# print(point2.get_order())
# print(ECPoint(use_defaults=True))
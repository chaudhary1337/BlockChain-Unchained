class FieldElement():
    """
    A class for converting vanilla elements to field elements
    """

    def __init__(self, value, prime):
        self.prime = prime
        # Handling Value range
        if 0 <= value < prime:
            self.value = value
        else:
            raise ValueError(f"The number {value} must be between 0 and {prime}.")

    def __eq__(self, other):
        try:
            return self.value == other.value and self.prime == other.prime
        except:
            return False
    
    def __repr__(self):
        return f"Value: {self.value}\t Over Field: Z({self.prime})"
    
    def __add__(self, other):
        try:
            if self.prime == other.prime:
                return self.__class__((self.value + other.value)%self.prime, self.prime)
            else:
                raise TypeError(f"Numbers belong to different fields {self.prime} and {other.prime}")
        except:
            raise TypeError("Not possible to Add")

    def __radd__(self, num):
        return self.__class__((self.value+num)%self.prime, self.prime)

    def __sub__(self, other):
        try:
            if self.prime == other.prime:
                return self.__class__((self.value - other.value)%self.prime, self.prime)
            else:
                raise TypeError(f"Numbers belong to different fields {self.prime} and {other.prime}")
        except:
            raise TypeError("Not possible to Subtract")
    
    def __mul__(self, other):
        try:
            if self.prime == other.prime:
                return self.__class__((self.value * other.value)%self.prime, self.prime)
            else:
                raise TypeError(f"Numbers belong to different fields {self.prime} and {other.prime}")
        except:
            raise TypeError("Not possible to Multiply")

    def __rmul__(self, coefficient):
        return self.__class__((self.value * coefficient)%self.prime, self.prime)

    def __pow__(self, other):
        try:
            other = other % (self.prime - 1)
            return self.__class__(pow(self.value, other, self.prime), self.prime)
        except:
            raise ValueError("Not possible to raise the Power")
    
    def __neg__(self):
        return -self.value % self.prime
            
    def __truediv__(self, other):
        try:
            return self.__pow__(-other)
        except:
            raise ValueError("Not able to access power function")

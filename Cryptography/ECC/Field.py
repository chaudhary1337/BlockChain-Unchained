class FieldElement():
    def __init__(self, value, prime):
        if self.check_prime(prime):
            self.prime = prime
        else:
            raise ValueError(f"The number {prime} is not a prime.")
        
        if 0 <= value < prime:
            self.value = value
        else:
            raise ValueError(f"The number {value} must be between 0 and {prime}.")

    def check_prime(self, value):
        i = 2
        while i*i <= value:
            if not(value % i):
                return False
            i += 1
        return True

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

    def __pow__(self, other):
        try:
            other = other % (self.prime - 1)
            return self.__class__(pow(self.value, other, self.prime), self.prime)
        except:
            raise ValueError("Not possible to raise the Power")
            
    def __div__(self, other):
        try:
            return self.__pow__(-other)
        except:
            raise ValueError("Not able to access power function")

if __name__ == "__main__":
    a = FieldElement(5, 23)
    b = FieldElement(3, 23)
    print("5+3\t:", a+b)
    print("3-5\t:", b-a)
    print("5*3\t:", a*b)
    print("5**3\t:", a**3)
    print("5**3*3\t:", a**3 * b)

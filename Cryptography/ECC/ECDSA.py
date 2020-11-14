import random
import hashlib
from Point import ECPoint

def inverse(num, mod):
    return pow(num, mod-2, mod)

class Person():
    def __init__(self, common=ECPoint(use_defaults=True)):
        self.common = common
        self.public_key, self.private_key = self.generate_key_pair()

    def generate_key_pair(self):
        """
        returns a public private key pair
        """

        # TODO: check for invalid points
        # TODO: Figure out: What does the above mean?
        d = random.randint(1, self.common.p-1)
        Qx = d*self.common.x
        Qy = ECPoint(x=Qx.value, y=None, use_defaults=True).y

        return ((Qx, Qy), d)

    def validate_public_key(self, public_key):
        """
        verifies other person's public key to be correct
        """
        # TODO: check for invalid points
        
        Qx = public_key[0].value
        Qy = public_key[1].value
        new_point = ECPoint(Qx, Qy, use_defaults=True)

        # The following are already checked for making a field element
        # assert 0 <= Qx < common.p
        # assert 0 <= Qy < common.p

        return new_point.is_point_on_curve()

    def sign(self, message):
        s = None
        r = None
        while not s:
            while not r:
                # getting a pseudo random number
                k = random.randint(1, self.common.p-1)

                # using the x coordinate of the new point
                r = (k*self.common.x).value % self.common.p
            
            # Done finding k and r
            
            e = int(hashlib.sha512(message.encode()).hexdigest(), 16)
            d = self.private_key
            s = ((e + d*r) % self.common.p * inverse(k, self.common.p)) % self.common.p
        
        return (r, s)

    def verify(self, sign, message, public_key):
        r, s = sign
        if r not in range(1, self.common.p):
            return 1
        if s not in range(1, self.common.p):
            return 2
        
        e = int(hashlib.sha512(message.encode()).hexdigest(), 16)

        w = inverse(s, self.common.p)
        u1 = e*w % self.common.p
        u2 = r*w % self.common.p

        X = (u1*self.common.x.value + u2*public_key[0].value) % self.common.p

        if not X:
            return 3

        return True if X == r else 4

if __name__ == "__main__":
    A = Person()
    # print(A.public_key)
    # print("="*80)
    # print(A.private_key)
    # print("="*80)
    # print(A.common)
    # print(A.validate_public_key(A.public_key))
    
    message = "hello"
    sign = A.sign(message)
    print(A.verify(sign, message, A.public_key))

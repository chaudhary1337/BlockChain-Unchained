import random
import hashlib
from Point import ECPoint

def inverse(num, mod):
    return pow(num, mod-2, mod)

class Person():
    def __init__(self, common=ECPoint(use_defaults=True), name="Sharma"):
        self.public_key, self.private_key = self.generate_key_pair()
        self.common = common

    def generate_key_pair(self):
        """
        returns a public private key pair
        """

        # TODO: check for invalid points
        d = random.randint(1, self.common.n-1)
        Qx = d*self.common.x
        Qy = Qx.get_ordinate()

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

        assert new_point.is_point_on_curve()

    def sign(self, message):
        s = None
        r = None
        while not s:
            while not r:
                # getting a pseudo random number
                k = random.randint(1, self.common.n-1)

                # using the x coordinate of the new point
                r = (k*self.common.x).value % self.common.n
            
            # Done finding k and r
            
            e = int(hashlib.sha512(message.encode()).hexdigest(), 16)
            d = self.public_key
            s = (e + d*r)*inverse(k, self.common.n) % self.common.n
        
        return r, s

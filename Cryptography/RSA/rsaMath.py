import random
from math import gcd as fast_gcd

def generate_prime(n=1024):
    """
    generates random prime numbers
    inputs:
        n: number of bits in the number
    return:
        a prime number
    """
    x = 2
    while not is_prime(x):
        x = random.randint(2**(n-1)+1, 2**n-1)
    return x

def get_totient(p, q):
    return (p-1)*(q-1)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def is_prime(n, k=8):
    """
    uses the miller rabin test. based on probabilities.
    worst case error bound: 4^(-k);
    that is 1/4^k chance its actually a composite number

    source: https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
    """
    if not (n > 3) or not (n & 1):
        return False
    
    # setup for miller rabin
    temp = n-1
    r = 0
    while not (temp & 1):
        temp >>= 1
        r += 1
    d = temp

    for _ in range(k):
        a = random.randrange(2, n-2)
        x = pow(a, d, n)

        if x == 1 or x == n-1:
            continue

        flag = False
        for __ in range(r-1):
            x = pow(x, 2, n)

            if x == n-1:
                flag = True
                break
        if flag:
            continue

        return False
    
    return True 

def mod_inv(x, mod):
    """
    Using Extended Euclidean Algorithm.
    Why not Fermat's Little Theorem? 
    mod is not guranteed to be prime!

    input:
        x: number whose modular inverse is to be found
        mod: inverse found wrt to x
    return:
        modular inverse, if found.
        None if not found.
    """
    t = 0; new_t = 1
    r = mod; new_r = x

    while new_r:
        q = r // new_r

        (t, new_t) = (new_t, t - q*new_t)
        (r, new_r) = (new_r, r - q*new_r)

    if r > 1:
        # invalid case
        return None
    else:
        # incase t becomes negative
        return (t+mod) % mod

def get_coprime(totient):
    x = random.randint(2, totient-1)
    while True:
        x = random.randint(2, totient-1)
        try:
            if fast_gcd(x, totient) == 1: break
        except:
            continue
    return x

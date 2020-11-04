from rsaMath import generate_prime, get_totient, get_coprime, mod_inv

def get_keys():
    """
    generates public private key pairs using the RSA Algorithm

    input:
        None
    output:
        a key pair
    """
    # step 1: generate the prime numbers pseudo-randomly
    print("getting primes ...", end="")
    p = generate_prime()
    q = generate_prime()
    print("Done.")

    # step 2: get the n; the number which we'll use to mod
    n = p*q

    # step 3: get the phi(n)
    print("getting totient ...", end="")
    totient = get_totient(p, q)
    print("Done.")

    # step 4: get the public key exponent
    print("getting public key ...", end="")
    e = get_coprime(totient)
    print("Done.")

    # step 5: get mod inv of e, wrt totient; the private key exponent
    print("getting private key ...", end="")
    d = mod_inv(e, totient)
    print("Done.")

    return ({'n': n, 'e': e}, {'p':p, 'q':q, 'd':d})

# if __name__ == "__main__":
#     public_key, private_key = get_keys()
#     print("Public Key exponent: ", public_key['e'])
#     print("Private Key inv: ", private_key['d'])
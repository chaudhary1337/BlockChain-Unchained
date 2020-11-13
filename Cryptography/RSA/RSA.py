from rsaMath import generate_prime, get_totient, get_coprime, mod_inv

def get_keys(debug=False):
    """
    generates public private key pairs using the RSA Algorithm

    input:
        debug:
            whether to print out each step of the generation or not
    output:
        a key pair
    """
    # step 1: generate the prime numbers pseudo-randomly
    if debug: print("getting primes ...", end="")
    p = generate_prime()
    q = generate_prime()
    if debug: print("Done.")

    # step 2: get the n; the number which we'll use to mod
    n = p*q

    # step 3: get the phi(n)
    if debug: print("getting totient ...", end="")
    totient = get_totient(p, q)
    if debug: print("Done.")

    # step 4: get the public key exponent
    if debug: print("getting public key ...", end="")
    e = get_coprime(totient)
    if debug: print("Done.")

    # step 5: get mod inv of e, wrt totient; the private key exponent
    # # NOTE: The algorithm says to use totient, but it does not work.
    # # only on using n, we get a correct response.
    if debug: print("getting private key ...", end="")
    d = mod_inv(e, totient)
    if debug: print("Done.")

    return ({'n': n, 'e': e}, {'p':p, 'q':q, 'd':d})

if __name__ == "__main__":
    public_key, private_key = get_keys(debug=True)
    
    m = 55
    x = public_key['e']
    y = private_key['d']
    mod = get_totient(private_key['p'], private_key['q'])
    n = public_key['n']

    print("Public Key: ", x)
    print("Private Key: ", y)
    print("Mod: ", m)
    if x*y % mod == 1:
        print("INVERSE CORRECT!")
    
    encrypted = pow(55, x, n)
    print(encrypted)
    decrypted = pow(encrypted, y, n)
    print(decrypted)

    if decrypted == m:
        print("ENCRYPTION/DECRYPTION CORRECT")

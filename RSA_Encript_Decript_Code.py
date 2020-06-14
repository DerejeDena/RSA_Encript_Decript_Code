print("\n\t Name: Dereje Dena ")
print("\n\t Digital Forensics ")


def multiplicative_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None


def isPrime(n, i=2):
    if n <= 2:
        return True if n == 2 else False
    if n % i == 0:
        return False
    if i * i > n:
        return True
    return isPrime(n, i + 1)


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def generate_keys(p, q):
    if not (isPrime(p) and isPrime(q)):
        print("\n\tError Both p and q must be prime numbers ")
    elif p == q:
        print("\n\tp and q cannot be the Same ")
    else:
        n = p * q
        phi = (p - 1) * (q - 1)

        # choose an integer e such thate and m are coprime

        print("Euler's function (totient) [phi(n)]: " + str(phi) + "\n")
        print("Choose an e from primes numbers:\n")
        e = int(input())
        d = multiplicative_inverse(e, phi)
        publicKey = (e, n)
        privateKey = (d, n)

        # using Euclid's algorithm to generate the private key
        g = gcd(e, phi)

        d = multiplicative_inverse(e, phi)

    return ((e, n), (d, n))


def encrypt(m, key):
    x, y = key
    exp = m ** x
    enc = exp % y
    return enc


def decrypt(c, key):
    a, b = key
    exp = c ** a
    dec = exp % b
    return dec


while True:

    print("\n\tRSA Encryption / Decryption ")

    p = int(input('Enter prime p: '))
    q = int(input('Enter prime q: '))

    if isPrime(p) == True and isPrime(q) == True:
        public, private = generate_keys(p, q)
        print("\n\tThe public key is ", public, " and the private key is ", private)

        s = int(input("Enter a message to encrypt: "))

        encrypted_msg = encrypt(s, public)
        print("Your enripted message is: " + str(encrypted_msg) + "\n")
        d = int(input("Enter a message to Decript: "))
        decript_msg = decrypt(d, private)
        print("Decrypted message: " + str(decript_msg) + "\n")
    else:
        print("Please, Both numbers must be Prime")









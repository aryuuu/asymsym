from Crypto.Util import number
from random import randint
from types import SimpleNamespace
from datetime import datetime as dt
import json

from util import findPrimRoot

class PubKey(object):
    def __init__(self, y=None, g=None, p=None):
        self.y = y
        self.g = g
        self.p = p

class PrivKey(object):
    def __init__(self, x=None, p=None):
        self.x = x
        self.p = p

# Encode and Decode block for ElGamal
def encode(plain):
    z = []
    k = 32
    j = -1 * k
    
    for i in range(len(plain)):
        if (i % k == 0):
            j += k
            z.append(0)
        
        z[j//k] += ord(plain[i]) * (2 ** (8 * (i % k)))

    return z

def decode(plain):
    bb = []
    k = 32

    for n in plain:
        for i in range(k):
            t = n

            for j in range(i+1, k):
                t = t % (2 ** (8*j))

            l = t // (2 ** (8 * i))
            bb.append(l)

            n = n - (l * 2 ** (8 * i))
    
    dec = ''.join(chr(c) for c in bb)

    return dec

def gen_key_pair():
    p = number.getPrime(512)
    g = pow(findPrimRoot(p), 2, p)
    x = randint(1, (p/1))
    y = pow(g, x, p)

    pub_key = PubKey(y, g, p)
    priv_key = PrivKey(x ,p)

    return pub_key, priv_key

def encrypt(key, plain):
    start = dt.now()

    e = encode(plain)
    cip = []

    for m in e:
        k = randint(1, key.p - 2)
        a = pow(key.g, k, key.p)
        b = (pow(key.y, k, key.p) * m) % key.p

        cip.append([a, b])
    
    enc = ""

    for p in cip:
        enc += str(p[0]) + ' ' + str(p[1]) + ' '

    end = dt.now()

    return enc, (end-start).microseconds

def decrypt(key, cipher):
    start = dt.now()

    dec = []
    cip = cipher.split()

    for i in range(0, len(cip), 2):
        a = int(cip[i])
        b = int(cip[i+1])

        ax1 = pow(a, key.p - 1 - key.x, key.p)
        m = (b * ax1) % key.p

        dec.append(m)
    
    d = decode(dec)
    dec = "".join([p for p in d if p != '\x00'])

    end = dt.now()

    return dec, (end-start).microseconds

if __name__ == "__main__":
    while(1):
        print("What do you want to do?")
        print("[1] Generate key pair")
        print("[2] Encrypt")
        print("[3] Decrypt")
        print("[4] Exit")

        choice = input(">> ")

        if (choice == "1"):
            name = input("What is your name? ")
            print("Generating key for %s" % name)

            pub_key, priv_key = gen_key_pair()

            filepath = "./test/"

            with open(filepath + name + ".pub", 'w') as pubf: 
                json.dump(json.dumps(pub_key.__dict__), pubf)
            with open(filepath + name + ".pri", 'w') as prif: 
                json.dump(json.dumps(priv_key.__dict__), prif)

            print("Your key pair has been generated")
            print("Check key file in test dir")

        elif(choice == "2"):
            pub_key = input("Public key file >> ")
            message_file = input("Message file >> ")

            with open(pub_key, 'r') as pubf:
                pub_key = json.load(pubf)
            
            pub_key = json.loads(pub_key, object_hook=lambda d: SimpleNamespace(**d))
            message = ""

            with open(message_file, 'r') as mf:
                message = mf.read()
            
            ciphertext, elapsed_time= encrypt(pub_key, message)

            with open(message_file + '.enc', 'w') as encf:
                encf.write(str(ciphertext))

            print("Message encrypted")
            print("Time elapsed %s" % elapsed_time)
            print("Ciphertext size %s bytes" % len(str(ciphertext)))

        elif(choice == "3"):
            priv_key = input("Private key file >> ")
            ciphertext_file = input("Ciphertext file >> ")

            with open(priv_key, 'r') as prif:
                priv_key = json.load(prif)
            
            priv_key = json.loads(priv_key, object_hook=lambda d: SimpleNamespace(**d))
            ciphertext = ""

            with open(ciphertext_file, 'r') as cf:
                ciphertext = cf.read()
            
            message, time_elapsed = decrypt(priv_key, ciphertext)

            with open(ciphertext_file + '.dec', 'w') as mf:
                mf.write(message)

            print("Message decrypted")
            print("Time elapsed %s" % time_elapsed)
        elif(choice == "4"):
            break
        else:
            print("Invalid choice")

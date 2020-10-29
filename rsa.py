from Crypto.Util import number
from random import randint
from types import SimpleNamespace
import math, json

class PubKey(object):
    def __init__(self, n, e):
        self.n = n
        self.e = e

class PrivKey(object):
    def __init__(self, n, d):
        self.n = n
        self.d = d

# extended eucledian GCD
def egcd(a, b):
    if (a == 0):
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b //a) * y, y)

# modular inverse
def mod_inv(a, m):
    g, x, y = egcd(a, m)

    if (g != 1):
        raise Exception('modular inverse failed')
    else:
        return x % m
    
def str_to_int(string):
    return int(string.encode('utf-8').hex(), 16)

def int_to_str(num):
    return bytes.fromhex(hex(num)[2:]).decode()

def gen_key_pair():
    e = 65537
    p = number.getPrime(512)
    q = number.getPrime(512)

    n = p * q
    phi = (p-1) * (q-1)

    d = mod_inv(e, phi)

    pub_key = PubKey(n, e)
    priv_key = PrivKey(n, d)

    return pub_key, priv_key

def rsa_encrypt(plaintext, pub_key):
    m = str_to_int(plaintext)
    c = pow(m, pub_key.e, pub_key.n)
    return c

def rsa_decrypt(ciphertext, priv_key):
    m = pow(ciphertext, priv_key.d, priv_key.n)
    string = int_to_str(m)
    return string
    # for i in string:
    #     print(hex(ord(i)))

if __name__ == "__main__":
    while(1):
        print("What do you want to do? ")
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

        elif (choice == "2"):
            pub_key = input("Public key file >> ")
            message_file = input("Message file >> ")

            with open(pub_key, 'r') as pubf:
                pub_key = json.load(pubf)
            
            pub_key = json.loads(pub_key, object_hook=lambda d: SimpleNamespace(**d))
            message = ""

            with open(message_file, 'r') as mf:
                message = mf.read()
            
            ciphertext = rsa_encrypt(message, pub_key)

            with open(message_file + '.enc', 'w') as encf:
                encf.write(str(ciphertext))

            print("Message encrypted")

        elif (choice == "3"):
            priv_key = input("Private key file >> ")
            ciphertext_file = input("Ciphertext file >> ")

            with open(priv_key, 'r') as prif:
                priv_key = json.load(prif)
            
            priv_key = json.loads(priv_key, object_hook=lambda d: SimpleNamespace(**d))
            ciphertext = ""

            with open(ciphertext_file, 'r') as cf:
                ciphertext = cf.read()
            
            message = rsa_decrypt(int(ciphertext), priv_key)

            with open(ciphertext_file + '.dec', 'w') as mf:
                mf.write(message)

            print("Message decrypted")


        elif (choice == "4"):
            break
        else:
            print("Invalid choice")

    

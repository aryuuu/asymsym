from Crypto.Util import number
from random import randint
import math, json, time

from util import findPrimRoot

bit = 256

def generate_session_key(n, g, x, y):
    val1 = pow(g, x, n)
    val2 = pow(g, y, n)

    k1 = pow(val2, x, n)
    k2 = pow(val1, y, n)

    return k1, k2

if __name__ == "__main__":
    first_person = input("First person >> ")
    second_person = input("Second person >> ")

    print("Generating big prime")
    n = number.getPrime(512)
    g = findPrimRoot(n)

    print("Big prime generated")

    print("Generating big numbers")
    x = randint(2**bit-1, 2**bit)
    y = randint(2**bit-1, 2**bit)

    print("Generating keys")

    k1, k2 = generate_session_key(n, g, x, y)

    print("Keys generated")

    print(k1)
    print(k2)
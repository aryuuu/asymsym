from Crypto.Util import number
from random import randint
import math, time

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
    if i % k == 0:
      j += k
      z.append(0)
    z[j//k] += ord(plain[i])*(2**(8*(i%k)))
  return z,,
#!/usr/bin/python

# Diffie-Hellman Key exchange.

import sys
import random 

if len(sys.argv) != 3: 
    err = sys.argv[0] + " g p"
    print("Expected: " + err)
    sys.exit()

g = int(sys.argv[1])
p = int(sys.argv[2])


print("Publicly Shared Variables:")
print("Publicly Shared Prime: " + str(g))
print("Publicly Shared Base: " + str(p))

a = random.randrange(1, 51)
b = random.randrange(1, 51)

def compute(secret):
    return g**secret % p

A = compute(a)
B = compute(b)


print("  Alice Sends Over Public Chanel: " + str(A))
print("  Bob Sends Over Public Chanel: " + str(B))

def SharedSecret(result, secret):
    return result ** secret % p

print("------------")
print("Privately Calculated Shared Secret:")

print("    Alice Shared Secret: " + str(SharedSecret(B, a)))
print("    Bob Shared Secret: " + str(SharedSecret(A,b)))
'''
$ python dh2.py 17 2
Publicly Shared Variables:
    Publicly Shared Prime:  17
    Publicly Shared Base:   2
  Alice Sends Over Public Chanel:  13
   Bob Sends Over Public Chanel:  9
------------
Privately Calculated Shared Secret:
    Alice Shared Secret:  4
    Bob Shared Secret:  4
'''

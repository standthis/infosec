#!/usr/bin/python

# Diffie-Hellman Key exchange.

import sys
import random 
import time

if len(sys.argv) != 3: 
    err = sys.argv[0] + " g p"
    print("Expected: " + err)
    sys.exit()

maxSecret = 1000
g = int(sys.argv[1])
p = int(sys.argv[2])


print("Publicly Shared Variables:")
print("Publicly Shared Prime: " + str(g))
print("Publicly Shared Base: " + str(p))

a = random.randrange(1, maxSecret + 1)
b = random.randrange(1, maxSecret + 1)
print(a)
print(b)

def compute(secret):
    return g**secret % p

A = compute(a)
B = compute(b)

print(" Alice secret: " + str(a))
print(" Bob secret: " + str(b))

print("  Alice Sends Over Public Chanel: " + str(A))
print("  Bob Sends Over Public Chanel: " + str(B))

def SharedSecret(result, secret):
    return result**secret % p

print("------------")
print("Privately Calculated Shared Secret:")
aliceSS = SharedSecret(B, a)
bobSS = SharedSecret(A,b)
print("    Alice Shared Secret: " + str(aliceSS))
print("    Bob Shared Secret: " + str(bobSS))

def bruteForce():
    for i in range(1, maxSecret + 1):
        if SharedSecret(A, i) == aliceSS:
            for i in range(1, maxSecret + 1):
                if bobSS == SharedSecret(B, i):
                    if aliceSS == bobSS:
                        return str(aliceSS)
    return "Failed to brute force"


print("\nATTEMPTING BRUCE FORCE BASED ON INTERCEPTION OF NETWORK TRAFFIC")
t1 = time.time()
print("The secret key is : " + bruteForce())
t2 = time.time()
print("Time taken : " + str(t2 - t1))





        




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

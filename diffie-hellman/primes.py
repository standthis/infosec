from random import getrandbits
from random import randint
import sys

# Helper Script to generate p and primitive root modulo p 
# Taken from https://github.com/masterrr/cryptography/blob/master/Diffie-Hellman/main.py

def is_prime_calc(num):
    return all(num % i for i in range(2, num))

def is_prime(num):
    return is_prime_calc(num)

def get_random_prime():
    while True:
        n = getrandbits(12) + 3;
        if is_prime(n):
            return n

def gcd(a,b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

def primitive_root(modulo):
    required_set = set(num for num in range (1, modulo) if gcd(num, modulo) == 1)
    for g in range(1, modulo):
        actual_set = set(pow(g, powers) % modulo for powers in range (1, modulo))
        if required_set == actual_set:
            return g



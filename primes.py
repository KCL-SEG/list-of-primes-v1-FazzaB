"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""
def checkIfPrime(number):
    isPrime = True
    for i in range (2,number):
        if number%i == 0:
            isPrime = False
    return isPrime

def primes(number_of_primes):
    list = []
    num = 1
    while len(list) < number_of_primes:
        num = num + 1
        if checkIfPrime(num) == True:
            list.append(num)
    return list

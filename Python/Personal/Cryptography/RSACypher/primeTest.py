LOW_PRIMES = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]

import random
def rabinMiller(num):
    if num % 2 == 0 or num < 2:
        return False
    if num == 3:
        return True
    s = num  - 1
    t = 0
    while s % 2 == 0:
        #keep halving s until it is odd
        s = s // 2
        t += 1
    for trials in range(5):
        a = random.randrange(2, num - 1)
        v = pow(a,s,num)
        if v != 1:
            i = 0
            while v != (num - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v ** 2) % num
    return True


def isPrime(num):
    if (num < 2):
        return False
    for prime in LOW_PRIMES:
        if (num == prime):
            return True
        if (num % prime == 0):
            return False
    return rabinMiller(num)

print ("37 + " + str(isPrime(37)))
print ("137 + " + str(isPrime(137)))
print ("8937049783 + " + str(isPrime(8937049783)))
print ("8937049813 + " + str(isPrime(8937049813)))
print ("671998030559713968361666935769 " + str(isPrime(671998030559713968361666935769)))

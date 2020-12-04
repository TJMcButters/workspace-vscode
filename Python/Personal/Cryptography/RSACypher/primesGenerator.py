import random
LOW_PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
low = '1'
high = '9'
for i in range(200):
    low += '0'
    high += '9'
low = int(low)
high = int(high)


def rabinMiller(num):
    if num % 2 == 0 or num < 2:
        return False
    if num == 3:
        return True
    s = num - 1
    t = 0
    while s % 2 == 0:
        # keep halving s until it is odd
        s = s // 2
        t += 1
    for trials in range(5):
        a = random.randrange(2, num - 1)
        v = pow(a, s, num)
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
    if num < 2:
        return False
    for prime in LOW_PRIMES:
        if num == prime:
            return True
        if num % prime == 0:
            return False
    return rabinMiller(num)


def main():
    count = 0
    primes = []
    while count <= 1:
        x = random.randint(low, high)
        if isPrime(x):
            count += 1
            primes.append(x)
    for prime in range(len(primes)):
        print("Prime " + str(prime + 1) + ": " + str(primes[prime]))


if __name__ == '__main__':
    main()
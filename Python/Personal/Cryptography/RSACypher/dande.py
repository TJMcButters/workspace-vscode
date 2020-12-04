#RSA Encrypt ===============================================================

import random,math

#Testing whether a number is prime
LOW_PRIMES = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
def isPrime(num):
    if (num < 2):
        return False
    for prime in LOW_PRIMES:
        if (num == prime):
            return True
        if (num % prime == 0):
            return False
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

#randomly test number from 1/2 the end to the end
def generateLargePrime(keySize):
    while True:
        num = random.randrange(2**(keySize-1),2**(keySize))
        if isPrime(num):
            return num
            break

#Generate key pair based on keysize
def generatekey(keySize):
   
    p = 0
    q = 0
    print ("Generating Primes ...")
    while p == q:
        p = generateLargePrime(keySize)
        q = generateLargePrime(keySize)
    n = p*q
    m =(p - 1)*(q -1)
    print("\nPrivate Key p : " + str(p))
    print("\nPrivate Key q : " + str(q))
    print("\nPublic Key Modulus n : " + str(n))
    print("\nExponent Modulus m : " + str(m))
    while True:
        e = random.randrange(2 ** (keySize -1), 2 ** (keySize))
        if math.gcd(e,m) == 1:
            break
    print("\nPublic Key e = " + str(e))
    return [n,e,m]

#MAIN LINE
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()-=[];,._+{}|:<>?            '
numSym = len(SYMBOLS)

#Get user input
plainText = input("Enter Your Plain Text : ")
keySize = int(input ("Enter the key size (64-4096 bits) : "))

#Convert Text to Digits
plainNumText = ''
for symbol in plainText:
    pos = SYMBOLS.find(symbol)
    if pos < 10:
        plainNumText += '0' + str(pos)
    plainNumText += str(pos)
#Show the plain num text
print(plainNumText)

#Genertate the key pair
keyPair = generatekey(keySize)
n = keyPair[0]
e = keyPair[1]
m = keyPair[2]

#Encrypt the text
cipherText = pow(int(plainNumText),e,n)
print("\nThis is our cipher Text : " + str(cipherText))

#DECRYPTION PROCESS ==================================================================================
print("\nNow time to decrypt...")

#Clear out plain text
plainTextNum = ''

#Calculate the reverse exponent key: d
if math.gcd(e,m) != 1:
    print("\nWrong Keys!")
    
u1, u2, u3 = 1, 0, e
v1, v2, v3 = 0, 1, m
while v3 != 0:
     x = u3 // v3  # Note that // is the integer division operator.
     v1, v2, v3, u1, u2, u3 = (u1 - x * v1), (u2 - x * v2), (u3 - x * v3), v1, v2, v3
     
d = u1 % m

#Verify the exponents, debug option
'''t = (e*d) % m
print("\nThis should be 1: " + str(t))'''

#Verify inverse key: d
print("\nThe inverse key is : " + str(d))

#Decrypt the cipher
plainTextNum = str(pow(int(cipherText),d,n))
print("\nThe Plain Text Num is : " + plainTextNum)
print("\nThe Plain Text is : ")
curPos = 0
while curPos < (len(plainTextNum) - 1):
    plainNum = int(plainTextNum[curPos]) * 10 + int(plainTextNum[curPos+1])
    plainText = SYMBOLS[plainNum]
    print (plainText, end = "")
    curPos += 2

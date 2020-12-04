import re
import math

# E = Log2(r^L)

"""
Entropy is the opposite of order. It is randomness. Calculating the 'entropy' of a password is essentially
the same as calculating how difficult it is to crack, or guess, a password. 

Password strength is determined with this chart:
< 28 bits = Very Weak; might keep out family members
28 - 35 bits = Weak; should keep out most people, often good for desktop login passwords
36 - 59 bits = Reasonable; fairly secure passwords for network and company passwords
60 - 127 bits = Strong; can be good for guarding financial information
128+ bits = Very Strong; often overkill
"""

pass_word = input("What is your password: ")

lower = False
upper = False
numbers = False
symbols = False
symbols_str = '`~!@#$%^&*()_-+=[{]}\\|;:\'\",<.>/? '  # 33
L = len(pass_word)
R = 0

if re.search('[a-z]', pass_word):
    lower = True
    R += 26
if re.search('[A-Z]', pass_word):
    upper = True
    R += 26
if re.search('[0-9]', pass_word):
    numbers = True
    R += 10

# Checking for Symbols in password
for character in range(len(pass_word)):
    if pass_word[character] in symbols_str:
        symbols = True
        R += 33
        break

E = math.log2(math.pow(R, L))

print('Lower: ' + str(lower))
print('Upper: ' + str(upper))
print('Numbers: ' + str(numbers))
print('Symbols: ' + str(symbols))
print('R: ' + str(R))
print('L: ' + str(L))
print('Password Strength: ' + str(E))
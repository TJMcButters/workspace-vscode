#This is the RSA Decrypt

import random,math

#temporary assignments
p = 16848307887662126047
q = 12066375379566496283
n = (p-1)*(q-1)
e = 9903235676081582309
cipherNum = 42059318370166819178542881780301689120
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()-=[];,._+{}|:<>?              '


#main line
#gets key info from user
"""keySize = int(input ("How many bits do you want for your decryption?"))
e = int(input("Enter the public key exponent e :")) 
p = int(input("Enter the Secret Key p :"))
q = int(input("Enter the Secret Key q :"))
n = p*q"""
print("n is :" + str(n))
#calculate the reverse exponent key
if math.gcd(e,n) != 1:
    print("Wrong Keys")
u1,u2,u3 = 1,0,e
v1,v2,v3 = 0,1,n

while v3 != 0:
    qq = u3 // v3
    v1,v2,v3,u1,u2,u3 = (u1 - qq*v1), (u2 - qq * v2), (u3 - qq*v3),v1,v2,v3
    print(str(v1) + " " + str(v2) + " " + str(v3) + " " + str(u1) + " " + str(u2) +" " + str(u3))
d = u1 % n     #reverse exponent key

print("The Inverse Key is : " + str(d))
plainTextNum = str(pow(int(cipherNum),d,n))
print("The Plain Text Num is : " + plainTextNum)
curPos = 0
while curPos < (len(plainTextNum) - 1):
    plainNum = int(plainTextNum[curPos]) * 10 + int(plainTextNum[curPos+1])
    plainText = SYMBOLS[plainNum]
    print (plainText, end = "")
    curPos += 2

exit(0)

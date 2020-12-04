# This is a Message Authentication with the Hill Cipher
# By Jonathan Zderad on Sep 8, 2020

# Defining Variables/Constants
choice = input("Do you want to encrypt or decrypt? [e or d]:")
if choice == "e":
    M = [[6, 24, 1], [13, 16, 10], [20, 17, 15]]
    print ("Hello Bob ... ")
if choice == "d":
    M = [[8, 5, 10], [21, 8, 21], [21, 12, 8]]
    print ("Hello Alice ...")
    testMac = input("Enter Bob's MAC : ")
PN = [[0], [0], [0]]
CN = [[0], [0], [0]]
SYMBOLS = "abcdefghijklmnopqrstuvwxyz"
numSym = len(SYMBOLS)

# Getting Message
plainText = input("Enter Message : ")
lenText = len(plainText)
while (lenText % 3 != 0):
    plainText += 'z'
    lenText = len(plainText)

#Getting Ready to Translate Message
curPos = 0
cipherText = ""
messageMac = 0;
translationMac = 0;

#Translating Message with MAC
while (curPos < len(plainText)):

    PN[0][0] = SYMBOLS.find(plainText[curPos])
    PN[1][0] = SYMBOLS.find(plainText[curPos + 1])
    PN[2][0] = SYMBOLS.find(plainText[curPos + 2])
    #print("Message Num is :" + str(PN))
    messageMac = messageMac ^ (10000 * PN[0][0] + 100 * PN[1][0] + PN[2][0])
    # Matrix Multiplication for Cipher Number
    CN = [[0], [0], [0]]
    for i in range(len(M)):
        for j in range(len(PN[0])):
            for k in range(len(PN)):
                CN[i][j] += M[i][k] * PN[k][j]
            CN[i][j] = CN[i][j] % numSym
    #print("Translation Num is :" + str(CN))
    # Compute Cipher Text
    cipherText += SYMBOLS[CN[0][0]]
    cipherText += SYMBOLS[CN[1][0]]
    cipherText += SYMBOLS[CN[2][0]]
    curPos += 3
    translationMac = translationMac ^ (10000 * CN[0][0] + 100 * CN[1][0] + CN[2][0])
    #print("Current MAC is: " + str(mac))

# Final Printout Depending on Whether it is Bob or Alice
if choice == "e":
    print("OK Bob ...  You should send ...")
    print("Translation Text plus MAC is :" + cipherText + str(messageMac))

if choice == "d":
    if (testMac == translationMac):
        print("Bob's Message is Authenticated")
        print("Bob's Message is : " + cipherText)
    else:
        print("Bob's MAC should be:" + str(translationMac))
        print("Bob's Message is Corrupted.")
exit(0)
letters = 'abcdefghijklmnopqrstuvwxyz'
list_lets = list(letters)

name = input("Enter your name: ")
name = name.lower().strip()
cText = []

for x in range(len(name)):
    for y in range(len(list_lets)):
        if name[x] == list_lets[y]:
            z = ((7 * y) + 18) % 26
            cText.append(letters[z])
            
print(''.join(map(str, cText)))

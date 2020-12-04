x = input("What's your message: ")
alpha = 'abcdefghijklmnopqrstuvwxyz'
punc = "!@#$%^&*()_-+=\{\[\}\]|\\:;\"<,>.?/\'"
z = ''
count = 1

for y in x.lower():
    if y in alpha:
        if count % 2 == 1:
            z += y.upper()
        else:
            z += y
        count += 1
    if y == ' ':
        z += ' '
    if y in punc:
        z += y

print(z)
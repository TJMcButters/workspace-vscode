import math

for x in range(25):
    print(str(x) + ": " + str((math.pow(x, 3)) % 26))
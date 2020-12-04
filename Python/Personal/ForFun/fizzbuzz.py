for i in range(1, 100):
    if i % 3 == 0 and i % 5 == 0:
        print(str(i) + ": FizzBuzz")
    elif i % 5 == 0:
        print(str(i) + ": Buzz")
    elif i % 3 == 0:
        print(str(i) + ": Fizz")
    else:
        print(str(i) + ": ")
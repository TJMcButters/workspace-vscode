import randomnumber

x = randomnumber.generate_number(100)
correct = False

while not correct:
    guess = int(input("Guess a number: "))
    if guess > x:
        print("Too high, guess again: ")
        continue
    elif guess < x:
        print("Too low, guess again: ")
        continue
    elif guess == x:
        print("You got it!")
        break
    
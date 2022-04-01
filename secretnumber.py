secret = 15

guess = int(input("Guess the secret number: "))

if guess == secret:
    print("Congratulations! It's number 15.")

else:
    print("Sorry, that's incorrect. The secret number is not " + str(guess))


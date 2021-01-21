
number = 5
guess = int(input("Please guess a number between 1 and 10 : "))

if guess == number:
    print("You guessed it first time")
elif guess > number:
    print("Please guess Lower: ")
    guess = int(input())
    if guess == number:
        print("You guessed correctly")
    else:
         print("Wrong guess. Game over!")
elif guess < number:
    print("Please guess Higher : ")
    guess = int(input())
    if guess == number:
        print("You guessed correctly")
    else:
        print("Wrong guess. Game over!")



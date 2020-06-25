"""Week 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """

    print("\nWelcome to the guessing game!")
    print("A number between _ and _ ?")
    upperBound = False
    while type(upperBound) is not int:
        try:
            upperBound=int(input("Enter an upper bound value: "))
        except ValueError:
            print('bru i want an integer lmao!!!! (just give me an integer im begging you)')

    lowerBound = False
    while type(lowerBound) is not int:
        try:
            lowerBound = int(input("Enter a lower bound value: "))
        except ValueError:
            print('lol xd what. that is not integer lol. plz give me integer hahah')

    
    upperBound = int(upperBound)
    lowerBound = int(lowerBound)

    if lowerBound > upperBound:
        temp = lowerBound
        lowerBound = upperBound
        upperBound = temp
        print('lol r u dumb. LOWER-bound is meant to be LOWER than UPPER-bound. but whatever i can work with that.')

    print("OK then, a number between " + str(lowerBound) + " and {} ?".format(upperBound))    

    actualNumber = random.randint(lowerBound, upperBound)

    guessed = False

    while not guessed:
        guessedNumber = False
        while type(guessedNumber) is not int:
            try:
                guessedNumber = int(input("Guess a number: "))
            except ValueError:
                print('you think this is funny? What happens when you cross an a non-integer input with code that expects an integer? I will tell you what you get. You get this message')

        print("You guessed {},".format(guessedNumber),)
        if guessedNumber == actualNumber:
            print('It took you a while (not too sure what that says about your IQ) but at least:')
            guessed = True
        elif guessedNumber < actualNumber:
            print("Too small, try again :(")
        else:
            print("Too big, try again :(")
        if guessedNumber < lowerBound:
            print('your litterally guessing below the lowerbound dumbass')
        elif guessedNumber > upperBound:
          print('your litterally guessing above the upperbound. what did you expect?')
    return "You got it!"
    # the tests are looking for the exact string "You got it!". Don't modify that!


if __name__ == "__main__":
    print(advancedGuessingGame())

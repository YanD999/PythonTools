from random import randint
# get user input via terminal
highest = input("Type the highest number to guess in: ")
maxG = input("Type the maximum amount of guesses in: ")

try: # when guess is not an integer
    high = int(highest)
    mx = int(maxG)
except:
    print("You have to give a valid number")
    exit()
   
toguess = randint(1, high) # random number to guess
count = 0 # times guessed     

while (True):
    if count == mx: # no guesses left and not found
        print("\nYou have no more guesses\nThe number was " + str(toguess))
        exit()
    guess = input("\nGuess: ")
    
    if guess.isnumeric(): # if guess (string) is number
        count += 1
        if toguess == int(guess): # found
            if count == 1:
                print("You found the number after one guess. Congratulations")
            else:
                print("You found the number after " + str(count) + " guesses")
            exit()
        elif mx - count > 0: # not found and guesses left
            if mx - count == 1:
                print("\nYou have one guess left")
            else:
                print("\nYou have " + str(mx - count) + " guesses left")
    else:
        print("You have to give a valid number")



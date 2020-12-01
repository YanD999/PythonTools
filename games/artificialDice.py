from random import randint
# get user input via terminal
dices = input("How many dices do you want? ")

def diceGen(): # generates random number
    return randint(1, 6)

def showDice(): # prints dices
    dice = diceGen()
    if dice == 1:
        print("\t   x")
    elif dice == 2:
        print("\tx\n\n\t     x")
    elif dice == 3:
        print("\tx\n         x\n           x")
    elif dice == 4:
        print("\tx    x\t\n\n\tx    x")
    elif dice == 5:
        print("\tx     x\n\t   x\n\tx     x")
    else:
        print("\tx    x\n\tx    x\n\tx    x")
    print("")

def execute():
    try: # when input is not an integer
        amount = int(dices)        
    except:
        print("You have to give a number")
        exit()
        
    if amount == 0:
        print("No dice")
    else:
        done = 0
        while (done < amount):
            print("Dice " + str(done+1))
            showDice()
            done += 1
            
execute()

# get user input via terminal
playerone = input("Name of the first player: ")
playertwo = input("Name of the second player: ")

if playerone == '' or playertwo == '':
    print("You have to fill in valid names for the players")
    exit()
elif playerone == playertwo:
    print("Please use two different names")
    exit()

winner = ""
grid = [".", ".", ".", ".", ".", ".", ".", ".", "."] # x and o

def currentPlayer():
    count = 0
    for k in range(0,9):
        if grid[k] != '.':
            count += 1
    if count%2 == 0: # even number of moves played
        return playerone
    else:
        return playertwo
        
def possiblePlays():
    playable = "You can play "
    for i in range(0, 9):
        if grid[i] == ".":
            playable += str(i) + ", "
    return playable[:-2]

def validPlay(move):
    if move.isnumeric() == False:
        return False
    if int(move) < 0 or int(move) > 8:
        return False
    else:
        return grid[int(move)] == "."
    
def playMove(move):
    global grid # makes global var accessible locally
    if currentPlayer() == playerone:
        grid[move] = "X"
    else:
        grid[move] = "O"
    
def isWinner():
    global winner
    sign = ""
    if grid[0] == grid[1] and grid[0] == grid[2]:
        sign = grid[0]
    elif grid[3] == grid[4] and grid[3] == grid[5]:
        sign = grid[3]
    elif grid[6] == grid[7] and grid[6] == grid[8]:
        sign = grid[6]
    elif grid[0] == grid[3] and grid[0] == grid[6]:
        sign = grid[0]
    elif grid[1] == grid[4] and grid[1] == grid[7]:
        sign = grid[1]
    elif grid[2] == grid[5] and grid[2] == grid[8]:
        sign = grid[2]
    elif grid[0] == grid[4] and grid[0] == grid[8]:
        sign = grid[0]
    elif grid[2] == grid[4] and grid[2] == grid[6]:
        sign = grid[2]
    if sign == 'X':
        winner = playerone
        return True
    elif sign == 'O':
        winner = playertwo
        return True
    return False

def showGrid():
    print("\n" + grid[0] + "\t" + grid[1] + "\t" + grid[2] + "\n" + grid[3] + "\t" + grid[4] + "\t" + grid[5] + "\n" + grid[6] + "\t" + grid[7] + "\t" + grid[8] + "\n")

while len(possiblePlays()) > 13: # still some possible moves doable
    if isWinner():
        break
    print("It's the turn of " + currentPlayer())
    print(possiblePlays()) # show grid, possible plays
    showGrid()
    play = input("\n" + currentPlayer() + ", make a move: ")
    while (validPlay(play) == False):
        print("This is an invalid move")
        print(possiblePlays())
        play = input("Make a move: ")
    playMove(int(play))
    showGrid()
    
# print winner
if winner == "":
    print("It's a draw game")
else:
    print("The winner is " + winner)

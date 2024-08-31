#global variable
board = ["_", "_", "_",
        "_", "_", "_",
        "_", "_", "_"]
currentPlayer = "X"
winner = None
gameRunning = True


#printing the game board
def printBoard(board):
    print("-------------")
    print("| " + board[0] + " | " + board[1] + " | " + board[2] + " | ")
    print("-------------")
    print("| " + board[3] + " | " + board[4] + " | " + board[5] + " | ")
    print("-------------")
    print("| " + board[6] + " | " + board[7] + " | " + board[8] + " | ")
    print("-------------")

#take player input 
def playerInput(board):
    num = int(input("Enter a number between 1 - 9 "))
    if num >=1 and num<=9 and board[num-1]== "_":
        board[num-1]=currentPlayer
    else:
        print("Oops spot already taken")

#check for win or tie
def checkHorizontal(board):
    #can make changes to global variable
    global winner 
    if (board[0]==board[1]==board[2]) and board[0]!= "_":
        winner = board[0]
        return True
    elif (board[3]==board[4]==board[5]) and board[3]!= "_":
        winner = board[3]
        return True
    elif (board[6]==board[7]==board[8]) and board[6]!= "_":
        winner = board[6]
        return True

def checkVertically(board):
    global winner 
    if (board[0]==board[3]==board[6]) and board[0]!= "_":
        winner = board[0]
        return True
    elif (board[1]==board[4]==board[7]) and board[1]!= "_":
        winner = board[1]
        return True
    elif (board[2]==board[5]==board[8]) and board[2]!= "_":
        winner = board[2]
        return True
    
def checkDiagonally(board):
    global winner 
    if (board[0]==board[4]==board[8]) and board[0]!= "_":
        winner = board[0]
        return True
    elif (board[6]==board[4]==board[2]) and board[6]!= "_":
        winner = board[6]
        return True
    
def checkTie(board):
    global gameRunning
    if "_" not in board and winner == None:
        printBoard(board)
        print("It is a tie :(")
        gameRunning=False

def checkWin():
    global gameRunning
    if checkDiagonally(board) or checkHorizontal(board) or checkVertically(board):
        printBoard(board)
        print(f"The winner is {winner}")
        gameRunning=False


#switch the player 
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

#check for win or tie again
while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()

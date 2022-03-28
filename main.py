#user userInput
#from curses.ascii import isdigit

#rows[row][column]:
#[ [' ', ' ', ' ']
#  [' ', ' ', ' ']
#  [' ', ' ', ' '] ]

def getInput():
    while True:
        userInput = input('Pick a cell to mark (row# col#): ')
        
        #check for input format 
        if len(userInput) != 3: 
            print('Input format not accepted.')
            continue
        #check if input consists of numbers
        elif not (userInput[0].isdigit() or userInput[2].isdigit()):
            print('Put numbers only.')
            continue

        row = int(userInput[0])
        col = int(userInput[2])

        #if selected numbers are in range 
        if row not in range(0,3) and col not in range(0,3):
            print('Numbers out of range.')
            continue

        #check if cell already marked
        if rows[row][col] != ' ':
            print('That cell is taken.\n')
            continue

        #return a tuple of row and col #
        return (row, col)

def completed():
    global rows 
    #horizontal or vertical
    for i in range(3):
        #if any rows or cols are completed 
        if rows[i][0] == rows[i][1] == rows[i][2] != ' ' or rows[0][i] == rows[1][i] == rows[2][i] != ' ':
                return True
    #if any diagnal line is completed 
    if rows[0][0] == rows[1][1] == rows[2][2] != ' ' or rows[0][2] == rows[1][1] == rows[2][0] != ' ':
        return True
    
    return False

#update and print board
def printBoard(userInput):
    global player
    global rows
    for i in range(3):
        for j in range(3):
            if userInput[0] == i and userInput[1] == j:
                if player == 0:
                    rows[i][j] = 'o'
                else:
                    rows[i][j] = 'x'

    print(rows[0])
    print(rows[1])
    print(rows[2])
    
    #check for any bingo
    if completed() == True:
        if player == 0:
            print('O won!')
        else:
            print('X won!')   


def play():
    global player
    init()
    #while not done 
    while not completed():
    #ask for user userInput
        userInput = getInput();
        #update and print board
        printBoard(userInput) 
        #switch player
        if player == 0:
            player = 1
        else:
            player = 0


def init():
    #initialize global vars 
    global rows 
    global player
    rows = [ [' ', ' ', ' '], 
         [' ', ' ', ' '], 
         [' ', ' ', ' '] ]
    
    player = 0
    #print initial board 
    print(rows[0])
    print(rows[1])
    print(rows[2])


play()
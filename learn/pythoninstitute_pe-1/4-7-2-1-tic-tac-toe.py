from random import randrange

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    edge = "+-------+-------+-------+"
    inline = "|       |       |       |"
    print(edge)
    print(inline)
    print("|  ",board[0][0],"  |  ",board[0][1],"  |  ",board[0][2],"  |")
    print(inline)
    print(edge)
    print(inline)
    print("|  ",board[1][0],"  |  ",board[1][1],"  |  ",board[1][2],"  |")
    print(inline)
    print(edge)
    print(inline)
    print("|  ",board[2][0],"  |  ",board[2][1],"  |  ",board[2][2],"  |")
    print(inline)
    print(edge)

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    valid_move = False
    while valid_move == False:
        row = int(input("Enter your next move in row (1~3): "))
        col = int(input("Enter your next move in column (1~3): "))
        if board[row-1][col-1] != 'X' and board[row-1][col-1] != 'O':
            board[row-1][col-1] = 'O'
            valid_move = True
        else:
            print("Target has been occupied already! Try again...")
    return board
    
def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_fields = []
    for i in range(0,3):
        for j in range(0,3):
            if isinstance(board[i][j],int) == True:
                free_fields.append((i,j))
    return free_fields

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    result = sign
    if (board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X') or \
       (board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X') or \
       (board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X') or \
       (board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X') or \
       (board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X') or \
       (board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X') or \
       (board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X') or \
       (board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X'):
           result = 'C'
    elif (board[0][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O') or \
       (board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O') or \
       (board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O') or \
       (board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O') or \
       (board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O') or \
       (board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O') or \
       (board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O') or \
       (board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O'):
           result = 'M'
    else:
        result = 'N'
    return result

def draw_move(board):
    # The function draws the computer's move and updates the board.
    valid_move = False
    while valid_move == False:
        c_row = randrange(3)
        c_col = randrange(3)
        if board[c_row-1][c_col-1] != 'X' and board[c_row-1][c_col-1] != 'O':
            board[c_row-1][c_col-1] = 'X'
            valid_move = True
    return board
    
# Main Program

board = [[1,2,3],[4,'X',6],[7,8,9]]
display_board(board)
sign = '-'

while make_list_of_free_fields(board) != [] and sign == '-':
    board = enter_move(board)
    display_board(board)
    victory_for(board, sign)
    draw_move(board)
    display_board(board)
    victory_for(board, sign)

if sign == 'C':
    print("Computer wins!")
elif sign == 'M':
    print("Congratulation! You win!")
elif sign == 'N':
    print("No win or lose!")
else:
    print("No more move!")
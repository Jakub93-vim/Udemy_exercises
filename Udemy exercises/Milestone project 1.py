def clear_screen():

    print ('\n'*100)

start_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
full_board = ['#','X','X','X','O','X','O','O','O','X']
win_board = ['#','O','O','O','O','X','O','O','O','X']

def display_board(board): # displays board with board items as a list

    space_line = '   |   |   '
    full_line = '----------------- '
    print ('  ',board[7],'  |  ',board[8],'  |  ',board[9],'\n',\
        full_line,'\n','  ',board[4],'  |  ',board[5],'  |  ',board[6],'\n',\
           full_line,'\n','  ',board[1],'  |  ',board[2],'  |  ',board[3],sep='')

def player_input(): # info about what the player wants to be

        print('Welcome to TicTacToe game')
        marker = 'wrong'

        while marker not in ['X','O']:

            marker = input('Hi Player 1, do you want to be X or O ?')

            if marker not in ['X','O']:
                print('Type in O or X')
        if marker == 'X':
            return ('X','O')
        else:
            return ('O','X')

def player_choice(board): # takes players choice and returns the position as a number


    position = 'wrong'
    while position not in range(1,10): # ask for position among 1-9

        position = input('Write your position(1-9): ')

        if position not in range(1,10) and position.isdigit()== False: # checks if the position is digit
            print('Type in number 1-9')
        elif space_check(board, int(position)) == True: # checks if the space is free via function space_check
            print('This position is full, choose another one')
        else:
            position = int(position)

    return position

def place_marker(board, marker, position): # puts the marker O or X on the position

    board[position] = marker

    return board

def full_board_check(board): # checks if the board is full
    count = 0
    for ele in board:
        if ele == 'X' or ele == 'O':
            count += 1
    if count == 9:
        print('End of the game, no winner !!')
        return False
    else:
        return True

def space_check(board, position):

    if board[position] == 'X' or board[position] == 'O':
        return True
    else:
        return False

def win_check(board):

    if board[1] == 'O' and board[2] == 'O' and board[3] == 'O':
        print('Player O wins !! ')
        return True
    elif board[1] == 'O' and board[5] == 'O' and board[9] == 'O':
        print('Player O wins !! ')
        return True
    elif board[1] == 'O' and board[4] == 'O' and board[7] == 'O':
        print('Player O wins !! ')
        return True
    elif board[4] == 'O' and board[5] == 'O' and board[6] == 'O':
        print('Player O wins !! ')
        return True
    elif board[7] == 'O' and board[8] == 'O' and board[9] == 'O':
        print('Player O wins !! ')
        return True
    elif board[7] == 'O' and board[5] == 'O' and board[3] == 'O':
        print('Player O wins !! ')
        return True
    elif board[8] == 'O' and board[5] == 'O' and board[2] == 'O':
        print('Player O wins !! ')
        return True
    elif board[9] == 'O' and board[6] == 'O' and board[3] == 'O':
        print('Player O wins !! ')
        return True
    #player X
    elif board[1] == 'X' and board[2] == 'X' and board[3] == 'X':
        print('Player X wins !! ')
        return True
    elif board[1] == 'X' and board[5] == 'X' and board[9] == 'X':
        print('Player X wins !! ')
        return True
    elif board[1] == 'X' and board[4] == 'X' and board[7] == 'X':
        print('Player X wins !! ')
        return True
    elif board[4] == 'X' and board[5] == 'X' and board[6] == 'X':
        print('Player X wins !! ')
        return True
    elif board[7] == 'X' and board[8] == 'X' and board[9] == 'X':
        print('Player X wins !! ')
        return True
    elif board[7] == 'X' and board[5] == 'X' and board[3] == 'X':
        print('Player X wins !! ')
        return True
    elif board[8] == 'X' and board[5] == 'X' and board[2] == 'O':
        print('Player X wins !! ')
        return True
    elif board[9] == 'X' and board[6] == 'X' and board[3] == 'O':
        print('Player X wins !! ')
        return True
    else:
        return False



defined_marker = player_input()
display_board(start_board)
defined_position = player_choice(start_board)
board = place_marker(start_board,defined_marker[0],defined_position)
clear_screen()
display_board(board)

while full_board_check(board):
    defined_position = player_choice(board)
    board = place_marker(start_board, defined_marker[1], defined_position)
    if win_check(board) == True:
        display_board(board)
        break
    clear_screen()
    display_board(board)


    defined_position = player_choice(board)
    board = place_marker(start_board, defined_marker[0], defined_position)
    if win_check(board) == True:
        display_board(board)
        break
    clear_screen()
    display_board(board)


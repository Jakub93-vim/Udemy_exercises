def clear_screen():

    print ('\n'*100)

start_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']

def display_board(board):

    space_line = '   |   |   '
    full_line = '----------------- '
    print ('  ',board[7],'  |  ',board[8],'  |  ',board[9],'\n',\
        full_line,'\n','  ',board[4],'  |  ',board[5],'  |  ',board[6],'\n',\
           full_line,'\n','  ',board[1],'  |  ',board[2],'  |  ',board[3],sep='')

def player_input():
    marker = 'wrong'
    position = 'wrong'

    while marker not in ['X','O']:

        marker = input('Hi Player 1, do you want to be X or O ?')

        if marker not in ['X','O']:
            print('Type in O or X')

    while position not in range(1,9):

        position = input('Write your position(1-9): ')

        if position not in range(1,9) and position.isdigit()== False:
            print('Type in number 1-9')
        else:
            position = int(position)

    return marker,position

def place_marker(board, marker, position):

    board[position] = marker

    return board



display_board(start_board)
defined_marker,defined_position = player_input()
board = place_marker(start_board,defined_marker,defined_position)
display_board(board)

defined_marker,defined_position = player_input()
board = place_marker(start_board,defined_marker,defined_position)
display_board(board)
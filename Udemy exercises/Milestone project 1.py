def clear_screen():

    print ('\n'*100)

start_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']

def display_board(board): # displays board with board items as a list

    space_line = '   |   |   '
    full_line = '----------------- '
    print ('  ',board[7],'  |  ',board[8],'  |  ',board[9],'\n',\
        full_line,'\n','  ',board[4],'  |  ',board[5],'  |  ',board[6],'\n',\
           full_line,'\n','  ',board[1],'  |  ',board[2],'  |  ',board[3],sep='')

def player_input():

        marker = 'wrong'

        while marker not in ['X','O']:

            marker = input('Hi Player 1, do you want to be X or O ?')

            if marker not in ['X','O']:
                print('Type in O or X')
        if marker == 'X':
            return ('X','O')
        else:
            return ('O','X')

def player_choice(board):

    #TODO check if the board is empty on that position

    position = 'wrong'
    while position not in range(1,9):

        position = input('Write your position(1-9): ')

        if position not in range(1,9) and position.isdigit()== False:
            print('Type in number 1-9')
        else:
            position = int(position)

    return position

def place_marker(board, marker, position):

    board[position] = marker

    return board



display_board(start_board)
defined_marker = player_input()
defined_position = player_choice(start_board)
board = place_marker(start_board,defined_marker,defined_position)
display_board(board)
n= 1
while n < 10:

    defined_marker,defined_position = player_input()
    clear_screen()
    board = place_marker(start_board,defined_marker,defined_position)
    display_board(board)
    n+= 1
def clear_screen():

    print ('\n'*100)


def display_board(board):

    space_line = '   |   |   '
    full_line = '----------------- '
    print ('  ',board[7],'  |  ',board[8],'  |  ',board[9],'\n',\
        full_line,'\n','  ',board[4],'  |  ',board[5],'  |  ',board[6],'\n',\
           full_line,'\n','  ',board[1],'  |  ',board[2],'  |  ',board[3],sep='')

display_board([' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '])

test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)

#display_board([])
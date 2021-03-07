game_list = [0,1,2,3]

def display_game():
    #print('---------------\nThis is a game where you can change a position in a list\n-------------')
    print('This is the current list', game_list)

def position_choice():
    choice = 'wrong'
    while choice not in ['0','1','2','3']:

        choice = input ('Choice position you want to change 0,1,2,3: ')

        if choice not in ['0','1','2','3']:
            print('You did not choice one of 0,1,2,3')
        else:
            pass
    return int(choice)


def replace_position(game_list, position):

    replace_string = input ('Write a text you want to replace the position with: ')
    game_list[position] = replace_string

    return game_list

def game_choice():

    go_on = 'wrong'

    while go_on not in ['Y','N']:
        go_on = input('Do you want to continue ? (Y/N): ')

        if go_on not in ['Y','N']:
            print ('Answer Y or N')

        if go_on == 'N':
            print('Game is over')

    return go_on


#Game control

go_on ='Y'

while go_on == 'Y':

    display_game()

    position = position_choice()

    game_list = replace_position(game_list, position)

    display_game()

    go_on = game_choice()
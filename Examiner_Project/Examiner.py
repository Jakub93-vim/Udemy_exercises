#Examiner
#--------

vocabulary = [['que','that'],['para','for'],['aquí','here']]

class Examine:

    def __init__(self,time):

        self.time = time

    def examine_me(self):

        check = input(f'Translate to english: {vocabulary[0]}')

        #if check == vocabulary[0][1]

print(vocabulary[0][0])
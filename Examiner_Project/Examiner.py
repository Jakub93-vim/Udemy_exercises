#Examiner
#--------
import time

vocabulary = [['que','that'],['para','for'],['aquí','here']]

class Examine:

    def __init__(self,time_value):

        self.countdown = time_value

    def countdown(self,t):
        while t > 0:
            print(t)
            t -= 1
            time.sleep(1)

    def examine_me(self):

        check = input(f'Translate to english: {vocabulary[0][0]}')


        if check == vocabulary[0][1]:
            print("You are right !")
        else:
            print("No")

first_examine = Examine(10)

#first_examine.examine_me()



def countdown(t):
    print(t)
    while t > 0:
        print('Hello', t,end="\r")
        t -= 1
        time.sleep(1)
        


def countdown2(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print("\r",timer, end='')
        time.sleep(1)
        t -= 1
    print('Blast Off!!!')
    
countdown2(5)
    
print("timer", end="\r")
print("ter")
print("timefgfgr")
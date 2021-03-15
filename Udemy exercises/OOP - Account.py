class Account:

    def __init__(self,owner, balance):

        self.owner = owner
        self.balance = balance

    def deposit  (self,value):
        self.balance = self.balance + value
        print('You have {}'.format(self.balance))

    def withdraw (self,value):
        if ( self.balance - value ) > 0:
            self.balance = self.balance - value
            print('You have {}'.format(self.balance))
        else:
            print('You have only {}'.format(self.balance))

    def __str__(self):
        return f'Account owner: {self.owner}\nAccount balance: {self.balance}'

my_account = Account('Jose',300)

my_account.deposit(200)

my_account.withdraw(700)

my_account.withdraw(350)

print(my_account)


class ATM:
    def __init__(self):
        self.balance = 0
        self.intrest = .001
        self.transaction_history = []

    def __str__(self):
        return f'Balance: {self.balance}\n Interest: {self.interest}'

    def check_balance(self):
        print(f'The balance of this account is ${self.balance}')

    def deposit_amount(self, amount):
        self.balance += amount
        self.transaction_history.append(f'User deposited ${amount}')

    def check_withdrawal(self, amount):
        return self.balance - amount > 0

    def withdrawal(self, amount):
        self.balance -= amount
        self.transaction_history.append(f'User withdrew ${amount}')

    def calc_interest(self):
        return self.balance * self.intrest

    def get_transaction_history(self):
        print('User Transaction History')
        for i in self.transaction_history:
            print(f'{i}')

def interface(account):
    while True:
        q = input('''Please select by typing the number from the follow options
1: Check Balance
2: Deposit
3: Check withdrawal
4: Withdraw
5: Calculate Interest
6: Get Transaction History
0: Quit Session

>''')
        if q == '1':
            account.check_balance()
        elif q == '2':
            amount = input('How much would you like to deposit\n>').replace('$','').strip()
            account.deposit_amount(float(amount))
        elif q == '3':
            amount = input('What amount withdrawal would you like to check?\n>').replace('$','').strip()
            if account.check_withdrawal(float(amount)):
                print('Sufficent Funds')
            else:
                print('Insufficent Funds')
        elif q == '4':
            amount = input('How much would you like to withdraw\n>').replace('$','').strip()
            account.withdrawal(float(amount))
        elif q == '5':
            interest = account.calc_interest()
            print(f'Current Intrest Value {interest}')
        elif q == '6':
            account.get_transaction_history()
        elif q == '0':
            exit()
        else:
            print('Invalid Selection')


if __name__ == '__main__':
    test = ATM()
    interface(test)

class Account:
    def __init__(self, amount, account_type):
        self.balance = float(amount)
        self.account_type = account_type
        with open('file.txt', 'w+') as f:
            if len(f.readlines()) > 0:
                for line in f.readlines():
                    data = line.strip().split(':')
                    print(data)



    def get_funds(self):
        return self.balance

    def deposit(self, amount):
        if not self.get_standing():
            amount -= .50
        self.balance += float(amount)
        self.record_transaction('deposit', amount)
        return self.balance

    def check_withdraw(self, amount):
        if amount > self.balance:
            return False
        else:
            return True

    def withdraw(self, amount):
        if not self.get_standing():
            amount -= .50
        if float(amount) > self.balance:
            raise ValueError
        else:
            self.balance -= float(amount)
        self.record_transaction('withdraw', amount)
        return self.balance

    def get_standing(self):
        if self.balance > 1000:
            return True
        else:
            return False

    def record_transaction(self, type, amount):
        with open('file.txt', 'w+') as f:
            f.write(f'{type}:{amount}\n')

    @staticmethod
    def from_csv_string(string):
        row = string.split(',')
        return Account(float(row[1]), row[2])

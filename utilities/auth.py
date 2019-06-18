from models.account import Account

# TODO switch to Config instead of users dict

users = {Account("Drainyyy", "xyz12345", 0)}


class Auth:
    def __init__(self, account: Account):
        self.account = account

    def login(self):
        for acc in users:
            print(acc is self.account)
            print(acc.username)
            print(acc.password)
            print(acc.uid)
            print(self.account.username)
            print(self.account.password)
            print(self.account.uid)     # TODO accounts not the same
            if acc is self.account:
                return True
            else:
                return False

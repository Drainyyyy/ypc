from models.account import Account


class Auth:
    def __init__(self, account: Account):
        self.account = account

    def login(self):
        print(self.account.username)
        print(self.account.password)
        print(self.account.admin)
        return False

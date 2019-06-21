#  Copyright (c) 2019. Drainyyy
#  This project is covered by MIT License
#  https://opensource.org/licenses/MIT

from models.account import Account

# TODO switch to Config instead of users dict

users = {Account("Drainyyy", "xyz12345", 0)}


class Auth:
    def __init__(self, account: Account):
        self.account = account

    def login(self):
        for acc in users:
            if acc is self.account:
                return True
            else:
                return False

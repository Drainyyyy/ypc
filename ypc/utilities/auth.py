# -*- coding: utf-8 -*-

#  Copyright (c) 2019. Drainyyy
#  This project is covered by MIT License
#  https://opensource.org/licenses/MIT

# TODO switch to Config instead of users dict
from ypc.models import account as acc

users = {acc.DefaultAccount("Drainyyy", "xyz12345", 0)}


class Auth:
    def __init__(self, account: acc.AcceptedAccount):
        self.account = account

    def login(self):
        for acc in users:
            if acc is self.account:
                return True
            else:
                return False

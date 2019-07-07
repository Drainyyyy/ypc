# -*- coding: utf-8 -*-

#  Copyright (c) 2019. Drainyyy
#  This project is covered by MIT License
#  https://opensource.org/licenses/MIT

# TODO switch to Config instead of users dict
from ypc.models import account as acc
from ypc.models.enums import AccountType, AccountStatus

users = {acc.Account("Drainyyy", "xyz12345", 0, AccountType.admin, AccountStatus.accepted)}


class Auth:
    def __init__(self, account: acc.Account):
        self.account = account

    def login(self):
        for acc in users:
            if acc is self.account:
                return True
            else:
                continue
        return False

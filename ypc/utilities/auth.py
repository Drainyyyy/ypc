# -*- coding: utf-8 -*-

#  Copyright (c) 2019. Drainyyy
#  This project is covered by MIT License
#  https://opensource.org/licenses/MIT

# TODO switch to Config instead of users dict
from ypc.models import enums
from ypc.models.account import Account

accounts = {0: Account("Drainyyy", "abc", 0, enums.AccountType.basic, enums.AccountState.accepted)}


class Auth:
    """
    TODO documentation
    """

    def __init__(self, account: Account):
        self._username = account.username
        self._password = account.password
        self._uid = account.uid
        self._type = account.type
        self._status = account.state

    def login(self):
        account = accounts[self._uid] if self._uid in accounts else 404
        if account == 404:
            return None, 404

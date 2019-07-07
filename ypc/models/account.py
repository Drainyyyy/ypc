# -*- coding: utf-8 -*-

#  Copyright (c) 2019. Drainyyy
#  This project is covered by MIT License
#  https://opensource.org/licenses/MIT
from ypc.utilities import pwhandler
from .enums import AccountType, AccountStatus

__all__ = ["Account"]


class Account:
    """The model for any type of account.
    This account model can be configured to be admin, owner, etc.

    :param username: self-explaining
    :param password: The encrypted password of the account.
    :param uid: The unique identifier of the account.
    :param account_type: The type of the account (user, admin, etc.).
    :param account_status: The status of the account (banned, rejected, etc.).
    :type username: str
    :type password: str
    :type uid: int
    :type account_type: AccountType
    :type account_status: AccountStatus
    """

    __slots__ = ["username", "password", "uid", "type", "status"]

    def __init__(self, username: str, password: str, uid: int, account_type: AccountType, account_status: AccountStatus):
        self.username = username
        self.password = pwhandler.encrypt(password)
        self.uid = uid
        self.type = account_type
        self.status = account_status

    def __str__(self):
        return self.username

    def __repr__(self):
        representer = "<ypc.Account username={} password={} uid={} account_type={} account_status={}".format(
            self.username,
            self.password,
            self.uid,
            self.type,
            self.status
        )
        return representer

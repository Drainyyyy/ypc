# -*- coding: utf-8 -*-

#  Copyright (c) 2019. Drainyyy
#  This project is covered by MIT License
#  https://opensource.org/licenses/MIT
from ypc.models.account import Account

__all__ = ["AccountException"]


class AccountException(Exception):
    """Base exception for the account part of ypc.

    Could be used to handle every exception thrown in the account section of ypc.
    """

    pass


class AccountNotFoundException(AccountException):
    """Exception that is thrown whenever a requested account was not found.

    This can e.g. be triggered when an admin tries to ban an account that already left the chat.
    """

    def __init__(self, account: Account = None, *args):
        if account is not None:
            message = "The account with the following credentials was not found."

            super(AccountException, self).__init__(*args if args is not None else message, account.__repr__())
        else:
            message = "The requested account was not found."

            super().__init__(*args if args is not None else message)


class AccountNotPermittedException(AccountException):
    """This exception is thrown whenever an account tries to do something it is not allowed to.
    TODO documentation
    """

    def __init__(self, account: Account, *args):
        types = {
            0: "basic",
            1: "admin",
            2: "owner"
        }

        status = {
            0: "accepted",
            1: "rejected",
            2: "banned"
        }

        self.type = types[account.type]
        self.status = status[account.status]

        message = "The account has not enough permissions for the requested action."

        super().__init__(*args if args is not None else message, f"Account is from type '{self.type}'. Currently the account is '{self.status}'.")


class AccountBannedException(AccountException):
    """Thrown when an account is banned but want's to perform an action but is not allowed to because it's banned.

    This can be thrown for example when the account tries to login, but is banned. TODO finish
    """

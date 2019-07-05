# -*- coding: utf-8 -*-

#  Copyright (c) 2019. Drainyyy
#  This project is covered by MIT License
#  https://opensource.org/licenses/MIT

import typing

from ypc.utilities import pwhandler

__all__ = (
    "AcceptedAccount",
    "DefaultAccount",
    "AdminAccount",
    "OwnerAccount",
    "RejectedAccount"
)


class _BaseAccount:
    """Base model for every account type.

    :param username: Self-explaining
    :param password: Self-explaining
    :param uid: The unique identification number for each account on the server.
    :type username: str
    :type password: str
    :type uid: int
    """

    __slots__ = ["username", "password", "uid"]

    def __init__(self, username: str, password: str, uid: int):
        self.username = username
        self.password = pwhandler.encrypt(password)
        self.uid = uid


class AcceptedAccount(_BaseAccount):    # TODO restructure with account all in one class and AccountTypes
    """Model for an accepted account.

    Accepted accounts are accounts that got accepted to join the chat by an administrator of the server.

    :param admin: Indicator if the member is an administrator of the chat
    :param banned: Represents the ban status of the user
    :type admin: bool
    :type banned: bool
    """

    __slots__ = _BaseAccount.__slots__ + ["admin", "banned"]

    def __init__(self, username: str, password: str, uid: int, admin: bool = False, banned: bool = False):
        super().__init__(username, password, uid)
        self.admin = admin
        self.banned = banned


class DefaultAccount(AcceptedAccount):
    """Model for the default account type.

    This account type is for normal users. There are no special permissions or similar given.
    """

    def __init__(self, username: str, password: str, uid: int, banned: bool = False):
        super().__init__(username, password, uid, admin=False, banned=banned)

    def send(self, message):
        #   TODO sending messages
        return message


class AdminAccount(AcceptedAccount):
    """Model for the administrator account type.

    An administrator account can manage messages and administrate the chat.
    """

    def __init__(self, username: str, password: str, uid: int, banned: bool = False):
        super().__init__(username, password, uid, admin=True, banned=banned)

    def ban(self, member: DefaultAccount):
        member.banned = True
        # TODO make ban with reason
        return self.username


class OwnerAccount(AcceptedAccount):
    """Model for the account type of the server owner.

    The server owner can basically do everything, e.g. ban administrators, which administrator accounts can't.
    """

    def __init__(self, username: str, password: str, uid: int):
        super().__init__(username, password, uid)

    def ban(self, member: typing.Union[AdminAccount, DefaultAccount]):
        member.banned = True    # TODO make ban screen
        return self.username
    # TODO more functions


class RejectedAccount(AcceptedAccount):
    """Model for a rejected account.

    A rejected account is the account of a user that got rejected when registering (which equals applying) for the chat.
    """

    __slots__ = _BaseAccount.__slots__ + ["reason"]

    def __init__(self, username: str, password: str, uid: int, reason: str):
        super().__init__(username, password, uid)
        self.reason = reason

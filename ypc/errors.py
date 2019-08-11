# -*- coding: utf-8 -*-

#  Copyright (c) 2019. Drainyyy
#  This project is covered by MIT License
#  https://opensource.org/licenses/MIT

from ypc.models.client import Client

__all__ = ["ClientException"]


class ClientException(Exception):
    """Base exception for the client part of ypc.

    Could be used to handle every exception thrown in the client section of ypc.
    """

    pass


class ClientNotFoundException(ClientException):
    """Exception that is thrown whenever a requested client was not found.

    This can e.g. be triggered when an admin tries to ban an client that already left the chat.
    """

    def __init__(self, client: Client = None, *args):
        if client is not None:
            message = "The client with the following credentials was not found."

            super(ClientException, self).__init__(*args if args is not None else message, client.__repr__())
        else:
            pass


class ClientNotPermittedException(ClientException):
    """This exception is thrown whenever an client tries to do something it is not allowed to.

    Thrown for example if a member tries to ban a member with a higher rank.
    """

    def __init__(self, client: Client, *args):
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

        self.type = types[client.type]
        self.status = status[client.state]

        message = "The client has not enough permissions for the requested action."

        super().__init__(*args if args is not None else message, f"client is from type '{self.type}'. Currently the client is '{self.status}'.")


class ClientBannedException(ClientException):
    """Thrown when an client is banned but want's to perform an action but is not allowed to because it's banned.

    Can be thrown for instance when the client tries to login while being banned.
    """

    pass


class ClientMutedException(ClientException):
    """An exception that is being thrown if an client tries to do something it can not do while being muted.

    This can be the case, for example, if the user has been muted by an administrator and tries to send messages to the chat (or speak if voice
    support should be implemented).
    """

    pass


class ClientOfflineException(ClientException):
    """

    """

    pass

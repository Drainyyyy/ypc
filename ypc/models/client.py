# -*- coding: utf-8 -*-

#  Copyright (c) 2019. Drainyyy
#  This project is covered by MIT License
#  https://opensource.org/licenses/MIT
from ypc.utilities import pwhandler
from .enums import ClientType, ClientState, ClientStatus

__all__ = ["Client", "Bot"]


class Client:
    """The model for any type of client.
    This client model can be configured to be admin, owner, etc.

    :param username: self-explaining
    :param password: The encrypted password of the client.
    :param uid: The unique identifier of the client.
    :param client_type: Signalises the clients permissions as client model (user, admin, etc.).
    :param client_state: Current state of the client (banned, rejected, etc.).
    :param client_status: Indicator of the status of the client (muted, blocked, etc.).
    :type username: str
    :type password: str
    :type uid: int
    :type client_type: ClientType
    :type client_state: ClientState
    :type client_status: ClientStatus
    """

    __slots__ = ["username", "password", "uid", "type", "state", "status"]

    def __init__(self, username: str, password: str, uid: int, client_type: ClientType, client_state: ClientState, client_status: ClientStatus):
        self.username = username
        self.password = pwhandler.encrypt(password)
        self.uid = uid
        self.type = client_type
        self.state = client_state
        self.status = client_status    # TODO PB Support

    def __str__(self):
        return self.username

    def __repr__(self):
        representation = "<ypc.Client username={} password={} uid={} client_type={} client_state={} client_status={}>".format(
            self.username,
            self.password,
            self.uid,
            self.type,
            self.state,
            self.status
        )
        return representation

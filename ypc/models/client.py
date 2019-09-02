# -*- coding: utf-8 -*-

#  Copyright (c) 2019. Drainyyy
#  This project is covered by MIT License
#  https://opensource.org/licenses/MIT
from ypc.utilities import security
from .enums import ClientType, ClientState, ClientStatus

__all__ = ["Client", "Bot"]


class Client:
    """The model for any type of client.

    This model is used for every client in the chat (except bots).

    :param username: self-explaining
    :param password: The clients password.
    :param uid: The unique identifier of the client.
    :param client_type: Signalises the clients permissions as client model (user, admin, etc.).
    :param client_state: Current state of the client (banned, rejected, etc.).
    :param client_status: Social status of the client (muted, blocked, etc.).
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
        self.password = security.Encryption.encrypt(password)
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


class Bot:
    """The model for a programmable bot.

    This bot can be configured/programmed by using an API Wrapper (maybe I will write one some day) for the connection with the ypc endpoints.
    Feel free to write one yourself and maybe I will feature it in the documentation of ypc.

    :param username: self-explaining
    :param token: A unique token that replaces username and password.
                  Can be used to log in into the bots with an API Wrapper (for programming the bot).
    :param uid: A unique identifier for the specific client.
    :param owner: The client the bot is owned by.
    :param client_state: Current state of the bot (banned, rejected, etc.).
    :param client_status: Social status of the bot (muted, blocked, etc.).
    :param blocked_clients: A list of clients whose messages the client does't want to receive/read.
    :type username: str
    :type token: str
    :type uid: int
    :type owner: Client
    :type client_state: ClientState
    :type client_status: ClientStatus
    :type blocked_clients: list
    """

    __slots__ = ["username", "token", "uid", "owner", "state", "status", "blocked_clients"]

    def __init__(self, username: str, token: str, uid: int, owner: Client, client_state: ClientState, client_status: ClientStatus,
                 blocked_clients: list):
        self.username = username
        self.token = security.Encryption.encrypt(token)
        self.uid = uid
        self.owner = owner
        self.state = client_state
        self.status = client_status
        self.blocked_clients = blocked_clients

    def __str__(self):
        return self.username

    def __repr__(self):
        representation = "<ypc.Bot username={} token={} uid={} client_state={} client_status={}>".format(
            self.username,
            self.token,
            self.uid,
            self.state,
            self.status
        )

        return representation

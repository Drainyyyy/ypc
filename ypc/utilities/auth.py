# -*- coding: utf-8 -*-

#  Copyright (c) 2019. Drainyyy
#  This project is covered by MIT License
#  https://opensource.org/licenses/MIT

# TODO switch to Config instead of users dict
from ypc.models import enums
from ypc.models.client import Client
from ypc.models.enums import ClientStatus

clients = {0: Client("Drainyyy", "abc", 0, enums.ClientType.basic, enums.ClientState.accepted, ClientStatus.fine)}


class Auth:
    """
    TODO documentation
    """

    def __init__(self, client: Client):
        self._username = client.username
        self._password = client.password
        self._uid = client.uid
        self._type = client.type
        self._status = client.state

    def login(self):
        client = clients[self._uid] if self._uid in clients else 404
        if client == 404:
            return None, 404

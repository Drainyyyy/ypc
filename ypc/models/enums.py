# -*- coding: utf-8 -*-

#  Copyright (c) 2019. Drainyyy
#  This project is covered by MIT License
#  https://opensource.org/licenses/MIT

__all__ = ["ClientType", "ClientState", "ClientStatus", "MessageType"]


class ClientType:
    """The type represents the position of the user in the order of precedence.

    basic: The normal type you are when you join the chat for the first time. Member got no special permissions.
    admin: If you got the admin password, you can log in as administrator of the chat. Admin has permissions to manage the chat and users.
    owner: Owner is the client whose owner created the chat. Owner can manage the chat and users (including admins).
    """

    basic = 0
    admin = 1
    owner = 2


class ClientState:
    """The state represents in which state the client is.

    pending: In the time between the client requesting to join the server and the owner reviewing the client, the state is pending.
    accepted: Shows that the user got accepted for joining the chat by an administrator.
    rejected: The opposite of accepted. Shows that you got rejected for joining the chat by an administrator.
    banned: self-explaining
    """

    pending = 0
    accepted = 1
    rejected = 2
    banned = 3


class ClientStatus:
    """The status indicates the status of the permissions of the client.

    fine: The client is usable and has no penalties.
    muted: The client can not send messages anymore.
    """

    fine = 0
    muted = 1


class MessageType:
    """The type of message that is sent to the chat.

    user_message: A message with a clearly visible author.
    server_message: A message that is sent by a user but without visible author. Usable for rules or messages where the author isn't needed.
                    This type of message can only be sent by administrators.
    """

    user_message = 0
    server_message = 1

# -*- coding: utf-8 -*-

#  Copyright (c) 2019. Drainyyy
#  This project is covered by MIT License
#  https://opensource.org/licenses/MIT

__all__ = ["AccountType", "AccountState", "AccountStatus", "MessageType"]


class AccountType:
    """The type represents the position of the user in the order of precedence.

    basic: The normal type you are when you join the chat for the first time. Member got no special permissions.
    admin: If you got the admin password, you can log in as administrator of the chat. Admin has permissions to manage the chat and users.
    owner: Owner is the account whose owner created the chat. Owner can manage the chat and users (including admins).
    """

    basic = 0
    admin = 1
    owner = 2


class AccountState:
    """The state represents in which state the account is.

    accepted: Shows that the user got accepted for joining the chat by an administrator.
    rejected: The opposite of accepted. Shows that you got rejected for joining the chat by an administrator.
    banned: self-explaining
    """

    accepted = 0
    rejected = 1
    banned = 2


class AccountStatus:
    """The status indicates the status of the rights of the account.

    muted: The account can not send messages anymore.
    blocked: The member can neither send messages nor read messages.
    """

    muted = 0
    blocked = 1


class MessageType:
    """The type of message that is sent to the chat.

    user_message: A message that is clearly marked with the username and (if implemented) the profile picture. TODO add pb support
    server_message: A message that is sent by a user but marked as message without author. Usable for rules or messages where the author isn't needed.
                    This type of message can only be sent by administrators.
    """

    user_message = 0
    server_message = 1

# -*- coding: utf-8 -*-

#  Copyright (c) 2019. Drainyyy
#  This project is covered by MIT License
#  https://opensource.org/licenses/MIT

from datetime import datetime

from .enums import MessageType
from .client import Client
from ypc.utilities.formatter import timestamp_for_message

__all__ = ["Message", "Embed"]  # TODO make embed


class Message:
    """The model for every type of message that is sent to the chat.

    :param author: self-explaining
    :param timestamp: A timestamp for when the message was sent to the chat.
    :param message_id: The unique identifier of the corresponding message.
    :param pinned: Marks if the message is in the list of pinned messages. This is similar to saving a message. Messages can only be pinned by admins.
    :param content: self-explaining
    :param message_type: See :func:`MessageType <ypc.models.enums.MessageType>`
    """

    __slots__ = ["author", "sent_at", "id", "pinned", "content", "mentions", "type"]

    def __init__(self, author: Client, timestamp: datetime, message_id: int, pinned: bool, content: str, message_type: MessageType):
        self.author = author
        self.sent_at = timestamp_for_message(timestamp)
        self.id = message_id
        self.pinned = pinned
        self.content = content
        self.mentions = None    # TODO mentions
        self.type = message_type

    def __str__(self):
        return self.content

    def __repr__(self):
        representation = "<ypc.Message author={} send_at={} message_id={} pinned={} content={} message_type={}>".format(
            self.author,
            self.sent_at,
            self.id,
            self.pinned,
            self.content,
            self.type
        )
        return representation

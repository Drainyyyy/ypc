# -*- coding: utf-8 -*-

#  Copyright (c) 2019. Drainyyy
#  This project is covered by MIT License
#  https://opensource.org/licenses/MIT

from datetime import datetime

from ..utilities.color import Color
from .enums import MessageType
from .client import Client
from ..utilities.formatter import timestamp_for_message

__all__ = ["Message", "Embed"]


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

    def __init__(self, author: Client, content: str, timestamp: datetime, message_id: int, pinned: bool, message_type: MessageType):
        self.author = author
        self.content = content
        self.sent_at = timestamp_for_message(timestamp)
        self.id = message_id
        self.pinned = pinned
        self.mentions = None    # TODO mentions
        self.type = message_type

    def __str__(self):
        return self.content

    def __repr__(self):
        representation = "<ypc.Message author={} content={} timestamp={} message_id={} pinned={} mentions={} message_type={}>".format(
            self.author,
            self.content,
            self.sent_at,
            self.id,
            self.pinned,
            self.mentions,
            self.type
        )

        return representation


class Embed(Message):
    """A message with a special border on it. Also this message type has an addition title.

    Usable to mark special or important messages.
    """

    __slots__ = super().__slots__ + ["color", "title"]

    def __init__(self, author: Client, content: str, timestamp: datetime, message_id: int, pinned: bool, message_type: MessageType,
                 border_color: Color, title: str = None):
        super().__init__(author, content, timestamp, message_id, pinned, message_type)

        self.color = border_color
        self.title = title

    def __str__(self):
        return self.content

    def __repr__(self):
        representation = "<ypc.Embed author={} content={} timestamp={} message_id={} pinned={} message_type={} border_color={} title={}>".format(
            self.author,
            self.content,
            self.sent_at,
            self.id,
            self.pinned,
            self.type,
            self.color,
            self.title
        )

        return representation




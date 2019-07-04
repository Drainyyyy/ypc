#  Copyright (c) 2019. Drainyyy
#  This project is covered by MIT License
#  https://opensource.org/licenses/MIT

# -*- coding: utf-8 -*-
from datetime import datetime

from api.models.account import DefaultAccount

__all__ = ["UserMessage", "ServerMessage"]


class _BaseMessage:

    __slots__ = ["author", "timestamp", "content"]

    def __init__(self, author: DefaultAccount, timestamp: datetime.timestamp, content: str):
        self.author = author
        self.timestamp = timestamp
        self.content = content


class UserMessage:
    None

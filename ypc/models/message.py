# -*- coding: utf-8 -*-

#  Copyright (c) 2019. Drainyyy
#  This project is covered by MIT License
#  https://opensource.org/licenses/MIT

from datetime import datetime

from ypc.models.account import DefaultAccount, AdminAccount
from ypc.utilities.auth import Auth
from ypc.utilities.formatter import timestamp_for_message

__all__ = ("MemberMessage", "ManageMessage")


class MemberMessage:

    def __init__(self, author: DefaultAccount, timestamp: datetime, message_id: int, pinned: bool, content: str):
        self.author = author
        self.created_at = timestamp_for_message(timestamp)
        self.id = message_id    # TODO automated id
        self.pinned = pinned
        self.content = content
        self.mentions = None    # TODO mentions

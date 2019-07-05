# -*- coding: utf-8 -*-

#  Copyright (c) 2019. Drainyyy
#  This project is covered by MIT License
#  https://opensource.org/licenses/MIT

import datetime

# TODO documentation!!!
def timestamp_for_message(timestamp: datetime.datetime):
    formatted = timestamp.strftime("%Y-%m-%d ~ %H:%M")
    return formatted

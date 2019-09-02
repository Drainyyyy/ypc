# -*- coding: utf-8 -*-

#  Copyright (c) 2019. Drainyyy
#  This project is covered by MIT License
#  https://opensource.org/licenses/MIT

from datetime import datetime


def timestamp_for_message(timestamp: datetime):
    """A formatter that formats a timestamp into a special format.

    The timestamp get's formatted into "day-month-year ~ hour:minute".
    Example: The "15th August 2019 22:08 O'Clock" would be "15-8-2019 ~ 22:08"

    :param timestamp:
    :type timestamp: datetime
    :return:
    """

    formatted = timestamp.strftime("%d-%m-%Y ~ %H:%M")
    return formatted

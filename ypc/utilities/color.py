# -*- coding: utf-8 -*-

#  Copyright (c) 2019. Drainyyy
#  This project is covered by MIT License
#  https://opensource.org/licenses/MIT

__all__ = ["Rgb", "Color"]
# TODO add hex etc. support


class Rgb:
    """A class representing three integers that form a color.
    The values can each be an int between 0 and 255. If a value is higher than 255 it will be set to 255 and if it is less than 0 it will be set to 0.

    :param r: The value for the color red.
    :param g: The value for the color green.
    :param b: The value for the color blue.
    :type r: int
    :type g: int
    :type b: int
    """

    __slots__ = ["red", "green", "blue"]

    def __init__(self, r: int, g: int, b: int):
        self.red = self.check_value(r)
        self.green = self.check_value(g)
        self.blue = self.check_value(b)

    def __str__(self):
        return Rgb.__repr__(self)

    def __repr__(self):
        representation = "<ypc.Rgb r={} g={} b={}>".format(self.red, self.green, self.blue)
        return representation

    @staticmethod
    def check_value(value: int):
        """Check if a value is higher than 255 or less than 0. If so it will be set to 255/0."""

        if value > 255:
            value = 255
        elif value < 0:
            value = 0
        return value


class Color:
    """A class containing presets of colors and custom color generator.

    Custom colors can currently only be made from rgb values.
    """

    __slots__ = []

    black = Rgb(0, 0, 0)
    white = Rgb(255, 255, 255)
    red = Rgb(255, 0, 0)
    green = Rgb(0, 255, 0)
    blue = Rgb(0, 0, 255)
    pink = Rgb(255, 192, 203)
    orange = Rgb(255, 165, 0)
    yellow = Rgb(255, 255, 0)
    brown = Rgb(165, 42, 42)

    @staticmethod
    def custom(rgb: Rgb):
        return rgb

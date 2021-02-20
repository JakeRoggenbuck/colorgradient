import math
import numpy as np
from typing import Tuple, Union, List


RGB = Tuple[int, int, int]


class FadeColors:
    def __init__(self, colors: List[str]):
        self.hex_colors = colors
        self.rgb_colors = [self.hex2rgb(h) for h in self.hex_colors]
        self.red, self.green, self.blue = self.get_channels(self.rgb_colors)

    @staticmethod
    def hex2rgb(h: str) -> RGB:
        return tuple(int(h[i : i + 2], 16) for i in (0, 2, 4))

    @staticmethod
    def get_channels(rgb: List[RGB]) -> Tuple[List[int], List[int], List[int]]:
        return map(list, zip(*rgb))

    @staticmethod
    def find_slope(x1: int, y1: int, x2: int, y2: int) -> float:
        return (y2 - y1) / (x2 - x1)

    @staticmethod
    def part(x: int) -> Tuple[int, int]:
        return math.floor(x), math.ceil(x)

    @staticmethod
    def find_y(x: Union[int, float], known_x: List[int]):
        if round(x) == x:
            return known_x[int(x)]

        left_x, right_x = FadeColors.part(x)

        left_y = known_x[left_x]
        right_y = known_x[right_x]

        slope = FadeColors.find_slope(left_x, left_y, right_x, right_y)

        return abs(round(left_y + (slope * (x - left_x))))

    def get_rgb(self, x: Union[int, float]) -> RGB:
        r = self.find_y(x, self.red)
        g = self.find_y(x, self.green)
        b = self.find_y(x, self.blue)
        return r, g, b

    def get_colors(self, quantity: int):
        for x in np.arange(0.0, 8.0, 8 / quantity):
            print(f"rgb{self.get_rgb(x)}")

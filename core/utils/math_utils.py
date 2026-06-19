import math


class MathUtils:

    @staticmethod
    def clamp(value, min_v, max_v):

        return max(min_v, min(value, max_v))

    ########################################################

    @staticmethod
    def deg_to_rad(deg):

        return deg * math.pi / 180.0

    ########################################################

    @staticmethod
    def safe_div(a, b):

        return a / b if b != 0 else 0
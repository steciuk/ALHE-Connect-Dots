import numpy as np


def sort_array_by_gain_asc(points):
    """
    :param points: [n * [x1, x2, x3, ..., xd, q]] where q is the gain of a point
    :return: sorted array
    """
    return points[points[:, -1].argsort()]

import numpy as np
from config import gain_func
from utils.sorts import sort_array_by_gain_asc


def generate(n, d=2, low=-1, high=1):
    """
    Generate n d-dimensional points with U[low, high] distribution of coordinates
    :param n: number of points
    :param d: dimensions of each point
    :param low: lowest coord
    :param high: highest coord
    :return: points = [n * [x1, x2, x3, ..., xd, q]] where q is the gain of a point
    """
    points = np.random.uniform(low=low, high=high, size=(n, d+1))
    for point in points:
        point[d] = gain_func(point)

    return sort_array_by_gain_asc(points)


if __name__ == '__main__':
    a = generate(2, 2)
    print(a)

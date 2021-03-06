import numpy as np
from utils.sorts import sort_array_by_gain_asc


def calc_mid_points(points, median=False):
    """
    Calc midpoints of points, each time removing worst rated point
    :param points: [n * [x1, x2, x3, ..., xd, q]] where q is the gain of a point
    :param median: if set to True use median instead of mean
    :return: array of midpoints sorted in calc order (midpoint[0] calc for n points, midpoint[-1] calc for dim+1 points)
    """
    points = sort_array_by_gain_asc(points)
    dim = points.shape[1] - 1
    p = points

    midpoints = []
    while p.shape[0] > dim:
        if median:
            midpoints.append(_calc_mid_point_median(p))
        else:
            midpoints.append(_calc_mid_point_mean(p))
        p = np.delete(p, 0, axis=0)

    return np.array(midpoints)


def _calc_mid_point_mean(points):
    return np.mean(points[:, :-1], axis=0)


def _calc_mid_point_median(points):
    return np.median(points[:, :-1], axis=0)


# for testing
if __name__ == '__main__':
    print(calc_mid_points(np.array([
        [100, 1, 1],
        [2, 2, 100],
        [0, 100, 15],
        [2, 6, 100]
    ])))

from scipy.optimize import fmin
from config import gain_func
import numpy as np


def approx_maximum(dim, start_point=None):
    """
    :param dim: number of dimensions
    :param start_point: [optional: from where start searching for optimum]
    :return: nd.array of dim size with maximum estimation
    """
    if start_point:
        return fmin(lambda x: -gain_func(x), start_point)
    else:
        return fmin(lambda x: -gain_func(x), np.zeros(dim))


# for_testing
if __name__ == '__main__':
    print(type(approx_maximum(2)))

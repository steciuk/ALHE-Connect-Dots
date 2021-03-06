import numpy as np


def gain_func(point):
    """
    Define gain function here
    """
    # q = - (np.tanh(point[0]) ** 2 + point[1] ** 2)
    # q = -((point[0]+0.5) ** 2 + point[1] ** 2)
    # q = -(point[0] ** 2 + point[1] ** 2)
    # q = -(point[0] ** 2 + point[1] ** 3)
    # q = -((point[0]) ** 2 + (point[1]) ** 2)
    # q = -((point[0]+1) ** 2 + (point[1]+0.2) ** 2) - ((point[0]-1) ** 2 + (point[1]-1) ** 2)
    # q = q = -((0.5-point[0])**2 + 100*(point[1] - point[0]**2)**2)
    # q = -((0.5-point[0])**2 + 100*(point[1] - point[0]**2)**2) + 50*((point[0]) ** 2 + (point[1]+0.2) ** 2)
    # q = 20 + point[0]**2 - 10*np.cos(2*np.pi*point[0]) + point[1]**2 - 10*np.cos(2*np.pi*point[1])
    # q = -((point[0]-0.5)**2 + (point[1]-0.25)**2 + (point[2]-0.4)**2)
    q = square_func(point)
    return q


PLOT_RES = 100


def square_func(point):
    result = 0
    for i, coord in enumerate(point):
        result += coord ** 2

    return -result

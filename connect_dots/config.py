def gain_func(point):
    """
    Define gain function here
    """
    # q = - (np.tanh(point[0]) ** 2 + point[1] ** 2)
    # q = -((point[0]+0.5) ** 2 + point[1] ** 2)
    # q = -(point[0] ** 2 + point[1] ** 2)
    # q = -(point[0] ** 2 + point[1] ** 3)
    q = -((point[0]+2) ** 2 + (point[1]+2) ** 2)

    return q


PLOT_RES = 100

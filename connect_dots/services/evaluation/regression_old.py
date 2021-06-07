import numpy as np

import services.evaluation.error_values
import services.evaluation.regression
import services.evaluation.distance
from utils.plotter import simplePlot
from config import gain_func


def regression_by_gain_func(mid_points, maximum):
    """
    Calculates regression of gain function over points
    Evaluates calculated prediction
    :param mid_points: list of points
    :param maximum: true optimum, parameter used for evaluation of the prediction
    """
    mid_points_scores = []
    distance_list = []
    error_list = []
    for m in mid_points:
        mid_points_scores.append(gain_func(m))
    for i in range(3, len(mid_points)):
        lin_reg = services.evaluation.regression.calc_regression(mid_points[:i], mid_points_scores[:i])
        line = lin_reg.coef_.tolist()
        line.append(lin_reg.intercept_)
        distance_list.append(services.evaluation.error_values.distance_2d(line, maximum))
        error_list.append(services.evaluation.error_values.calc_error(line, maximum, gain_func(maximum)))

    simplePlot(distance_list, pltTitle="Odleglosci od prostej wyznaczonej przez regresje", pltName='dist')
    simplePlot(error_list, pltTitle="Blad bezwgledny predykcji w maximum globalnym", pltName='errors')
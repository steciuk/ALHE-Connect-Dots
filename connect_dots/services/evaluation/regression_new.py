import numpy as np

import services.evaluation.regression
from services.evaluation.distance import calc_distance
from utils.plotter import simplePlot, advancedPlot
from config import gain_func


def regression_correct(mid_points, maximum, dim, plot_for_each=True):
    """
    Predicts optimum using linear regression over the percentage of discarded points
    The function evaluates the prediction and draws plots
    :param mid_points: list of points
    :param maximum: true optimum, parameter used for evaluation of the prediction
    :param dim: number of dimensions
    :param plot_for_each: True if draw plot for every dimension, False if draw only one main plot
    """
    optimum = []
    predict_list = []  # list of predicted values for each dim, in every iteration
    if dim > 7:
        plot_for_each = False

    for d in range(dim):
        percentages = [1]
        predict_list.append([])
        for i in range(2, len(mid_points)):
            percentages.append(1 - i / (len(mid_points) - 1))
            lin_reg = services.evaluation.regression.calc_regression([percentages], [mid_points[:i, d]], trans=True)
            predict_list[-1].append(lin_reg.intercept_[0])
        optimum.append(predict_list[-1][-1])

    predict_list = np.array(predict_list)
    if plot_for_each:
        for d in range(dim):
            pred_dist = []
            for m in range(len(predict_list[0])):
                pred_dist.append(np.abs(predict_list[d, m] - maximum[d]))
            simplePlot(pred_dist, pltTitle="Odleglosc od optimum w wymiarze " + str(d + 1) +
                                           " (regresja po % odrzuconych)", pltName='pred_dist_in_dim' + str(d))
    else:
        pred_dist = []
        for m in range(len(predict_list[0])):
            point = predict_list[:, m].tolist()
            pred_dist.append(calc_distance(point, maximum))
        simplePlot(pred_dist, pltTitle="Odleglosc predykcji od optimum (regresja po % odrzuconych)",
                   pltName="pred_dist_global")
    return optimum


def mean_correct(mid_points, maximum, dim, plot_for_each=True):
    """
    Predicts optimum using averaging given points
    The function evaluates the prediction and draws plots
    :param mid_points: list of points
    :param maximum: true optimum, parameter used for evaluation of the prediction
    :param dim: number of dimensions
    :param plot_for_each: True if draw plot for every dimension, False if draw only one main plot
    """
    optimum = []
    mean_predict_list = []  # list of predicted values for each dim, in every iteration
    if dim > 7:
        plot_for_each = False

    for d in range(dim):
        percentages = [1]
        mean_predict_list.append([])
        for i in range(2, len(mid_points)):
            percentages.append(1 - i / (len(mid_points) - 1))
            mean_predict_list[-1].append(np.mean(mid_points[:i, d]))
        optimum.append(mean_predict_list[-1][-1])

    mean_predict_list = np.array(mean_predict_list)
    if plot_for_each:
        for d in range(dim):
            mean_dist = []
            for m in range(len(mean_predict_list[0])):
                mean_dist.append(np.abs(mean_predict_list[d, m] - maximum[d]))
            simplePlot(mean_dist, pltTitle="Odleglosc od optimum w wymiarze " + str(d + 1) + " (usrednienie midpointow)",
                       pltName='mean_dist_in_dim' + str(d))
    else:
        mean_pred_dist = []
        for m in range(len(mean_predict_list[0])):
            point = mean_predict_list[:, m].tolist()
            mean_pred_dist.append(calc_distance(point, maximum))
        simplePlot(mean_pred_dist, pltTitle="Odleglosc predykcji od optimum (usrednienie midpointow)",
                   pltName="mean_pred_dist_global")
    return optimum


def gain_regression_correct(mid_points, dim):
    """
    Predicts optimum using linear regression over the percentage of discarded points
    The function calculates gain_function for successive points and draws a plot
    :param mid_points: list of points
    :param dim: number of dimensions
    """
    predict_list = []  # list of predicted values for each dim, in every iteration

    for d in range(dim):
        percentages = [1]
        predict_list.append([])
        for i in range(2, len(mid_points)):
            percentages.append(1 - i / (len(mid_points) - 1))
            lin_reg = services.evaluation.regression.calc_regression([percentages], [mid_points[:i, d]], trans=True)
            predict_list[-1].append(lin_reg.intercept_[0])

    predict_list = np.array(predict_list)
    pred_dist = []
    best_point = predict_list[:, 0].tolist()
    best_value = gain_func(best_point)
    best_id = 0
    for m in range(len(predict_list[0])):
        point = predict_list[:, m].tolist()
        pred_dist.append(gain_func(point))
        if best_value < pred_dist[-1]:
            best_value = pred_dist[-1]
            best_point = point
            best_id = m
    advancedPlot(pred_dist, pltTitle="Funkcja " + str(dim) + " wymiarowa",
                pltName="gain_func_regression", best_val=best_value, best_id=best_id)
    return best_point


def find_best_point_in_population(points):
    """
    Finds best point in the population
    :param points: list of point in the population
    """
    best = points[0]
    best_gain = gain_func(points[0])
    for p in points:
        p = p[:-1]
        if gain_func(p) > best_gain:
            best_gain = gain_func(p)
            best = p
    return best


def find_best_ever(mid_points, dim, maximum):
    """
    Calculates regression for ech dimension
    In each dimension it takes the closest value to maximum that ever was achieved by regression
    Predicts optimum using averaging given points
    The function evaluates the prediction and draws plots
    :param mid_points: list of points
    :param maximum: true optimum, parameter used for evaluation of the prediction
    :param dim: number of dimensions
    """
    predict_list = []  # list of predicted values for each dim, in every iteration

    for d in range(dim):
        percentages = [1]
        predict_list.append([])
        for i in range(2, len(mid_points)):
            percentages.append(1 - i / (len(mid_points) - 1))
            lin_reg = services.evaluation.regression.calc_regression([percentages], [mid_points[:i, d]], trans=True)
            predict_list[-1].append(lin_reg.intercept_[0])

    predict_list = np.array(predict_list)
    optimum = []
    for d in range(dim):
        coordinate = predict_list[d][0]
        biggest_distance = np.abs(maximum[d] - predict_list[d][0])
        for i in range(len(predict_list[d])):
            if biggest_distance > np.abs(maximum[d] - predict_list[d][i]):
                biggest_distance = np.abs(maximum[d] - predict_list[d][i])
                coordinate = predict_list[d][i]
        optimum.append(coordinate)

    return optimum

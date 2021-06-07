import numpy as np

import services.evaluation.regression
from utils.plotter import simplePlot


def regression_correct(mid_points, maximum, dim):
    """
    Predicts optimum using linear regression over the percentage of discarded points
    The function evaluates the prediction and draws plots
    :param mid_points: list of points
    :param maximum: true optimum, parameter used for evaluation of the prediction
    :param dim: number of dimensions
    """
    optimum = []
    predict_list = []  # list of predicted values for each dim, in every iteration

    for d in range(dim):
        percentages = [1]
        predict_list.append([])
        for i in range(2, len(mid_points)):
            percentages.append(1 - i / (len(mid_points) - 1))
            lin_reg = services.evaluation.regression.calc_regression([percentages], [mid_points[:i, d]], trans=True)
            predict_list[-1].append(lin_reg.intercept_[0])
        optimum.append(predict_list[-1][-1])

    predict_list = np.array(predict_list)
    for d in range(dim):
        pred_dist = []
        for m in range(len(predict_list[0])):
            pred_dist.append(np.abs(predict_list[d, m] - maximum[d]))
        simplePlot(pred_dist, pltTitle="Odleglosc od optimum w wymiarze " + str(d + 1) + " (regresja po % odrzuconych)",
                   pltName='pred_dist_in_dim' + str(d))
    return optimum

def mean_correct(mid_points, maximum, dim):
    """
    Predicts optimum using averaging given points
    The function evaluates the prediction and draws plots
    :param mid_points: list of points
    :param maximum: true optimum, parameter used for evaluation of the prediction
    :param dim: number of dimensions
    """
    optimum = []
    mean_predict_list = []  # list of predicted values for each dim, in every iteration

    for d in range(dim):
        percentages = [1]
        mean_predict_list.append([])
        for i in range(2, len(mid_points)):
            percentages.append(1 - i / (len(mid_points) - 1))
            mean_predict_list[-1].append(np.mean(mid_points[:i, d]))
        optimum.append(mean_predict_list[-1][-1])

    mean_predict_list = np.array(mean_predict_list)
    for d in range(dim):
        mean_dist = []
        for m in range(len(mean_predict_list[0])):
            mean_dist.append(np.abs(mean_predict_list[d, m] - maximum[d]))
        simplePlot(mean_dist, pltTitle="Odleglosc od optimum w wymiarze " + str(d + 1) + " (usrednienie midpointow)",
                   pltName='mean_dist_in_dim' + str(d))

    return optimum

import argh
from utils.file_menager import csv_to_array, clear_dir
from services.calc_mid_points import calc_mid_points
from utils.plotter import plot2d, simplePlot
from utils.max_approx import approx_maximum

import services.evaluation.error_values
import services.evaluation.regression
import services.evaluation.distance
import services.evaluation.regression_old
import services.evaluation.regression_new
from config import gain_func
import numpy as np


def run(file_name):
    """
    Runs 'connect dots' algorithm and save result plots in './plots' directory
    :param file_name: name of the '.csv' (without extension name) file in './data' directory containing points coords and gain function values
    """
    p0 = csv_to_array(file_name)  # read points and their gain
    dim = p0.shape[1] - 1
    maximum = approx_maximum(dim)  # search for maximum approx
    mid_points = calc_mid_points(p0)
    clear_dir('plots')

    # services.evaluation.regression_old.regression_by_gain_func(mid_points, maximum)
    # services.evaluation.regression_new.regression_correct(mid_points, maximum, dim)
    # services.evaluation.regression_new.mean_correct(mid_points, maximum, dim)
    best_point = services.evaluation.regression_new.gain_regression_correct(mid_points, dim)
    print("best point:", best_point)
    print("best value:", gain_func(best_point))

    if(p0.shape[1]) == 3:
        plot2d(p0, mid_points)


if __name__ == '__main__':
    argh.dispatch_command(run)


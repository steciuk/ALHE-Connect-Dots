import argh
from utils.file_menager import csv_to_array
from services.calc_mid_points import calc_mid_points
from utils.plotter import plot2d, simplePlot  # dodalem simplePlot
from utils.max_approx import approx_maximum

##########dodane
import evaluation.errorValues
import evaluation.regression
from config import gain_func
import numpy as np


##########

def run(file_path):
    p0 = csv_to_array(file_path)  # read points and their gain

    dim = p0.shape[1] - 1
    maximum = approx_maximum(dim)  # search for maximum approx

    mid_points = calc_mid_points(p0)

    ###########
    mid_points_scores = []
    distance_list = []
    error_list = []
    for m in mid_points:
        mid_points_scores.append(gain_func(m))
    for i in range(2, len(mid_points)):
        lin_reg = evaluation.regression.calc_regression(mid_points[:i], mid_points_scores[:i])
        line = lin_reg.coef_.tolist()
        line.append(lin_reg.intercept_)
        distance_list.append(evaluation.errorValues.distance2D(line, maximum, lin_reg.predict(np.array([maximum]))))
        error_list.append(evaluation.errorValues.calcError(line, maximum, lin_reg.predice(np.array([maximum]))))

    simplePlot(distance_list, pltTitle="Odleglosci od prostej wyznaczonej przez regresje")
    simplePlot(distance_list, pltTitle="Blad bezwgledny predykcji w maximum globalnym")
    ###########

    plot2d(p0, mid_points)


if __name__ == '__main__':
    # argh.dispatch_command(run)
    run('files/test.csv')  # for testing

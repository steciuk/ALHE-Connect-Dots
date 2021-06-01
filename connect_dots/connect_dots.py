# import argh
from utils.file_menager import csv_to_array
from services.calc_mid_points import calc_mid_points
from utils.plotter import plot2d, simplePlot  # dodalem simplePlot
from utils.max_approx import approx_maximum

# dodane
import evaluation.errorValues
import evaluation.regression
import evaluation.distance
from config import gain_func
import numpy as np


#

def run(file_path):
    p0 = csv_to_array(file_path)  # read points and their gain

    dim = p0.shape[1] - 1
    maximum = approx_maximum(dim)  # search for maximum approx
    print("m", maximum)

    mid_points = calc_mid_points(p0)

    ###########
    mid_points_scores = []
    distance_list = []
    error_list = []
    for m in mid_points:
        mid_points_scores.append(gain_func(m))
    for i in range(3, len(mid_points)):
        lin_reg = evaluation.regression.calc_regression(mid_points[:i], mid_points_scores[:i])
        line = lin_reg.coef_.tolist()
        line.append(lin_reg.intercept_)
        distance_list.append(evaluation.errorValues.distance_2d(line, maximum, lin_reg.predict(np.array([maximum]))[0]))
        error_list.append(evaluation.errorValues.calc_error(line, maximum, gain_func(maximum)))

    simplePlot(distance_list, pltTitle="Odleglosci od prostej wyznaczonej przez regresje")
    simplePlot(error_list, pltTitle="Blad bezwgledny predykcji w maximum globalnym")
    ###########

    optimum = []
    mean_predict_list = []
    predict_list = []  # list of predicted values for each dim, in every iteration

    for d in range(dim):
        percentages = [1]
        predict_list.append([])
        mean_predict_list.append([])
        for i in range(2, len(mid_points)):
            percentages.append(1 - i/(len(mid_points)-1))
            lin_reg = evaluation.regression.calc_regression([percentages], [mid_points[:i, d]], trans=True)
            predict_list[-1].append(lin_reg.intercept_[0])
            mean_predict_list[-1].append(np.mean(mid_points[:i, d]))
        optimum.append(predict_list[-1][-1])

    predict_list = np.array(predict_list)
    for d in range(dim):
        pred_dist = []
        for m in range(len(predict_list[0])):
            pred_dist.append(np.abs(predict_list[d, m] - maximum[d]))
        simplePlot(pred_dist, pltTitle="Odleglosc od optimum w wymiarze " + str(d+1) + " (regresja po % odrzuconych)")

    mean_predict_list = np.array(mean_predict_list)
    for d in range(dim):
        mean_dist = []
        for m in range(len(mean_predict_list[0])):
            mean_dist.append(np.abs(mean_predict_list[d, m] - maximum[d]))
        simplePlot(mean_dist, pltTitle="Odleglosc od optimum w wymiarze " + str(d+1) + " (usrednienie midpointow)")
    # print(found_list)

    print(optimum)
    print(evaluation.distance.calc_distance(maximum, optimum))

    ###########

    plot2d(p0, mid_points)


if __name__ == '__main__':
    # argh.dispatch_command(run)
    run('files\\test.csv')  # for testing
    # pass

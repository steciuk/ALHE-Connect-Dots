import argh
from utils.file_menager import csv_to_array
from services.calc_mid_points import calc_mid_points
from utils.plotter import plot2d
from utils.max_approx import approx_maximum


def run(file_path):
    p0 = csv_to_array(file_path)  # read points and their gain

    dim = p0.shape[1] - 1
    maximum = approx_maximum(dim)  # search for maximum approx

    mid_points = calc_mid_points(p0)
    plot2d(p0, mid_points)


if __name__ == '__main__':
    # argh.dispatch_command(run)
    run('files/test.csv')  # for testing

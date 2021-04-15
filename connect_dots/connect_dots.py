import argh
from utils.file_menager import csv_to_array
from services.calc_mid_points import calc_mid_points


def run(file_path):
    p0 = csv_to_array(file_path)
    mid_points = calc_mid_points(p0)


if __name__ == '__main__':
    # argh.dispatch_command(run)
    run('files/test.csv')  # for testing

import argh
from services.generate import generate
from utils.file_menager import array_to_csv


def run(file_name, n=100, d=2, bottom=-1.0, top=1.0):
    """
    Generate n d-dimensional points with U[bottom, top] distribution of coordinates
    Calculates gain value for each of them
    Saves generated points to 'file_name.csv' file in './data' directory
    Specify gain function in 'config.py'
    :param file_name: path and name of the result .csv file
    :param n: number of points
    :param d: dimensions of each point
    :param bottom: lowest coord
    :param top: highest coord
    """
    p0 = generate(n, d, bottom, top)
    array_to_csv(file_name, p0)


if __name__ == '__main__':
    argh.dispatch_command(run)

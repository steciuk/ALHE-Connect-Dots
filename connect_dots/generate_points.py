import argh
from services.generate import generate
from utils.file_menager import array_to_csv


def run(file_name, n=100, d=2, low=-1, high=1):
    """
    Generate n d-dimensional points with U[low, high] distribution of coordinates
    Calculates gain value for each of them
    Saves generated points to 'file_name.csv' file in './data' directory
    Specify gain function in 'config.py'
    :param file_name: path and name of the result .csv file
    :param n: number of points
    :param d: dimensions of each point
    :param low: lowest coord
    :param high: highest coord
    """
    p0 = generate(n, d, low, high)
    array_to_csv(file_name, p0)


if __name__ == '__main__':
    argh.dispatch_command(run)

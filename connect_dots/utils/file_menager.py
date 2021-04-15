import numpy as np
from os.path import join
from definitions import ROOT_DIR


def array_to_csv(file_path, array):
    np.savetxt(join(ROOT_DIR, file_path), array, delimiter=",")


def csv_to_array(file_path):
    return np.genfromtxt(join(ROOT_DIR, file_path), delimiter=",")

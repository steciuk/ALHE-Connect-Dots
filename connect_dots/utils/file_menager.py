import numpy as np
from os.path import join, exists
from os import makedirs
from definitions import ROOT_DIR


def array_to_csv(file_name, array):
    path = join(ROOT_DIR, 'data')
    if not exists(path):
        makedirs(path)
    np.savetxt(join(path, file_name + '.csv'), array, delimiter=",")


def csv_to_array(file_name):
    path = join(ROOT_DIR, 'data', file_name + '.csv')
    return np.genfromtxt(path, delimiter=",")


def save_plot(file_name, plt):
    path = join(ROOT_DIR, 'plots')
    if not exists(path):
        makedirs(path)
    plt.savefig(join(path, file_name + '.png'))

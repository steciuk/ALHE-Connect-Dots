import os
import matplotlib.pyplot as plt
import numpy as np
from config import gain_func
from config import PLOT_RES
from utils.file_menager import save_plot


def plot2d(points, mid_points=None):
    if points.shape[1] != 3:
        raise Exception('Points dimension not 2!')
    if mid_points.shape[1] != 2:
        raise Exception('MidPoints dimension not 2!')

    # plot heatmap of gain function
    x_max, y_max = points[:, :2].max(axis=0)
    x_min, y_min = points[:, :2].min(axis=0)
    res_x = (x_max - x_min) / PLOT_RES
    res_y = (y_max - y_min) / PLOT_RES
    m = np.arange(x_min, x_max + res_x, res_x)
    p = np.arange(y_min, y_max + res_y, res_y)
    x, y = np.meshgrid(m, p)
    z = gain_func([x, y])
    plt.figure()
    plt.pcolormesh(x, y, z, cmap='viridis', alpha=1, shading='auto')
    plt.colorbar()

    # plot used points
    plt.scatter(points[:, 0], points[:, 1], color='#ff82f0', s=10)

    # plot midpoints
    plt.scatter(mid_points[:, 0], mid_points[:, 1], color='red', s=10)

    plt.margins(0)
    plt.grid(False)
    save_plot('points_map', plt)


def simplePlot(values, legend=None, pltTitle=None, pltName='plot'):
    plt.figure()
    plt.plot(values, label=legend)
    plt.title(pltTitle)
    if legend:
        plt.legend()
    save_plot(pltName, plt)


def advancedPlot(values, best_id, best_val, legend=None, pltTitle=None, pltName='plot'):
    x_label = []
    for i in range(len(values)):
        x_label.append(i/len(values))
    best_id /= len(values)
    plt.plot(x_label, values, label=legend)
    plt.plot(best_id, best_val, 'ro')
    plt.xlabel("Ulamek wykorzystanych punktow")
    plt.ylabel("Wartosc funkcji celu")
    plt.title(pltTitle)
    if legend:
        plt.legend()
    save_plot(pltName, plt)


# for testing
if __name__ == '__main__':
    plot2d(np.array([
        [100, 1, 1],
        [2, 2, 30],
        [0, 25, 15],
        [2, 6, 8]
    ]))

import numpy as np


def calc_distance(p1, p2):
    s = 0
    w1 = w2 = 0
    while w1 < len(p1) or w2 < len(p2):
        val1 = p1[w1] if w1 < len(p1) else 0
        val2 = p2[w2] if w2 < len(p2) else 0
        s += (val1 - val2)**2
        w1 += 1
        w2 += 1
    return np.sqrt(s)

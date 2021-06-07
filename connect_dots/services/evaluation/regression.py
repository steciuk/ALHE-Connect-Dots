import pandas as pd
import numpy as np
import sympy
from sklearn.linear_model import LinearRegression


def calc_regression(midpoints, scores=None, trans=False):
    """
    Calculates regression for last coordinate or score (if given)
    Returns an object of class LinearRegression()
    :param midpoints: list of points
    :param scores: values of gain function for each point
    :param trans: True if list of points and list of scores require transposition
    """
    if trans and scores is not None:
        midpoints = np.array(midpoints).transpose()
        scores = np.array(scores).transpose()
        return LinearRegression().fit(midpoints, scores)

    midpoints = np.array(midpoints).tolist()
    if scores is not None:
        for i in range(len(midpoints)):
            midpoints[i].append(scores[i])
    df = pd.DataFrame(midpoints)
    x = df.iloc[:, :-1]  # takes values for further estimations
    y = df.iloc[:, -1]  # takes values to fit to
    lin_reg = LinearRegression()
    lin_reg.fit(x, y)
    return lin_reg

    # return (lin_reg.coef_).tolist(), lin_reg.intercept_  #zwraca parametry regresji liniowej oraz bazową warość


def prep_for_sympy(poly):
    """
    Returns the polynomial in text format, which than can by used by sympy.solve()
    :param poly: polynomial represented by a list of factors
    """
    s = ""
    stopien = len(poly) - 1
    for p in poly:
        s += str(p)
        if stopien > 1:
            s += "*x**" + str(stopien) + " + "
        elif stopien == 1:
            s += "*x + "
        stopien -= 1
    return s


def calc_der_for_each(midpoints):
    """
    Calculates derivative for each coordinate separately
    :param midpoints: list of points
    """
    df = pd.DataFrame(midpoints)
    sz = df.shape[1] - 1
    ders = []
    for i in range(df.shape[1] - 1):
        f = np.polyfit(df[i].tolist(), df[sz].tolist(), 3).tolist()  # third degree function
        f.reverse()
        for j in range(len(f) - 1):  # calculate simple derivative
            f[j] = f[j + 1] * (j + 1)
        f.pop()
        f.reverse()
        ders.append(f)
    return ders


def find_solutions(derivatives):
    """
    Finds local maximums for each derivative
    Every derivative should be represented as a list of factors
    Returns a list of lists
    Each list contains maximums for each derivative
    :param derivatives: list of derivatives
    """
    solutions = []
    for d in derivatives:
        solu = sympy.solve(prep_for_sympy(d))
        saved_solu = []

        # check if maximum or minimum
        dd = d
        dd.reverse()
        for j in range(len(dd) - 1):  # calculate second derivative
            dd[j] = dd[j + 1] * (j + 1)
        dd.pop()
        dd.reverse()
        for s in solu:
            val = 0
            for x in dd:
                val *= s
                val += x
            if sympy.sympify(val).is_real and val < 0:  # maximum
                saved_solu.append(s)
        solutions.append(saved_solu)
    return solutions


###Funkcje poniżej robia predykcje współrzędnej punktu - być może zaszłaby taka potrzeba, gdyby jakichś danych brakowało

def calc_reg_for_each(midpoints):
    """
    Calculates regression for each parameter separately
    Returns list of lists
    Each list contains coefficients and intercept of each regression
    :param midpoints: list of points
    """
    params = []
    df = pd.DataFrame(midpoints)
    for i in range(len(midpoints[0])):
        x = []
        y = []
        if i != len(midpoints[0]) - 1:
            x1 = df.iloc[:, :i]
            x2 = df.iloc[:, i + 1:]
            x = pd.concat([x1, x2], axis=1)
            y = df.iloc[:, i]  # takes values to fit to
        else:
            x = df.iloc[:, :-1]
            y = df.iloc[:, -1]
        lin_reg = LinearRegression()
        lin_reg.fit(x, y)
        tab = lin_reg.coef_.tolist()
        tab.append(lin_reg.intercept_)
        params.append(tab)
    return params


def predict_each(point, params):
    """
    Calculates prediction based on linear regressions given as a list
    Last field of every list should contain intercept
    Returns a list of predictions - one for every linear regression
    :param point: point, which will be used in predicting values
    :param params: list of linear regressions
    """
    predicted = []
    for i in range(len(params)):
        index = 0
        x = 0
        for j in range(len(point)):
            if j == i:
                continue
            x += point[j] * params[i][index]
            index += 1
        x += params[i][-1]
        predicted.append(x)
    return predicted


# for testing
if __name__ == '__main__':
    m = [[3, 6, 15], [-3, 3, 3], [1, 1, 3], [-5, 6, 7]]
    wyniki = [24, 3, 5, 8]
    para = calc_reg_for_each(m)
    para_with_scores = calc_regression(m, wyniki)
    deriv = calc_der_for_each(m)
    solucje = find_solutions(deriv)

    print(para_with_scores.coef_, para_with_scores.intercept_)
    print(deriv)
    print(solucje)

# RankWarning: Polyfit may be poorly conditioned  -->  zbyt wysoki stopień funkcji

import pandas as pd
import numpy as np
#import sympy

def calc_regression(midpoints, scores=None): #oblicza regresje dla ostatniego parametru lub dla wyników, jeśli podane
    if scores != None:
        for i in range( len(midpoints) ):
            midpoints[i].append(scores[i])
    df = pd.DataFrame(midpoints)
    X = df.iloc[:, :-1]  # wyciaga wartosci, na podstawie ktorych jest estymacja
    Y = df.iloc[:, -1]  # wyciaga wartosci, do ktorych chce sie dopacowac
    lin_reg = LinearRegression()
    lin_reg.fit(X, Y)
    return lin_reg #zwraca klase LinearRegression()

    #return (lin_reg.coef_).tolist(), lin_reg.intercept_  #zwraca parametry regresji liniowej oraz bazową warość 


def prep_for_sympy(poly):
    s = ""
    stopien = len(poly) - 1
    for p in poly:
        s += str(p)
        if stopien>1:
            s += "*x**" + str(stopien) + " + "
        elif stopien==1:
            s += "*x + "
        stopien -= 1
    return s

def solve_polynomial(poly):  #znajduje miejsca zerowe wielomianu
    x = sympy.symbols('x')
    return sympy.solve(prep_for_sympy(poly), x)

def calc_der_for_each(midpoints, scores): #liczy pochodna dla kazdego parametru osobno
    df = pd.DataFrame(midpoints)
    sz = df.shape[1]-1
    ders = []
    for i in range(df.shape[1]):
        f = numpy.polyfit(df[i].tolist(), df[sz].tolist(), 3) #funkcja 3-ego stopnia
        f.reverse()
        for j in range(len(f)-1):
            f[j] = f[j+1]*(j+1)
        f.reverse()
        der.append(f)
    return der

###Funkcje poniżej robia predykcje współrzędnej punktu - być może zaszłaby taka potrzeba, gdyby jakichś danych brakowało

def calc_reg_for_each(midpoints): #robi regresje dla kazdego parametru oddzielnie
    params = []
    df = pd.DataFrame(midpoints)
    for i in range( len(midpoints[0]) ):
        X = Y = []
        if i != len(midpoints[0])-1:
            X1 = df.iloc[:, :i] 
            X2 = df.iloc[:, i+1:]
            X = pd.concat( [X1, X2],  axis=1)
            Y = df.iloc[:, i]  # wyciaga wartosci, do ktorych chce sie dopacowac
        else:
            X = df.iloc[:, :-1]
            Y = df.iloc[:, -1]
        lin_reg = LinearRegression()
        lin_reg.fit(X, Y)
        tab = (lin_reg.coef_).tolist()
        tab.append( lin_reg.intercept_ )
        params.append(tab)
    return params

def predict_each(point, params): #oblicza predykcje kazdego parametru oddzielnie i zwraca wektor predykcji
    predicted = []
    for i in range(len(params)):
        index = 0
        x = 0
        for j in range( len(point) ):
            if j==i:
                continue
            x += point[j] * params[i][index]
            index += 1
        x += params[i][-1]
        predicted.append(x)
    return predicted

m = [[3, 6, 15], [-3, 3, 3], [1, 1, 3], [-5, 6, 7]]
para = calc_reg_for_each(m)
print(para)
print(predict_each([4, 6, 16], para))

import pandas as pd
import numpy as np

def calc_regression(midpoints): #oblicza regresje dla ostatniego parametru
    df = pd.DataFrame(midpoints)
    X = df.iloc[:, :-1]  # wyciaga wartosci, na podstawie ktorych jest estymacja
    Y = df.iloc[:, -1]  # wyciaga wartosci, do ktorych chce sie dopacowac
    lin_reg = LinearRegression()
    lin_reg.fit(X, Y)
    #Y_pred = lin_reg.predict(X)
    #lin_reg.coef_

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

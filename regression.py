import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import sklearn as sk
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import ElasticNet
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn import svm
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

from databasefunctions import new_batting
from databasefunctions import new_teams
from databasefunctions import new_pitching
from databasefunctions import single_data
from databasefunctions import multi_year

#Let's get some test data using the database functions

training = pd.DataFrame(columns = ['teamID', 'W', 'R', 'H', 'HR', '2B', '3B', 'BB', 'SB', 'SO', 'ER', 'HA', 'HRA', 'BBA', 'SOA'])

for i in range(2008,2019):
    training = pd.concat([training, multi_year(i)])

testing = multi_year(i)

print(training.shape[0])
print(testing.shape[0])

#Declaring and normalizing the Data

X_train = training[['R', 'H', 'HR', '2B', '3B', 'BB', 'SB', 'SO', 'ER', 'HA', 'HRA', 'BBA', 'SOA']]
y_train = training['W']

X_test = testing[['R', 'H', 'HR', '2B', '3B', 'BB', 'SB', 'SO', 'ER', 'HA', 'HRA', 'BBA', 'SOA']]
y_test = testing["W"]

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
#y_train = scaler.fit_transform(y_train)

X_test = scaler.fit_transform(X_test)
#y_test = scaler.fit_transform(y_test)

#Sci-Kit Learn - Regular Linear Regression

regr = sk.linear_model.LinearRegression()
regr.fit(X_train, y_train)
predictions_linear = regr.predict(X_test)
print("Basic Linear Regression:")
print('Mean squared error: %.5f'
      % mean_squared_error(y_test, predictions_linear))
print('Coefficient of determination: %.5f'
      % r2_score(y_test, predictions_linear))

#Sci-Kit Learn - Ridge Regression with Penalty 0.01

reg_ridge = sk.linear_model.Ridge(alpha=0.01)
reg_ridge.fit(X_train, y_train)
predictions_ridge = reg_ridge.predict(X_test)
print("Ridge Regression:")
print('Mean squared error: %.5f'
      % mean_squared_error(y_test, predictions_ridge))
print('Coefficient of determination: %.5f'
      % r2_score(y_test, predictions_ridge))

#Sci-Kit Learn - Lasso Regression

reg_lasso = sk.linear_model.Lasso(alpha=0.01)
reg_lasso.fit(X_train, y_train)
predictions_lasso = reg_lasso.predict(X_test)
print("Lasso Regression:")
print('Mean squared error: %.5f'
      % mean_squared_error(y_test, predictions_lasso))
print('Coefficient of determination: %.5f'
      % r2_score(y_test, predictions_lasso))

#Sci-Kit Learn - ElasticNet Regression

reg_elastic = sk.linear_model.ElasticNet(alpha=0.01)
reg_elastic.fit(X_train, y_train)
predictions_elastic = reg_elastic.predict(X_test)
print("ElasticNet Regression:")
print('Mean squared error: %.5f'
      % mean_squared_error(y_test, predictions_elastic))
print('Coefficient of determination: %.5f'
      % r2_score(y_test, predictions_elastic))

#Sci-Kit Learn - Support Vector Regression with Kernel

reg_svr = svm.SVR()
reg_svr.fit(X_train, y_train)
predictions_svr = reg_svr.predict(X_test)
print("SVR")

print('Mean squared error: %.5f'
      % mean_squared_error(y_test, predictions_svr))
print('Coefficient of determination: %.5f'
      % r2_score(y_test, predictions_svr))



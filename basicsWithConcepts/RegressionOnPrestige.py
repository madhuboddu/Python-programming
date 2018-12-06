#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 20:40:00 2018

@author: madhusudhanreddy
"""

from sklearn.linear_model import Lasso
import pandas as pd 
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np


data  = pd.read_csv("Prestige.csv")


data = data.iloc[:, [0,2,3,1]]


x_train , x_test , y_train , y_test  = train_test_split( data.iloc[:, :-1], data.iloc[ :,-1], test_size = 0.15,random_state = 123)


#Applying Standard Scaler before applying laso Regression.

standard = StandardScaler()
x_train = standard.fit_transform(x_train)

x_test = standard.transform(x_test)



#apply linear regression
reg_model = LinearRegression(n_jobs=-1)


reg_model.fit(x_train,y_train)


predict_test = reg_model.predict(x_test)
predict_train = reg_model.predict(x_train)



reg_model.score(x_train,y_train)
reg_model.score(x_test,y_test)



np.sqrt(mean_squared_error(y_train,predict_train))
np.sqrt(mean_squared_error(y_test,predict_test))
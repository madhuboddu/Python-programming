#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 19:37:29 2018

@author: madhusudhanreddy
"""

from sklearn.linear_model import Ridge
import pandas as pd 
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np


data  = pd.read_csv("Prestige.csv")


data = data.iloc[:, [0,2,3,1]]


x_train , x_test , y_train , y_test  = train_test_split( data.iloc[:, :-1], data.iloc[ :,-1], test_size = 0.15,random_state = 123)



#Applying Standard Scaler before applying laso Regression.

standard = StandardScaler()
x_train = standard.fit_transform(x_train)

x_test = standard.transform(x_test)

#apply Ridge

ls = Ridge(alpha= 20)
ls.fit(x_train,y_train)

# predicting values for both test and training set.
predicted_values = ls.predict(x_test)
predicted_values_train  =ls.predict(x_train)

#for R2 values
ls.score(x_train, y_train)
ls.score(x_test,y_test)

#for RSME values
np.sqrt(mean_squared_error(y_train,predicted_values_train))
np.sqrt(mean_squared_error(y_test,predicted_values))





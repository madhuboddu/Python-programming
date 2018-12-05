#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 19:52:34 2018

@author: madhusudhanreddy
"""

import numpy as np 
import pandas as pd
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

 
data  = pd.read_csv('Balloon.csv')

X = data.iloc[:, :-1].values
Y = data.iloc[:, -1].values

data1 =pd.get_dummies(data,drop_first=True)

X = data1.iloc[:, :-1].values
Y = data1.iloc[:, -1].values


x_train,x_test,y_train,y_test = train_test_split(X,y,test_size=0.15)

reg_model = DecisionTreeClassifier( criterion = 'gini'  )

reg_model.fit(x_train,y_train)


y_pred = reg_model.predict(x_test)



from sklearn.metrics import accuracy_score

accuracy_score(y_test,y_pred)

#########################################################################   

from sklearn.ensemble import BaggingClassifier

bag =  BaggingClassifier(reg_model , n_estimators= 50 , oob_score= True ).fit(x_train,y_train)

bag_pred = bag.predict(x_test)

accuracy_score(y_test,bag_pred)




#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 21:06:08 2018

@author: madhusudhanreddy
"""

import numpy as np 
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
 
data  = pd.read_csv('Indian Liver Patient Dataset (ILPD).csv', header = None)


data1 =pd.get_dummies(data,drop_first=True)


X = data1.iloc[:, [0,10,1,2,3,4,5,6,7,8,9]]

X = X.iloc[:, :-1]
y = data1.iloc[:, -2]




x_train,x_test,y_train,y_test = train_test_split(X,y,test_size=0.15)



ran_cls = RandomForestClassifier(n_estimators= 200, oob_score= True).fit(x_train.fillna(0),y_train)


#cls_model = BaggingClassifier(DecisionTreeClassifier(criterion = 'gini'), n_estimators= 50,oob_score=True).fit(x_train.fillna(0), y_train)



from sklearn.metrics import accuracy_score

y_pred = ran_cls.predict(x_test)

accuracy_score(y_test,y_pred)

from sklearn.metrics import confusion_matrix

c_matrix = confusion_matrix(y_test,y_pred)

c_matrix




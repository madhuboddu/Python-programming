#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 20:31:44 2018

@author: madhusudhanreddy
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

indianLiver = pd.read_csv("Indian Liver Patient Dataset (ILPD).csv",header=None)

indianLiver


indianLiverFactoredData = pd.get_dummies(indianLiver, drop_first = True)


x_train , x_test , y_train , y_test = train_test_split(indianLiver.iloc[: ,: -2] , indianLiverFactoredData.iloc[:,-2], test_size = 0.15 , random_state = 123)

clf_entroy = DecisionTreeClassifier(criterion ="entropy",random_state =123,min_samples_leaf = 1,max_depth = 1 )




clf_entroy.fit(x_train,y_train)

clf_entroy.predict(x_test)
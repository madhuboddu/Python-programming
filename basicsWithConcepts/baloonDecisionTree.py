import numpy as np
import pandas as pd
import os
from sklearn.preprocessing import LabelEncoder, OneHotEncoder



dataset=pd.read_csv("Balloon.csv")
dataset
# Encoding categorical data

labelencoder = LabelEncoder()
dataset.iloc[:, 0] = labelencoder.fit_transform(dataset.iloc[:, 0])
onehotencoder = OneHotEncoder(categorical_features = dataset[:,0])
dataset.iloc[:,0] = onehotencoder.fit_transform(dataset.iloc[:,0]).toarray()


from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder = LabelEncoder()

dataset.iloc[:, 1] = labelencoder.fit_transform(dataset.iloc[:, 1])
onehotencoder = OneHotEncoder(categorical_features = dataset[:,1])
dataset.iloc[:,1] = onehotencoder.fit_transform(dataset.iloc[:,1]).toarray()



labelencoder = LabelEncoder()
dataset.iloc[:, 2] = labelencoder.fit_transform(dataset.iloc[:, 2])
onehotencoder = OneHotEncoder(categorical_features = dataset[:,2])
dataset.iloc[:,2] = onehotencoder.fit_transform(dataset.iloc[:,2]).toarray()


labelencoder = LabelEncoder()
dataset.iloc[:, 3] = labelencoder.fit_transform(dataset.iloc[:, 3])
onehotencoder = OneHotEncoder(categorical_features = dataset[:,3])
dataset.iloc[:,3] = onehotencoder.fit_transform(dataset.iloc[:,3]).toarray()

labelencoder = LabelEncoder()
dataset.iloc[:, 4] = labelencoder.fit_transform(dataset.iloc[:, 4])
onehotencoder = OneHotEncoder(categorical_features = dataset[:,4])
dataset.iloc[:,4] = onehotencoder.fit_transform(dataset.iloc[:,4]).toarray()

import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn  import metrics
from sklearn.metrics import r2_score

import matplotlib as mp
import matplotlib.pyplot as plt


data = pd.read_csv("dataset.csv")  # to read a file to python.

x = data.iloc[:, :-1]
y = data.iloc[:, -1]


x_train , x_test ,y_train , y_test = train_test_split(x,y,test_size = 0.15)




reg_model = LinearRegression(n_jobs=1)


reg_model.fit(x_train,y_train)


y_predict = reg_model.predict(x_test)



np.sqrt(r2_score(y_test,y_predict))



plt.plot(x_test,linestyle ='solid',color ='red')


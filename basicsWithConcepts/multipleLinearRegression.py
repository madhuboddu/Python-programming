import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
from sklearn.metrics import mean_squared_error



data = pd.read_csv("data.csv")


x_train , x_test , y_train , y_test  = train_test_split( data.iloc[:, :-1], data.iloc[ :,-1], test_size = 0.15,random_state = 234)


data = data.iloc[ :,[0,2,3,1]]  # to rearrange the coloumns

#Different types of models or methods to select different features

#exuastive search
#forward search    -  #check p value and adjusted R and consider back
#backward search 

#here we are checking with LOG and without LOG
# so we have to check the RMSE for both the models and select the best.

reg_model =  sm.OLS(np.log(y_train), x_train).fit()

reg_model =  sm.OLS(y_train, x_train).fit()



print(reg_model.summary())


y_predict  = reg_model.predict(x_test)



np.sqrt(mean_squared_error(y_test,np.exp(y_predict)))

np.sqrt(mean_squared_error(y_test,y_predict)) 
  
#since the rmse value with out LOG is quite low we consider the model without log. 

#sorting the data frame according to the income.


data.sort_values(by = "income",inplace = True)

data
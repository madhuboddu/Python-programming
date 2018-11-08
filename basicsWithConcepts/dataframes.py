import pandas as pd
import numpy as np


from sklearn import datasets

import pandas as pd

irish = datasets.load_iris()


irish



irish1 = pd.DataFrame(irish['data'],columns = irish['feature_names'])

irish1['Target'] = irish['target']

irish1[irish1['Target'] == 0 ]


irish.describe()

irish.info()


irish1['Target'] = irish1['Target'].astype('category')   #converting the normal data into categorical data.


irish1['Target'].unique()   #list of all the unique elements.
 
irish1['Target'].nunique()  #how many unique values.


irish1['Target'].value_counts() #Returns the num of records per category

irish1.apply()


  irish1['cats'] = irish1['Target'].apply(lambda x : 'category1' if x<=1 else 'category2')


del[irish1['cats']]   #delete colmns in the data frame.

irish1.drop('cats',axis=1,inplace= True)   # delete colmns in the data frame, to delete rows axis =0



irish1[151] = irish1[10,10,10,10,1]


irish1.loc[150] = [10,10,10,10,1]

irish1.loc[150]

irish1.loc[151] = [10,np.NaN,10,np.NaN,1 ]

pd.isnull(irish1)









 
 
 






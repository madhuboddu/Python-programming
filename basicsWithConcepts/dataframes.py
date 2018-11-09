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




irish1 = pd.DataFrame(irish['data'],columns = irish['feature_names'])

irish1['Target'] = irish['target']

irish3 = pd.DataFrame(irish1['Target'])

irish3['New_Target'] = irish3['Target'].apply(lambda x: 'category1' if x<=1 else 'category2' )

pd.merge(irish1, irish3, how = "inner", on = "Target")


pd.join(irish1,irish3,h)


del irish3['Target']

irish3['New_Target1'] = irish3['Target'].apply(lambda x: '1' if x<=1 else '2' )

irish3['seq'] = irish3['New_Target']


import matplotlib.pyplot as plt


rand1 = np.random.randint(1,100,10)
rand2 = np.random.randint(1,100,10)

rand1


plt.plot(np.sort(rand1),np.sort(rand2))  #for line plot


plt.scatter(np.sort(rand1),np.sort(rand2))  #for a scatter plot
plt.xlabel('X-axis')
plt.xlabel('Y-axis')
plt.title('TEST GRAP')

plt.bar(np.sort(rand1),np.sort(rand2))


pd.read_csv("irish.csv")  # to import a file into python.


pd.to_csv('irish.csv')


irish3.to_csv("irish3.csv") # to export a file into system.















 
 
 






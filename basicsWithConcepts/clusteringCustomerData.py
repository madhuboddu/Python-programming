#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 11:11:35 2019

@author: madhusudhanreddy
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

customer_data  = pd.read_csv('Mall_Customers.csv')
start = time.time()
customer_data.head()

customer_data.info()


sum(customer_data['CustomerID'].isna())

sum(customer_data['Genre'].isna())

sum(customer_data['Age'].isna())
sum(customer_data['Annual Income (k$)'].isna())
sum(customer_data['Spending Score (1-100)'].isna())



#before converting the catagorical to numeric values, we should fill up all the null values.


customer_data['Genre'].describe()


customer_data['Spending Score (1-100)'].head()

#best way to find null values is to find indexes of the null values accross the axis 1
customer_data[customer_data.isnull().any(axis = 1)]



cleanup = { 'Genre' :  {'Male' : 1 , 'Female' : 2} }

customer_data.replace(cleanup , inplace = True)

customer_data['Genre'].head()


X = customer_data.iloc[:,[3,4]].values

from sklearn.cluster import KMeans
wcss = []
for i in range(1,11):
    kmeans = KMeans(n_clusters=i , init='k-means++', n_init=10, max_iter=300, random_state=0) 
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
plt.plot(range(1,11), wcss)
plt.xlabel('no of clusters')
plt.ylabel('WCSS')
plt.title('no of clusters vs WCSS')
plt.show()


kmeans = KMeans(n_clusters=5 , init='k-means++', n_init=10, max_iter=300, random_state=0)
predclusters = kmeans.fit_predict(X)


#for visulization of clusters.

plt.scatter(X[predclusters == 0, 0], X[predclusters == 0 , 1] , s = 75,c = 'red', label = 'high value' )
plt.scatter(X[predclusters == 1, 0], X[predclusters == 1 , 1] , s = 75,c = 'blue', label = 'avg spenders' )
plt.scatter(X[predclusters == 2, 0], X[predclusters == 2 , 1] , s = 75,c = 'green', label = 'less spenders' )
plt.scatter(X[predclusters == 3, 0], X[predclusters == 3 , 1] , s = 75,c = 'cyan', label = 'care less' )
plt.scatter(X[predclusters == 4, 0], X[predclusters == 4 , 1] , s = 75,c = 'magenta', label = 'very carfull' )
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1] , s = 100 , c = 'black', label = 'centroids')
plt.xlabel('income of customers')
plt.ylabel('spending points')
plt.title('customer spening clusters')
plt.legend()
plt.show()

print('Execution time - ',time.time()-start)











        



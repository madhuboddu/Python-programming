#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 12:38:03 2019

@author: madhusudhanreddy
"""

#hierarchical clusering.


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


mall_data = pd.read_csv('Mall_Customers.csv')

X = mall_data.iloc[:,[3,4]].values


#creating a dendogram to find the optimal no of clusters
import scipy.cluster.hierarchy as sch

dendogram = sch.dendrogram(sch.linkage(X, method = 'ward'))

plt.title('dendogram')
plt.xlabel('no of clusters')
plt.ylabel('euclidian distane')


#fitting the hirerchical clustering to mall data set.

from sklearn.cluster import AgglomerativeClustering

clustermodel = AgglomerativeClustering(n_clusters=5, affinity = 'euclidean' , linkage = 'ward' )

predclust = clustermodel.fit_predict(X)


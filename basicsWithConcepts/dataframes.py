import pandas as pd
import numpy as np


from sklearn import datasets

import pandas as pd

irish = datasets.load_iris()

irish


irish1 = pd.DataFrame(irish['data'],columns = irish['feature_names'])

irish1['Target'] = irish['target']

irish1[irish1['Target'] == 0 ]

 irish1[(irish1['petal length (cm)'] > 6) & (irish1['sepal length (cm)'] > 7)]






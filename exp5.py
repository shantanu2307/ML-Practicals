import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split,cross_val_score

from sklearn.metrics import mean_squared_error

houses=pd.read_csv('house_data.csv')
houses.head()
corr = houses.corr()
sns.heatmap(corr)
feature_cols = 'sqft_living' 
x = houses[feature_cols]
y = houses.price
x_train, x_test, y_train, y_test = train_test_split( x, y,test_size=0.2) 
linreg = LinearRegression()
print(x_train,y_train)
linreg.fit([x_train],[y_train])
print(linreg.intercept_)
print(linreg.coef_)

linreg.predict(1000)
mse = mean_squared_error(y_test, linreg.predict(x_test))
np.sqrt(mse)
linreg.score(x_test,y_test)
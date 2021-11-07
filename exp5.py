import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt
train=pd.read_csv("./california_housing_test.csv")
pd.set_option('display.max_columns', None)
bed=train.loc[:,'total_bedrooms']
x=np.linspace(0,10,100)
y=2+3*x + np.random.normal(-3, 3, 100)
model = LinearRegression()
x = x[:, np.newaxis]
y = y[:, np.newaxis]
model.fit(x, y)
y_pred = model.predict(x)
plt.scatter(x, y, s=10)
plt.plot(x, y_pred, color='r')
print(y_pred)
plt.show()

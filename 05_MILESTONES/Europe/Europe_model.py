import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge

from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import make_pipeline
df = pd.read_csv('EU28_dataconcat.csv', index_col=0)

# Create train and validation sets
nbr_train = 16
y = df['co2'].to_numpy()
y_train = y[:nbr_train]
y_val = y[nbr_train:]

X = df[['pop', 'gdpc', 'nrg_int', 'co2_int']].to_numpy()
X_train = X[:nbr_train, :]
X_val = X[nbr_train:, :]

# prepare model
model = make_pipeline(StandardScaler(), PolynomialFeatures(2), LinearRegression())

fitted = model.fit(X_train, y_train)
pred_val = fitted.predict(X_val)
pred_val = np.insert(pred_val, 0, y_train[-1])

# plot results
fig, ax = plt.subplots(figsize=(20, 10))
ax.plot(df.index, y)
ax.plot(np.arange((2019-len(pred_val)), 2019), pred_val)
plt.xticks(np.arange(1990, 2019))

plt.show()

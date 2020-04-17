import pandas as pd
import numpy as np
import pickle

import matplotlib
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.kernel_ridge import KernelRidge

from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge

from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import make_pipeline

df = pd.read_csv('EU28_dataconcat.csv', index_col=0)

# df.plot(kind='scatter', x='pop', y='co2')
# #plt.show()
# df.plot(kind='scatter', x='gdpc', y='co2')
# #plt.show()
# df.plot(kind='scatter', x='nrg_int', y='co2')
# #plt.show()
# df.plot(kind='scatter', x='co2_int', y='co2')
# #plt.show()

# Create train and validation sets
# X = df[['pop', 'gdpc', 'nrg_int', 'co2_int']].to_numpy()
X = df[['pop', 'gdpc', 'nrg_int', 'est_ci']].to_numpy()
y = df['co2'].to_numpy()

nbr_train = 28
y_train = y[:nbr_train]
y_val = y[nbr_train:]

X_train = X[:nbr_train, :]
X_val = X[nbr_train:, :]

# prepare model
model = make_pipeline(StandardScaler(), GridSearchCV(KernelRidge(kernel='rbf', gamma=0.1), cv=5, iid=True,
                                                     param_grid={"alpha": [1e0, 0.1, 1e-2, 1e-3],
                                                                 "gamma": np.logspace(-2, 2, 5)}))

fitted = model.fit(X_train, y_train)
filename = 'stdKR_model.sav'
pickle.dump(model, open(filename, 'wb'))

pred_X = fitted.predict(X)
pred_val = fitted.predict(X_val)

rmse = mean_squared_error(y_val, pred_val, squared=False)
print('RMSE: {}'.format(rmse))
pred_val = np.insert(pred_val, 0, y_train[-1])/10**6

# plot results
size = 15
params = {'legend.fontsize': size*1.5,
          'axes.labelsize': size*1.5,
          'xtick.labelsize': size*0.75,
          'ytick.labelsize': size*0.75}
matplotlib.rcParams.update(params)

fig, ax = plt.subplots(figsize=(20, 10))
ax.plot(df.index, y/10**6, label='Target emissions')
ax.plot(np.arange((2019 - len(pred_val)), 2019), pred_val, label='Predicted emissions')

plt.xticks(np.arange(1990, 2019))
plt.xlabel('Years')
plt.ylabel('CO2 emissions [million tonne]')
plt.legend()

plt.savefig('model_emissions.png')
plt.close()

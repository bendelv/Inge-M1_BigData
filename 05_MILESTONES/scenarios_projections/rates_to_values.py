import pandas as pd
import numpy as np

var18 = pd.read_csv('Europe/var18.csv', index_col=['Unnamed: 0']).to_numpy()
print(var18)
from_dir = 'proj_rates/'
to_dir = "proj_values/"

pop = ['pop_SSP1.csv', 'pop_SSP2.csv', 'pop_SSP3.csv', 'pop_SSP4.csv', 'pop_SSP5.csv']
gdp = ['gdp_SSP1.csv', 'gdp_SSP2.csv', 'gdp_SSP3.csv', 'gdp_SSP4.csv', 'gdp_SSP5.csv']
ei = ['EnergyIntensity_SSP1.csv', 'EnergyIntensity_SSP2.csv', 'EnergyIntensity_SSP3.csv', 'EnergyIntensity_SSP4.csv',
      'EnergyIntensity_SSP5.csv']
ci = ['CarbonIntensity_SSP1.csv', 'CarbonIntensity_SSP2.csv', 'CarbonIntensity_SSP3.csv', 'CarbonIntensity_SSP4.csv',
      'CarbonIntensity_SSP5.csv']

vars18 = [pop, gdp, ei, ci]
for var in np.arange(len(vars18)):
    for file in vars18[var]:
        df = pd.read_csv(from_dir+file, index_col=['Unnamed: 0'])
        m = df.to_numpy()

        for i in np.arange(m.shape[0]):
            val = var18[0][var]
            for j in np.arange(m.shape[1]):
                val = val*(m[i][j]/100 + 1)
                m[i][j] = val

        df = pd.DataFrame(m)
        df.to_csv(to_dir+file)


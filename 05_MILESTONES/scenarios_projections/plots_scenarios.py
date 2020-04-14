import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from_dir = "proj_values_EU28/"

pop = ['pop_SSP1.csv', 'pop_SSP2.csv', 'pop_SSP3.csv', 'pop_SSP4.csv', 'pop_SSP5.csv']
gdp = ['gdp_SSP1.csv', 'gdp_SSP2.csv', 'gdp_SSP3.csv', 'gdp_SSP4.csv', 'gdp_SSP5.csv']
ei = ['EnergyIntensity_SSP1.csv', 'EnergyIntensity_SSP2.csv', 'EnergyIntensity_SSP3.csv', 'EnergyIntensity_SSP4.csv',
      'EnergyIntensity_SSP5.csv']
ci = ['CarbonIntensity_SSP1.csv', 'CarbonIntensity_SSP2.csv', 'CarbonIntensity_SSP3.csv', 'CarbonIntensity_SSP4.csv',
      'CarbonIntensity_SSP5.csv']

vrs = [pop]
#, gdp, ei, ci]

for var in vrs:
    fig, ax = plt.subplots(figsize=(20, 10))
    for file in var:
        df = pd.read_csv(from_dir + file, index_col=['Unnamed: 0'])
        m = df.mean()
        std = df.std()
        df = pd.DataFrame({'mean': m, 'std': std})

        dates = np.arange(2019, 2031)
        ax.plot(dates, m, color='green')
        plt.fill_between(dates, m - std, m + std, alpha=0.5)
    plt.show()


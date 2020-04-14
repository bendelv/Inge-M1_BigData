import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


from_dir = "proj_values_EU28/"

# pop = ['pop_SSP1.csv', 'pop_SSP2.csv', 'pop_SSP3.csv', 'pop_SSP4.csv', 'pop_SSP5.csv']
# gdp = ['gdp_SSP1.csv', 'gdp_SSP2.csv', 'gdp_SSP3.csv', 'gdp_SSP4.csv', 'gdp_SSP5.csv']
# ei = ['EnergyIntensity_SSP1.csv', 'EnergyIntensity_SSP2.csv', 'EnergyIntensity_SSP3.csv', 'EnergyIntensity_SSP4.csv',
#       'EnergyIntensity_SSP5.csv']
# ci = ['CarbonIntensity_SSP1.csv', 'CarbonIntensity_SSP2.csv', 'CarbonIntensity_SSP3.csv', 'CarbonIntensity_SSP4.csv',
#       'CarbonIntensity_SSP5.csv']
#
# vrs = [pop, gdp, ei, ci]
#
# for var in vrs:
#     for file in var:
#         df = pd.read_csv(from_dir + file, index_col=['Unnamed: 0'])
#         m = df.mean()
#         std = df.std()
#         df = pd.DataFrame({'mean': m, 'std': std})
#
#         fig, ax = plt.subplots(figsize=(20, 10))
#         dates = np.arange(2019, 2032)
#         ax.plot(dates, m, color='green')
#         plt.fill_between(dates, m - std, m + std, color='lightblue')
#         # plt.show()

ssp1 = ['pop_SSP1.csv', 'gdp_SSP1.csv', 'EnergyIntensity_SSP1.csv', 'CarbonIntensity_SSP1.csv']
ssp2 = ['pop_SSP2.csv', 'gdp_SSP2.csv', 'EnergyIntensity_SSP2.csv', 'CarbonIntensity_SSP2.csv']
ssp3 = ['pop_SSP3.csv', 'gdp_SSP3.csv', 'EnergyIntensity_SSP3.csv', 'CarbonIntensity_SSP3.csv']
ssp4 = ['pop_SSP4.csv', 'gdp_SSP4.csv', 'EnergyIntensity_SSP4.csv', 'CarbonIntensity_SSP4.csv']
ssp5 = ['pop_SSP5.csv', 'gdp_SSP5.csv', 'EnergyIntensity_SSP5.csv', 'CarbonIntensity_SSP5.csv']


def stat_scenario(scenario):
    df_mean = pd.DataFrame({})
    df_std = pd.DataFrame({})
    for file in scenario:
        df = pd.read_csv(from_dir + file, index_col=['Unnamed: 0'])

        m = df.mean()
        col_name = file.split('_')[0]
        df_mean[col_name] = m

        std = df.std()
        col_name = file.split('_')[0]
        df_std[col_name] = std
    df_mean.index = np.arange(2019, 2032)
    df_std.index = np.arange(2019, 2032)

    return df_mean, df_std


# example pour ssp1
mean_ssp1, std_ssp1 = stat_scenario(ssp1)
print(mean_ssp1['CarbonIntensity'])
print(std_ssp1['CarbonIntensity'])
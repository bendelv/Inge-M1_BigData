import pandas as pd
import numpy as np

pop = pd.read_csv('pop_eurostat.csv')
pop.set_index('TIME', inplace=True)
pop = pop['Value'].str.replace(",", "").astype(float)
pop = pop.drop([2019])
pop = pop.iloc[10:]
pop18 = pop[2018]
print(pop)

gdp = pd.read_csv('gdp_worldbank.csv')
gdp = gdp.transpose()
gdp = gdp.loc[:, 0]
gdp = gdp.iloc[14:]
gdp.index = gdp.index.map(lambda x: int(x.split(' ')[0]))
gdp = gdp.drop([2019])
print(gdp)

nrg = pd.read_csv('nrg_conso_eurostat.csv')
nrg.set_index('TIME', inplace=True)

# transorm into tonne of oil equivalent
nrg = nrg['Value'].str.replace(",", "").astype(float) * 1000
print(nrg)

co2 = pd.read_csv('fossilCO2_emissions_edgar.csv', skiprows=1)
co2.set_index('date', inplace=True)
co2 = co2.iloc[20:]
co2 = co2['EU28'].str.replace(",", ".").astype(float) * (10 ** 6)
print(co2)

# Calculate GDP per capita [$(2010)/capita]
gdpc = gdp.values / pop.values
gdpc = pd.DataFrame({'gdpc': gdpc}, index=pop.index)
gdpc18 = gdpc.iloc[28].values[0]

# Calculate energy intensity [toe/$(2010)]
nrg_int = nrg.values / gdp.values
nrg_int = pd.DataFrame({'nrg_int': nrg_int}, index=pop.index)
nrg_int18 = nrg_int.iloc[28].values[0]

# Calculate carbon intensity [t CO2/toe]
co2_int = co2.values / nrg.values
co2_int = pd.DataFrame({'co2_int': co2_int}, index=pop.index)
co2_int18 = co2_int.iloc[28].values[0]

pop = pd.DataFrame({'pop': pop}, index=pop.index)
co2 = pd.DataFrame({'co2': co2}, index=pop.index)

var18 = [pop18, gdpc18, nrg_int18, co2_int18]
var18 = pd.DataFrame({'pop': [var18[0]], 'gdpc': [var18[1]], 'nrgint': [var18[2]], 'co2int': [var18[3]]}, index=[2018])
var18.to_csv('var18.csv')

df = [pop, gdpc, nrg_int, co2_int, co2]
df = pd.concat(df, axis=1, sort=False, join='inner')
print(df)

df.to_csv('EU28_dataconcat.csv')

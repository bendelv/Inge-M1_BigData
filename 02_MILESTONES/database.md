# BIG DATA PROJECT
## Part 1 : Perfrom an exploratory data analysis

#### Why ? 
- Most of the analysis have been done for Europe, now let's do it for Belgium only.
- Better knowledge on our variables
- Variable selection

### Plots 
***Histogram*** : Normaly shapped (and take the difference of adjacent point, p.77)
***Scatter plots*** : It can be useful to see how two or more time series are linked over time (p.79-80)

## Part 1 : Bench mark
- As ***benchmark***, we should predicts (linear regression, SVR regression, MA, etc) other fossil energy consumption (independant variables) and the corresponding CO2 emissions.
- ***Energy sources : [https://www.iea.org/subscribe-to-data-services/co2-emissions-statistics](https://www.iea.org/subscribe-to-data-services/co2-emissions-statistics) data + documentations  _ 1971-2017***
	- coal
	- oil (diesel + gasoline)
	- natural gas
	- other
- ***Sectors : [Edgar dataset] _ 1970 - 2018***
	- Power industry
	Includes power and heat generation plants (public and autoproducers).
*Public :* Main activity producers (formerly known as public utilities) are defined as those undertakings whose primary activity is to supply the public.
	*Autoproducer :* Autoproducer undertakings generate electricity and/or heat, wholly or partly for their own use as an activity which supports their primary activity.
		- Thermal power plants.
			- Nuclear power plants.
			- Coal power plants.
		- Hydroelectric power plants.
		- Solar power plants.
		- Wind power plants.
	- Other combustion industry
	Includes combustion for :
		- Industrial manufacturing
		- Fuel production
	- Buildings 
		- CO2 emissions from residential buildings and commercial and public services contains all emissions from fuel combustion in households.
	- Transport 
		-	CO2 emissions from transport contains emissions from the combustion of fuel for all transport activity, regardless of the sector, except for international marine bunkers and international aviation. This includes domestic aviation, domestic navigation, road, rail and pipeline transport.
	- Other 
		- Includes industrial process emissions (non-metallic minerals, non-ferrous metals, solvents and other product
use, chemicals), indirect emissions (for N2O only), agriculture (including agricultural soils, agricultural waste
burning, enteric fermentation, manure management) and waste.

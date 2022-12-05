# Project Charter
## Business background

### The Client
The client of this project is a fictional company that is researching about the effects of the Green House Gas (GHG) emissions and the effect on the global average temperature warming. The company focuses on doing scientific research to link the increase on temperature with the anthropogenic GHG emissions.

### The problem
The company want to understand the relation between GHG emissions and the increase on temperature on the globe and well create a forecast model to predict the global temperature increase based on historical GHG emissions and temperature data. 

## Scope
This project will develop a machine learning project to predict the future global temperature increase based on historical GHG emissions and temperature data. In total two historical data set will be analyzed. The client will be able to use this model to predict the global temperature increase in the next 10 years using a simplified user interface on we web application. The user will be able to play with different scenarios: below 1.5C, 2C and above 2C. 

## Personnel
* Who are on this project:
	* Unal team:
		* Project lead: Martin Jaramillo
		* PM: Martin Jaramillo
		* Data scientist(s): : Martin Jaramillo
		* Account manager: : Martin Jaramillo
	* Client:
		* Data administrator: Fictional Client_A 
		* Business contact: Fictional Client_B
	
## Metrics
* Qualitative objectives:Capacity to forecast different global temperature increase based on historical data. Create a cluster of the most vulnerables countries.
* Quantitative metrics: Time spend to update a real time temperature increase forecast. Accuracy of the forecast prediction. 

## Working plan

The project will be developed in the following phases: 

Phase 0: Business understanding
Phase 1: Data acquisition and understanding 
Phrase 2: Development
Phase 3: Modeling
Phase 4: Deployment

## Architecture
* Data
  * Two data sets will be explored:
    ** Dataset_Temratures:https://www.kaggle.com/datasets/berkeleyearth/climate-change-earth-surface-temperature-data
    ** Dataset_Emissions:https://ourworldindata.org/co2-and-other-greenhouse-gas-emissions
* Data movement from the public available sources above to a local MySQL server

## to update from here as the project advance!
  * all the data, 
  * after some pre-aggregation on-prem,
  * Sampled data enough for modeling 

* What tools and data storage/analytics resources will be used in the solution e.g.,
  * ASA for stream aggregation
  * HDI/Hive/R/Python for feature construction, aggregation and sampling
  * AzureML for modeling and web service operationalization
* How will the score or operationalized web service(s) (RRS and/or BES) be consumed in the business workflow of the customer? If applicable, write down pseudo code for the APIs of the web service calls.
  * How will the customer use the model results to make decisions
  * Data movement pipeline in production
  * Make a 1 slide diagram showing the end to end data flow and decision architecture
    * If there is a substantial change in the customer's business workflow, make a before/after diagram showing the data flow.

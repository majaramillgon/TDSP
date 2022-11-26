# Data Dictionary
# Database weather_db
The database for this project will be organized into a SQL schema that will contain two tables. The first table will have the data related to the global temperature by country and the second table will have the data from the GHG emissions by country. All the data will be historical data in the form of a time series. 

The database is still not fully functional and the schema together with the UML diagram will be added latter as the project progress. 

![UML Diagram](/file/uml/database1)

## Table 1: Country_emissions

The first table will be composed from information taken from the following source: https://www.kaggle.com/datasets/berkeleyearth/climate-change-earth-surface-temperature-data

The data contains the following columns: 

| column | type | description |
| --- | --- | --- |
| dt | DATE| This colums has the date in the YYYY-MM-DD format |
| AverageTemperature | INT | Contains the average global temperature for a given year in a given country |
| Country | INT | Contains the country name |

## Table 2: Country_temperature

The first table will be composed from information taken from the following source: https://ourworldindata.org/co2-and-other-greenhouse-gas-emissions

The data contains the following columns: 

| column | type | description |
| --- | --- | --- |
| Entity | STR | Contains the country name |
| Code | INT | Contains the country code |
| Year | INT | This colums has the date in the YYYY format |
| Annual_emissions | INT | Contains the emissions on tonCO₂e |
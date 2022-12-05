# Data and Feature Definitions

This document provides a central hub for the raw data sources of the project. The processed/transformed data, and feature sets. More details of each dataset is provided in the data summary report. 

For each dataset, an individual report describing the data schema, the meaning of each data field, and other information that is helpful for understanding the data is provided. If the dataset is the output of processing/transforming/feature engineering existing data set(s), the names of the input data sets, and the links to scripts that are used to conduct the operation are also provided. 

For each dataset, the links to the sample datasets in the _**Data**_ directory are also provided.

## Raw Data Sources

| Dataset Name | Original Location | Destination Location  | Data Movement Tools / Scripts
| ---:| ---: | ---: | ---: |
| Country_emissions_raw | Source: [Kaggel](https://www.kaggle.com/datasets/berkeleyearth/climate-change-earth-surface-temperature-data) | SQL database | [Get_raw_data.txt](https://github.com/majaramillgon/TDSP/blob/master/docs/data/Raw_data/Get_raw_data.txt)
| Country_temperature_raw| Source: [ourworldindata](https://ourworldindata.org/co2-and-other-greenhouse-gas-emissions) | SQL database | [Get_raw_data.txt](https://github.com/majaramillgon/TDSP/blob/master/docs/data/Raw_data/Get_raw_data.txt) |

* Country_emissions summary. <Provide brief summary of the data, such as how to access the data. More detailed information should be in the Dataset1 Report.>
* DCountry_temperature summary. <Provide brief summary of the data, such as how to access the data. More detailed information should be in the Dataset2 Report.> 

## Processed Data
| Processed Dataset Name | Input Dataset(s)   | Data Processing Tools/Scripts
| ---:| ---: | ---: |
| Country_emissions | [Country_emissions](link/to/dataset2/report) | [data_processing.py](https://github.com/majaramillgon/TDSP/blob/master/scripts/preprocessing/data_processing.py) | [Processed Dataset 1 Report](https://github.com/majaramillgon/TDSP/tree/master/docs/data/SQL_documentation)|
| Country_temperature | [Country_temperature]() |[data_processing.py](https://github.com/majaramillgon/TDSP/blob/master/scripts/preprocessing/data_processing.py)

* Processed Data1 summary. The processed data was aggregated into a single data base in a MySQL database. Please see below the database description.

| Field       | Type         | Null | Key | Default | Extra          |
| ---:      | ---:         | ---: | ---: | ---: | ---:          |
| id          | int(11)      | NO   | PRI | NULL    | auto_increment |
| Year        | int(11)      | YES  |     | NULL    |                |
| Country     | varchar(255) | YES  |     | NULL    |                |
| Emissions   | float        | YES  |     | NULL    |                |
| Temperature | float        | YES  |     | NULL    |                |

## Final data for the anlysis
* Database name: ql7582498
* Table name: climate_db

How to query data using Python: [Link](https://github.com/majaramillgon/TDSP/blob/master/scripts/data_acquisition/Query_data_MySQL.py)

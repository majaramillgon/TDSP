# Data and Feature Definitions

This document provides a central hub for the raw data sources of the project. The processed/transformed data, and feature sets. More details of each dataset is provided in the data summary report. 

For each dataset, an individual report describing the data schema, the meaning of each data field, and other information that is helpful for understanding the data is provided. If the dataset is the output of processing/transforming/feature engineering existing data set(s), the names of the input data sets, and the links to scripts that are used to conduct the operation are also provided. 

For each dataset, the links to the sample datasets in the _**Data**_ directory are also provided.

## Raw Data Sources

| Dataset Name | Original Location | Destination Location  | Data Movement Tools / Scripts | Link to Report |
| ---:| ---: | ---: | ---: | -----: |
| Country_emissions_raw | Source: [Kaggel](https://www.kaggle.com/datasets/berkeleyearth/climate-change-earth-surface-temperature-data) | SQL database | [data_aquisition.py](https://github.com/majaramillgon/TDSP/blob/master/scripts/preprocessing/data_aquisition.py) | [Dataset 1 Report](link/to/report1)|
| Country_temperature_raw| Source: [ourworldindata](https://ourworldindata.org/co2-and-other-greenhouse-gas-emissions) | SQL database | [data_aquisition.py](https://github.com/majaramillgon/TDSP/blob/master/scripts/preprocessing/data_aquisition.py) | [Dataset 2 Report](link/to/report2)|

* Country_emissions summary. <Provide brief summary of the data, such as how to access the data. More detailed information should be in the Dataset1 Report.>
* DCountry_temperature summary. <Provide brief summary of the data, such as how to access the data. More detailed information should be in the Dataset2 Report.> 

## Processed Data
| Processed Dataset Name | Input Dataset(s)   | Data Processing Tools/Scripts | Link to Report |
| ---:| ---: | ---: | ---: | 
| Country_emissions | [Country_emissions](link/to/dataset2/report) | [Python_Script1.py](link/to/python/script/file/in/Code) | [Processed Dataset 1 Report](https://github.com/majaramillgon/TDSP/tree/master/docs/data/SQL_documentation)|
| Country_temperature | [Country_temperature]() |[script2.R](link/to/R/script/file/in/Code) | [Country_temperature Report](https://github.com/majaramillgon/TDSP/tree/master/docs/data/SQL_documentation)|
* Processed Data1 summary. <Provide brief summary of the processed data, such as why you want to process data in this way. More detailed information about the processed data should be in the Processed Data1 Report.>
* Processed Data2 summary. <Provide brief summary of the processed data, such as why you want to process data in this way. More detailed information about the processed data should be in the Processed Data2 Report.> 
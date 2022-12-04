# Data Report

This document contains the results from the exploratory data analysis. Please refer to the following [data_processing.py](https://github.com/majaramillgon/TDSP/blob/master/scripts/preprocessing/data_processing.py) script to see the run the full analysis. 

## General summary of the data
| #  | Column   |    Non-Null | Count | Dtype | 
|--- | ---    |   --- | --- |  --- | 
| 0  | Year     |    12740 | non-null |  int64  |
| 1  | Country   |   12740 | non-null | object |
| 2  | Emissions |   12740 | non-null | float64 |
| 3  | Temperature | 12740 | non-null | float64 |

## Data quality summary
The data was cleaned an there is sufficient data for all the years.
## Target variable
The objetive variable will the Emissions. 

## Individual variables
* Year
* Country
* Temperature
* Emissions
## Variable ranking
* Emissions > Temperature > Year > Country

## Relationship between explanatory variables and target variable

The increase on emissions will be related on the increase of the temperature in time. 

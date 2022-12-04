# Data Dictionary
# Database weather_db
The database for this project will be organized into a SQL schema that will contain one table. The table will have the data related to the global temperature and GHG emissions by country. From the years 1949 to 2013. 

Please see the datbase schema below:

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
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import mysql.connector

#%% 1. Import the data
## 1.1 Temperatue
Dataset_Temratures_raw = pd.read_csv('/home/majaramillogon/Downloads/GlobalLandTemperaturesByCountry.csv')

## 1.2 Emissions
Dataset_Emissions_raw = pd.read_csv('/home/majaramillogon/Downloads/annual-co-emissions-by-region.csv')

#%% 2. Explore the two data sets
# 2.1 Information
Dataset_Temratures_raw.info()
Dataset_Emissions_raw.info()

# 2.2 Select colums that I need
Dataset_Temratures_raw = Dataset_Temratures_raw[['dt','Country', 'AverageTemperature']]
Dataset_Emissions_raw = Dataset_Emissions_raw[['Year', 'Entity','Annual CO₂ emissions (zero filled)']].sort_values(by=['Entity'])

#%% 3. Clean the data
# 3.1 Drop NAs
Dataset_Temratures_raw = Dataset_Temratures_raw.dropna()

# 3.2 Fix the year to the same date data type
Dataset_Temratures_raw['dt'] = Dataset_Temratures_raw['dt'].str.split('-',expand=True,)[0].astype('int64')

# 3.2.1 Create an avergae of the year for temperature to harmonize the datasets
Dataset_Temratures_raw = Dataset_Temratures_raw.groupby(['dt', 'Country']
                                                        ).agg({'AverageTemperature':'mean'}
                                                                ).reset_index().sort_values(by=['Country'])

# 3.3 Harominze the colums
Dataset_Temratures_raw.columns = ['Year', 'Country', 'Temperature']
Dataset_Emissions_raw.columns = ['Year', 'Country', 'Emissions']

# 3.4 Harominze the County variable betwen the two datasets
len(Dataset_Temratures_raw['Country'].unique())
len(Dataset_Emissions_raw['Country'].unique())

count = list(set(Dataset_Temratures_raw['Country']) & set(Dataset_Emissions_raw["Country"]))

# Select the data that only is available in both data sets
Dataset_Temratures_raw = Dataset_Temratures_raw[(Dataset_Temratures_raw['Country'].isin(count))&
                                                (Dataset_Temratures_raw['Year']<= 2013) & 
                                                (Dataset_Temratures_raw['Year']>= 1949) 
                                              ]
Dataset_Emissions_raw = Dataset_Emissions_raw[(Dataset_Emissions_raw['Country'].isin(count)) &
                                              (Dataset_Emissions_raw['Year']<= 2013) & 
                                              (Dataset_Emissions_raw['Year']>= 1949) 
                                              ]

#%% 4. Describe the data
## 4.1 Temperatues
Dataset_Temratures_raw.describe()
Dataset_Temratures_raw.describe(include=['object'])

Dataset_Temratures_raw.head(2)

## 4.1 Emissions
Dataset_Emissions_raw.describe()
Dataset_Emissions_raw.describe(include=['object'])

Dataset_Emissions_raw.head(2)

#%% 5. Data statistics
## 5.1 See how the distributions look
plt.hist(Dataset_Temratures_raw['Temperature'])
#plt.show();

plt.hist(Dataset_Emissions_raw['Emissions'])
#plt.show();

# 5.2 Kurtosis
'''
k > +1, the distribution is too peaked
k < –1 indicates a distribution that is too flat.
-1 < k < 1 Distributions exhibiting skewness and/or kurtosis that exceed these guidelines are considered nonnormal.
'''
Dataset_Temratures_raw.kurt()
Dataset_Emissions_raw.kurt()

# 5.3 Kurtosis
'''
k > 1, the distribution is balanced to the maximun
k < –1 the distribution is balanced to the minimun
'''
Dataset_Temratures_raw.skew()
Dataset_Emissions_raw.skew()

#%% 6. Correlations
Dataset_Emissions_raw['help'] = Dataset_Emissions_raw['Year'].astype(str) + Dataset_Emissions_raw['Country']
Dataset_Temratures_raw['help'] = Dataset_Temratures_raw['Year'].astype(str) + Dataset_Temratures_raw['Country']

corr_df = pd.merge(Dataset_Emissions_raw,
                   Dataset_Temratures_raw, 
                   how = 'left',
                   on = 'help')

corr_df.drop(['Year_y','Country_y','help'], axis = 1, inplace = True)
corr_df.columns = ['Year', 'Country', 'Emissions', 'Temperature']

#%% 7. Save a df in MySQL
df = corr_df

pwr = input()

mydb = mysql.connector.connect(
  host="sql7.freesqldatabase.com",
  user="sql7582498",
  password=pwr,
  database="sql7582498"
)

mycursor = mydb.cursor()

#%% 7. Create a table
mycursor.execute('''CREATE TABLE climate_db 
                    (id INT AUTO_INCREMENT PRIMARY KEY, 
                    Year INT, 
                    Country VARCHAR(255),
                    Emissions FLOAT,
                    Temperature FLOAT
                    )''')

# 7.1 insert the data
add_data = ('''INSERT INTO climate_db 
               (Year, Country, Emissions, Temperature)
               VALUES (%s, %s, %s, %s)
               '''
               )

data = df.to_json(orient="records")
type(data)

import json
data_1 = json.loads(data)

ls = []
for i in range(len(data_1)):
   a = tuple([v for v in data_1[i].values()])
   ls.append(a)

mycursor.executemany(add_data , ls)
   
mydb.commit()

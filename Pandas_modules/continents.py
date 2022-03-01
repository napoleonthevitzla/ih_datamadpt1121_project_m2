# Libraries
import pandas as pd
import numpy as np

# Import CSV from SQL
df_diamonds = pd.read_csv ('/Users/antoniohuerta/ironhack/ih_datamadpt1121_project_m2/db/Diamonds_db_SQL.csv')

# Obtenemos el listado de valores únicos de la columna city
cities = df_diamonds['City'].unique()

# Creamos un diccionario al que asignamos los continentes:

country_cont = {'Dubai':'Asia',
                 'Kimberly':'Africa',
                 'Las Vegas':'America',
                 'Tel Aviv':'Asia',
                 'Amsterdam':'Europe',
                 'Zurich':'Europe',
                 'Antwerp':'Europe',
                 'Madrid':'Europe',
                 'Paris':'Europe',
                 'Surat':'Asia',
                 'Luxembourg':'Europe',
                 'London':'Europe', 
                 'New York City':'America'
                 }

# Insertamos una columna con el continente
df_diamonds['Continent']=df_diamonds['City'].map(country_cont)
# Exportamos el csv
df_diamonds.to_csv(r'/Users/antoniohuerta/ironhack/ih_datamadpt1121_project_m2/db/Diamonds_db_pandas.csv', index = False)

import pandas as pd

#print all columns when printing dataframes
pd.set_option('display.max_columns', None)

df = pd.read_csv('pokemon_data.csv')

##Reading Data
#print(df.head())

#print(df.columns)

#print(df[['Name', 'Type 1', 'HP']])

#print(df.sort_values(['Type 1', 'HP'], ascending=[1,0]))

##Change Data
df['Total'] = df.iloc[:, 4:10].sum(axis=1)

cols = list(df.columns.values)
df = df[cols[0:4] + [cols[-1]] + cols[4:12]]

print(df.head())

df.to_csv('modified.csv')
import os
import glob
import pandas as pd
import matplotlib.pyplot as plt

#%% import all data and put it into one DataFrame
dir_path = os.path.dirname(os.path.realpath(__file__))
folder_path = os.path.join(dir_path, "sales_data")

os.chdir(folder_path)
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

df = pd.DataFrame()

for file in all_filenames:
    temp_df = pd.read_csv(file)
    df = pd.concat([df, temp_df])

#%% cleanup data
df.dropna(inplace=True, how='all')

df = df[df['Order Date'].str[0:2] != 'Or']

df.reset_index()

#%% add month column
df['Month'] = df['Order Date'].str[0:2].astype('int8')

#%% add total price column
df['Total Price'] = df['Price Each'].astype('double') * df['Quantity Ordered'].astype('int32')

#%% which month was the best?
month_sales = df.groupby('Month')['Total Price'].sum()
months = range(1,13)

plt.bar(months, month_sales)
plt.xticks(months)
plt.ylabel('Sales [$]')
plt.xlabel('Month number')
plt.show()

#%% which city sold the most products?
df['City'] = df['Purchase Address'].apply(lambda x: x.split(',')[1].strip())
#print("City, where most products were sold: " + str(df.groupby('City')))
cities = df.groupby('City', as_index=False)['Total Price'].sum()

plt.bar(cities['City'], cities['Total Price'])
plt.figure(figsize=(20, 3))
plt.show()
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
df['City'] = df['Purchase Address'].apply(lambda x: x.split(',')[1].strip() + ' ' + x.split(',')[2].strip().split(' ')[0].strip())
#print("City, where most products were sold: " + str(df.groupby('City')))
cities = df.groupby('City', as_index=False)['Total Price'].sum()

plt.bar(cities['City'], cities['Total Price'])
plt.xticks(cities['City'], rotation='vertical')
plt.ylabel('Sales [$]')
plt.xlabel('City name')
plt.show()

#%% Question #3: What time should we display advertisements to maximize the likelihood of purchases?
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Hour'] = df['Order Date'].dt.hour
df['Minute'] = df['Order Date'].dt.minute

hours = [hour for hour, dtfrm in df.groupby('Hour')]

plt.plot(hours, df.groupby('Hour').count())
plt.xticks(hours)
plt.xlabel('Hour')
plt.ylabel('Number of Orders')
plt.grid()
plt.show()

#%% Question #4: Which products are most often sold together?
df2 = df[df['Order ID'].duplicated(keep=False)]

temp_df = df2.groupby('Order ID')

new_column = temp_df['Product'].transform(lambda x: ','.join(x))
                                        
df2.insert(11, 'Grouped', new_column)

df2 = df2[['Order ID','Grouped']].drop_duplicates()

from itertools import combinations
from collections import Counter

count = Counter()

for row in df2['Grouped']:
    row_list = row.split(',')
    count.update(Counter(combinations(row_list, 2)))
    
for key,value in (count.most_common(10)):
    print(key, value)

#%% Question 5: What product sold the most and why?
df['Quantity Ordered'] = df['Quantity Ordered'].astype('int32') 
df['Price Each'] = df['Price Each'].astype('float') 
product_group = df[['Product','Quantity Ordered']].groupby('Product').sum()

plt.bar(product_group.index, product_group['Quantity Ordered'])
plt.xticks(product_group.index, rotation='vertical')
plt.ylabel('Quantity Ordered')
plt.xlabel('Product')
plt.show()


















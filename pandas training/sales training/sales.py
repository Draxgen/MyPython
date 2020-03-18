import os
import glob
import pandas as pd

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
print("Best month: " + str(df.groupby('Month').sum().idxmax()[0]))

#%% which city sold the most products?
new = df['Purchase Address'].str.split(', ')
#print("City, where most products were sold: " + str(df.groupby('')))
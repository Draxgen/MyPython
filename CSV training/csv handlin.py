import csv
import pathlib
import os

# get paths
curr_dir = pathlib.Path(__file__).parent.absolute()
#path = "C:\Projects\_Prywatne\MyPython\CoggingTorque_200309_073348_CCW.csv"
path = os.path.join(curr_dir, 'CoggingTorque_200309_073348_CCW.csv')

#open the CSV file that has \t as delimiters
file = open(path, newline='')
reader = csv.reader(file, delimiter='\t')

#skip the header
header = next(reader)

#data = [row for row in reader]
data = []
for row in reader:
    deg = float(row[0].replace(',','.'))
    torque = float(row[1].replace(',','.'))
    data.append([deg, torque])

print(data[0])


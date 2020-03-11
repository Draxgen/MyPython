import csv
import pathlib
import os
import matplotlib.pyplot as plt 
import numpy as np
from scipy import signal

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
deg = []
torque = []
for row in reader:
    deg.append(float(row[0].replace(',','.')))
    torque.append(float(row[1].replace(',','.')))

print(deg[0])
print(torque[0])

plt.plot(deg, torque, label='raw')

#lowpass filter
freq_samp = 6000
freq_cutoff = 10
freq_norm = freq_cutoff / (freq_samp / 2)
b, a = signal.butter(5, freq_norm, 'low')
filtered_sig = signal.filtfilt(b, a, torque)

plt.plot(deg, filtered_sig, label='filtered')


plt.xlabel('Degrees [deg]')
plt.ylabel('Torque [mNm]')
plt.title('CoggingTorque')

plt.show()



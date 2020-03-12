import csv
import pathlib
import os
import matplotlib.pyplot as plt 
import numpy as np
from scipy import signal

# get paths
curr_dir = pathlib.Path(__file__).parent.absolute()
#path = "C:\Projects\_Prywatne\MyPython\CoggingTorque_200309_073348_CCW.csv"
path = os.path.join(curr_dir, 'CoggingTorque_200309_073348_RawCW.csv')

#open the CSV file
file = open(path, newline='')
reader = csv.reader(file, delimiter='\t')

#skip the headers
header = []
header.append(next(reader))
header.append(next(reader))

#data = [row for row in reader]
torque = []
temp = next(reader)#[2:]
print(temp[0][2:])
torque.append(temp[0][2:])
for row in reader:
    torque.append(float(row[0].replace(',','.')))


x = [i for i in range(0, len(torque))]

#print(torque[0])

plt.plot(x, torque, label='filtered')

#lowpass filter
freq_samp = 6000
freq_cutoff = 15
freq_norm = freq_cutoff / (freq_samp / 2)
b, a = signal.butter(5, freq_norm, 'low')
filtered_sig = signal.filtfilt(b, a, torque)

plt.plot(filtered_sig, label='filtered')


plt.xlabel('Degrees [deg]')
plt.ylabel('Torque [mNm]')
plt.title('CoggingTorque')

plt.show()



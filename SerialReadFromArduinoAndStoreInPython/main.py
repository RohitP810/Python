import pandas as pd
import serial
import csv
from serial import Serial

seonsor = serial.Serial('COM9', 9600)
# 'COM5' is the port name that the Arduino is connected.
# '9600' is the Baudrate.

data = pd.DataFrame()
w = 100;
safe = True
while safe:
    print('\nPUT ', w, ' GRAMS AND PRESS THE BUTTON\n')
    signal = seonsor.readline()
    print('serial : ', signal, '\nweight : ', w)
    temp = signal.decode('utf-8').split(',')
    temp.insert(0, w)
    if (w <= 38000) and (w > 30000):
        w = w - 4000
    elif (w <= 30000) and (w > 20000):
        w = w - 10000
    elif (w <= 20000) and (w > 10000):
        w = w - 5000
    elif (w <= 10000) and (w > 1000):
        w = w - 1000
    elif (w <= 1000) and (w > 500):
        w = w - 500
    elif w <= 500:
        w = w - 100

    data = data.append(pd.Series(signal), ignore_index=True)

    f = open('sensors.csv', 'a', newline='')
    wr = csv.writer(f)
    wr.writerow(temp)

    f.close()

print('\nMAX WEIGHT LIMIT REACHED')
import matplotlib.pyplot as plt
import csv


x = []
y = []
z = []

with open('data.csv', 'r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        x.append(row[0])
        y.append(row[1])
        z.append(row[2])

plt.plot(x, y, color='g', linestyle='-',marker='o',label='Inc')
plt.plot(x, z, color='r', linestyle='-',marker='o',label='Dec')
plt.legend()
plt.show()
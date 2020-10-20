import matplotlib.pyplot as plt
import numpy as np
import csv

date = []
temp = []

with open('./data/data.csv') as data_file:
    csv_reader = csv.reader(data_file, delimiter=',')
    for row in csv_reader:
        date.append(row[0])
        temp.append(float(row[1]))

print('Done Parsing Data')

plt.xticks(np.arange(0, 100, 1))
plt.scatter(date[:100], temp[:100], c='blue')
plt.show()
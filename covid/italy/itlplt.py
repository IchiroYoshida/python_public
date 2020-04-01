'''
   plot Italy

   2020-03-28
'''
import math
import csv
import matplotlib.pyplot as plt

read_csv = './data/itlplt.csv'

csvRow = []

with open(read_csv) as f:
    reader = csv.reader(f)
    for row in reader:
        csvRow.append([row][0])

del csvRow[:1]

Date = []
Deaths =[]
X = []
Y = []
 
for dat in csvRow:
    date = dat[0]
    deaths = (math.log(int(dat[1])/math.log(10)))*5.
    x = float(dat[2])
    y = float(dat[3])

    Date.append(date)
    Deaths.append(deaths)
    X.append(x)
    Y.append(y)

#plt.scatter(X,Y, s=20, c="pink", linewidths="2", edgecolors="red")

for n in range(len(Date)):
   plt.scatter(X[n],Y[n],s=Deaths[n],c="pink", linewidths="2", edgecolors="red")
   plt.text(X[n],Y[n],Date[n],fontsize=10, color="black")

plt.title("COVID-19 pandemic in Italy [2020/2/21-3/18]")
plt.xlabel("Td(Doubling time [days])")
plt.ylabel("Milion/Deaths")
plt.grid(True)
plt.xscale('log')
plt.yscale('log')
plt.show()
     

import matplotlib.pyplot as plt
from random import random
from math import log

def poissonProcess(lmbda, t):
    time = 0
    arrivals = 0
    while (time < t):
        val = random()
        time += (1/lmbda) * log(1/(1-val))
        arrivals += 1
    return arrivals

def plotOutcomes(numberOfArrivals):
    bins = range(min(numberOfArrivals), max(numberOfArrivals)+2) 
    counts, edges, bars = plt.hist(numberOfArrivals, bins, edgecolor = "midnightblue")
    plt.bar_label(bars, fontsize = 8)
    plt.xticks(bins, fontsize = 6)
    plt.xlabel("Number of patients (arrivals)")
    plt.ylabel("Frequency")
    plt.show()

t = 10

# simulation 1, value of λ = 5
numberOfArrivals1 = []
for process in range(1000):
    numberOfArrivals1.append(poissonProcess(lmbda = 5, t = t))

print(f"mean value of number of arrivals when λ = 5 is {sum(numberOfArrivals1)/len(numberOfArrivals1)}")
plotOutcomes(numberOfArrivals1)

# simulation 2, value of λ = 15
lmbda = 15
numberOfArrivals2 = []
for process in range(1000):
    numberOfArrivals2.append(poissonProcess(lmbda = 15, t = t))

print(f"mean value of number of arrivals when λ = 15 is {sum(numberOfArrivals2)/len(numberOfArrivals2)}")
plotOutcomes(numberOfArrivals2)

# simulating first interarrival time
arrivalTimes = []
for process in range(1000):
    val = random()
    arrivalTimes.append((1/lmbda) * log(1/(1-val)))

xvals = [i+1 for i in range(1000)]
plt.scatter(xvals, arrivalTimes, c = "midnightblue", s = 8)
plt.xlabel("Process number")
plt.ylabel("Inter-arrival time")
plt.show()
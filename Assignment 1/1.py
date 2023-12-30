import matplotlib.pyplot as plt
from random import random

def bernoulliProcess(p):
    heads = 0
    for toss in range(20):
        out = 1 if (random() <= p) else 0
        heads += out
    return heads

def plotOutcomes(numberOfHeads):
    bins = range(min(numberOfHeads), max(numberOfHeads)+2) 
    counts, edges, bars = plt.hist(numberOfHeads, bins, edgecolor = "midnightblue")
    plt.bar_label(bars)
    plt.xticks(bins)
    plt.xlabel("Number of heads (arrivals)")
    plt.ylabel("Number of processes")
    plt.show()

# simulation 1, value of p = 0.8
numberOfHeads1 = []
for process in range(1000):
    numberOfHeads1.append(bernoulliProcess(p = 0.8))
plotOutcomes(numberOfHeads1)

# simulation 2, value of p = 0.5
numberOfHeads2 = []
for process in range(1000):
    numberOfHeads2.append(bernoulliProcess(p = 0.5))
plotOutcomes(numberOfHeads2)
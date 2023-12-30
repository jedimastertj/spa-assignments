import matplotlib.pyplot as plt
import numpy as np
from math import sqrt

def diff2norm(previousDistribution, currentDistribution):
    val = 0
    for i in range(4):
        val += (currentDistribution[i] - previousDistribution[i]) ** 2
    return sqrt(val)

def multiply(currentDistribution, tpm):
    n = len(tpm)
    nextDistribution = []
    for i in range(n):
        val = 0
        for j in range(n):
            val += currentDistribution[j] * tpm[j][i]
        nextDistribution.append(val)
    return nextDistribution

def matrixMultiply(p_i, tpm):
    a = np.array([p_i[0], p_i[1], p_i[2], p_i[3]])
    b = np.array([tpm[0], tpm[1], tpm[2], tpm[3]])
    mul = np.matmul(a, b)
    mul = [mul[i].tolist() for i in range(4)]
    return mul

def getFinalDistribution(initialDistribution, tpm, steps):
    finalDistribution = initialDistribution
    p_i = tpm
    
    for step in range(steps):
        finalDistribution = multiply(finalDistribution, tpm)
        p_i = matrixMultiply(p_i, tpm)
    finalDistribution = [round(val, 3) for val in finalDistribution]
    
    for i in range(4):
        p_i[i] = [round(p_i[i][j], 3) for j in range(4)]
    print(f"Matrix p^{steps} = {p_i}")

    return finalDistribution

def plotDistribution(finalDistribution, time, initialDistribution):
    data = {
        "Read": finalDistribution[0], 
        "Write": finalDistribution[1],
        "E-mail": finalDistribution[2],
        "Surf": finalDistribution[3]
    }
    stages = list(data.keys())
    probabilities = list(data.values())
    p = plt.bar(stages, probabilities, edgecolor = "midnightblue")
    plt.bar_label(p)
    plt.xlabel("Stage")
    plt.ylabel("Probability")
    plt.title(f"Evolution of Markov chain after {time} minutes (Initial distribution = {initialDistribution})")
    plt.show()

tpm = [[0.5, 0.3, 0, 0.2],
     [0.2, 0.5, 0.1, 0.2],
     [0.1, 0.3, 0.3, 0.3],
     [0, 0.2, 0.3, 0.5]]

# 1A
initialDistribution = [1, 0, 0, 0]
finalDistribution = getFinalDistribution(initialDistribution, tpm, 20)
print(f"Initial distribution = {initialDistribution}, Final distribution = {finalDistribution}")
print(f"P(X20 = s|X0 = r) = {finalDistribution[3]}")
plotDistribution(finalDistribution, 20, initialDistribution)

# 1B
initialDistribution = [1, 0, 0, 0]
finalDistribution = getFinalDistribution(initialDistribution, tpm, 25)
print(f"Initial distribution = {initialDistribution}, Final distribution = {finalDistribution}")
plotDistribution(finalDistribution, 25, initialDistribution)

initialDistribution = [0, 0, 0, 1]
finalDistribution = getFinalDistribution(initialDistribution, tpm, 5)
print(f"Initial distribution = {initialDistribution}, Final distribution = {finalDistribution}")
print(f"P(X25 = s|X20 = s) = {finalDistribution[3]}")
plotDistribution(finalDistribution, 5, initialDistribution)

# 1C
p = np.array([tpm[0], tpm[1], tpm[2], tpm[3]])
pT = np.transpose(p)
evals, evecs = np.linalg.eig(pT)
stationary = None
for i in range(len(evals)):
    if (abs(1 - evals[i]) < 0.00001):
        stationary = [evecs[j][i] for j in range(len(evecs))]
if (stationary is not None):
    total = sum(stationary)
    stationary = [round(val/total, 3) for val in stationary]
    print(f"Stationary distribution = {stationary}")

# 1D
limiting = False
currentDistribution = [0.25, 0.25, 0.25, 0.25]
for trial in range(10000):
    nextDistribution = multiply(currentDistribution, tpm)
    val = diff2norm(currentDistribution, nextDistribution) 
    if (val < 0.00001):
        print(f"Limiting distribution found after {trial} trials")
        currentDistribution = [round(val, 3) for val in currentDistribution]
        limiting = True
        break
    else:
        currentDistribution = nextDistribution
if (limiting):
    print(f"Limiting distribution = {currentDistribution}")
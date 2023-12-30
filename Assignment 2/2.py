import matplotlib.pyplot as plt
from random import random

def getFinalDistribution(initialState, p, steps):
    initialDistribution = {}
    for state in range(initialState - steps, initialState + steps + 1):
        if (state == initialState):
            initialDistribution[state] = 1
        else:
            initialDistribution[state] = 0
    
    finalDistribution = initialDistribution
    for step in range(steps):
        updatedDistribution = {}
        for state in range(initialState - steps, initialState + steps + 1):
            val = 0
            if (state != initialState - steps):
                val += p * finalDistribution[state-1]
            if (state != initialState + steps):
                val += (1-p) * finalDistribution[state+1]
            updatedDistribution[state] = val
        finalDistribution = updatedDistribution

    for key, value in finalDistribution.items():
        finalDistribution[key] = round(value, 3)
    return finalDistribution

def simulateRandomWalk(initialState, p, steps):
    states = [initialState]
    currentState = initialState
    for step in range(steps):
        if (random() <= p):
            currentState += 1
        else:
            currentState -= 1 
        states.append(currentState)
    return states

def plotDistribution(finalDistribution, i, steps, p):
    states = list(finalDistribution.keys())
    probabilities = list(finalDistribution.values())
    plt.bar(states, probabilities, edgecolor = "midnightblue")
    plt.xlabel("State number")
    plt.ylabel("Probability")
    plt.title(f"Probability distribution for states after {steps} steps (initial state = {i}, p = {p})")
    plt.show()

def plotRandomWalks(randomWalks, i, steps, p):
    for randomWalk in randomWalks:
        time = [i for i in range(len(randomWalk))]
        plt.plot(time, randomWalk)
    plt.xlabel("Time elapsed")
    plt.ylabel("Current state")
    plt.title(f"Random walk simulation for {steps} steps (inital state = {i}, p = {p})")
    plt.show()

i = 500
steps = 500

# 2A
p = 0.5
randomWalk = simulateRandomWalk(i, p, steps)
finalDistribution = getFinalDistribution(i, p, steps)
print(f"Random walk simulation = {randomWalk}", end = "\n\n")
plotRandomWalks([randomWalk], i, steps, p)
print(f"Final distribution of states in random walk = {finalDistribution}", end = "\n\n")
plotDistribution(finalDistribution, i, steps, p)

# 2B
p = 0.8
randomWalk = simulateRandomWalk(i, p, steps)
finalDistribution = getFinalDistribution(i, p, steps)
print(f"Random walk simulation = {randomWalk}", end = "\n\n")
plotRandomWalks([randomWalk], i, steps, p)
print(f"Final distribution of states in random walk = {finalDistribution}", end = "\n\n")
plotDistribution(finalDistribution, i, steps, p)

# 2C
simulations = 1000
p = 0.8
freq = {}
for state in range(i - steps, i + steps + 1):
    freq[state] = 0

randomWalks = []
for simulation in range(simulations):
    randomWalk = simulateRandomWalk(i, p, steps)
    randomWalks.append(randomWalk)
    finalState = randomWalk[-1]
    freq[finalState] += 1
plotRandomWalks(randomWalks, i, steps, p)

probability = {}
for key, value in freq.items():
    probability[key] = value / simulations
print(f"Final distribution of states in random walk = {probability}")
plotDistribution(probability, i, steps, p)
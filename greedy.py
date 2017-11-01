#- Shane Bodimer 
#- Greedy Knapsack
#- October 31, 2017
#- Chaman Sabharwal

#- Imports ---------------------------------------------------------------------
import sys                                                 #- Operating commands
import json                                                #- JSON posts
from datetime import datetime                              #- Time runtime
from itertools import combinations                         #- Combinations

#- Data ------------------------------------------------------------------------
# Un-comment the dataset you wish to use
from datasetSmall import *                                        #- 1000
# from datasetLarge import *                                        #- 10000

#- Generic Functions -----------------------------------------------------------
# Calc total weight and profit of selected items
def totalSack(comb):
	# Set initial total weight and values to zero
	totalWeight = totalProfit = 0

	# For each item, take name, weight, value
	for item, weight, profit in comb:
		totalWeight += weight
		totalProfit += profit

	# Return totals
	return (totalProfit, -totalWeight)

# Check if optimal
def isOptimal(data, weight):
	# Calc total weight
	sackWeight = 0
	for x in data:
			sackWeight += x[1]

	# If optimally filled to weight
	if(weight >= sackWeight):
		return True

#- Assignment Functions --------------------------------------------------------
# Greedily select items
def greedyKnapsack(items, capacity):
	# Calculate ratios
	ratios = [(index, item[2] / float(item[1])) for index, item in enumerate(items)]

	# Sort list using Heap Sort
	ratios = sorted(ratios, key=lambda x: x[1], reverse=True)

	# Set up result 
	result = []
	weight = 0

	# Invariant: a sack of size zero using a subset of n weights has optimal value 0
	assert(len(result) == 0), "Not empty"

	# Calc result
	for index, ratio in ratios:
		# Invariant: K[i-1,0..W] are optimal values of sacks of sizes 0..W for (i-1)-th row (from subset of first i-1 weights)
		assert(isOptimal(result, weight)), "Not optimal"
		
		# If it can fit
		if items[index][1] + weight <= capacity:
			# Update weight, add to result
			weight += items[index][1]
			result.append(items[index])

	# Invariant: K[i-1,0..W] are optimal values of sacks of sizes 0..W for (i-1)-th row (from subset of first i-1 weights)
	assert(isOptimal(result, weight)), "Not optimal"
	return result

#- Main ------------------------------------------------------------------------
# Set max capacity
capacity = 200

# Set run amount for multiple test
amount = 1000

# Set multiple test variables
maxTime = 0
minTime = 99999999
total = average = 0

#- Run Once --------------------------------------------------------------------
# Start timer
startTime = datetime.now()

# Get selected items
selected = greedyKnapsack(items, capacity)

# End timer
time = str(datetime.now() - startTime)

# Print solution
print("\n\n\nGreedy\n-------------------------")
print("Selected: " + 
      '\n          '.join(sorted(item for item,_,_ in selected)))

# Calc totals
profit, weight = totalSack(selected)

# Print totals
print("Profit:   %i \nWeight:   %i\nTime:     %ss" % (profit, -weight, time))
print("-------------------------\n\n\n")

#- Run Many --------------------------------------------------------------------
# # Run loop number of specified times to test
# for x in range(0, amount):
# 	# Print set
# 	print("Solving: " + str(x))

# 	# Run
# 	startTime = datetime.now()
# 	selected = greedyKnapsack(items, capacity)
# 	time = datetime.now() - startTime
# 	time = time.total_seconds()


# 	# Calc highs/lows
# 	# Skip first sort, lags
# 	if(x != 0):
# 		total += time

# 		if(time > maxTime):
# 			maxTime = time 
# 		if(time < minTime):
# 			minTime = time

# # Calc average
# average = total/amount

# # Print time results
# print("max time:" + str(maxTime))
# print("min time:" + str(minTime))
# print("avg time:" + str(average))






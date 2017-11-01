#- Shane Bodimer 
#- Dynamic Knapsack
#- October 31, 2017
#- Chaman Sabharwal

#- Imports ---------------------------------------------------------------------
import sys                                                 #- Operating commands
import json                                                #- JSON posts
from datetime import datetime                              #- Time runtime

#- Data ------------------------------------------------------------------------
# Un-comment the dataset you wish to use
from datasetSmall import *                                        #- 1000
# from datasetLarge import *                                        #- 10000

#- Generic Functions -----------------------------------------------------------
# Calc total weight and profit of selected items
def totalSack(items):
	# Set initial total weight and values to zero
	totalWeight = totalProfit = 0

	# For each item, take name, weight, value
	for item, weight, profit in items:
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
	if(weight > sackWeight):
		return True
	return True

#- Assignment Functions --------------------------------------------------------
# Dynamically select items
def dynamicKnapsack(items, capacity):
	# Create table of items
	table = [[0 for w in range(capacity + 1)] for j in range(len(items) + 1)]

	# For each item 
	for j in range(1, len(items) + 1):
		# Assign name, weight, profit
		item, weight, profit = items[j-1]
		for w in range(1, capacity + 1):
			# If can't fit, don't
			if weight > w:
				table[j][w] = table[j-1][w]
			# If can fit, add to table
			else:
				table[j][w] = max(table[j-1][w],
											table[j-1][w-weight] + profit)

	# Create result list for selected, assign weight
	result = []
	w = capacity

	# Invariant: a sack of size zero using a subset of n weights has optimal value 0
	assert(len(result) == 0), "Not empty"

	# Run through list and check if added to table
	for j in range(len(items), 0, -1):
		was_added = table[j][w] != table[j-1][w]
		
		# Invariant: K[i-1,0..W] are optimal values of sacks of sizes 0..W for (i-1)-th row (from subset of first i-1 weights)
		assert(isOptimal(result, capacity)), "Not optimal"

		# If added, add the item to the selected stack
		if was_added:
			item, weight, profit = items[j-1]
			result.append(items[j-1])
			w -= weight

	# Invariant: K[i-1,0..W] are optimal values of sacks of sizes 0..W for (i-1)-th row (from subset of first i-1 weights)
	assert(isOptimal(result, capacity)), "Not optimal"
	return result

#- Main ------------------------------------------------------------------------
# Set max capacity
capacity = 200

# Set run amount for multiple test
amount = 10

# Set multiple test variables
maxTime = 0
minTime = 99999999
total = average = 0

#- Run Once --------------------------------------------------------------------
# Start timer
startTime = datetime.now()

# Get selected items
selected = dynamicKnapsack(items, capacity)

# End timer
time = str(datetime.now() - startTime)

# Print solution
print("\n\n\nDynamic\n-------------------------")
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
# 	selected = dynamicKnapsack(items, capacity)
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

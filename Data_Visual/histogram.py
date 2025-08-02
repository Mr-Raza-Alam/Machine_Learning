# histogram
import numpy as np
import matplotlib.pyplot as plt
# create a dataset for histogram
# np.random.seed(5) # set it for reprodcuibility
# dataSet = np.random.normal(loc=4,scale=1,size=500) # generate random value from normal distribution

# plt.figure(figsize=(8,4))
# plt.hist(dataSet,bins=20,color='orange',edgecolor='green')
# plt.title('Random Data Distribution')
# plt.xlabel('Value')
# plt.ylabel('Frequency')
# plt.show()

markScore = np.array([60,62,67,78,89,74,79,75,77,98,88,89,79,68,67,57,54,48,96,92,75])

plt.figure(figsize=(8,4))
plt.hist(markScore,bins=10,color='green',edgecolor='blue')
plt.title('Distribution of IIIrd Sem Marks')
plt.xlabel('Marks')
plt.ylabel('No. of students')
plt.show()

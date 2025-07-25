# Scatter plot 
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5) # for reproduclibility
x = np.random.rand(50)*10 # 50 values b/w the range is 0 - 10
y = np.random.rand(50)*10 # 50 values b/w the range is 0 - 10

plt.figure(figsize=(8,4))
plt.scatter(x,y,color='green',alpha=0.9) # It show relationalship b/w x and y
plt.title('Random Distribution of numbers')
plt.xlabel('X-value')
plt.ylabel('Y-value')
plt.show()

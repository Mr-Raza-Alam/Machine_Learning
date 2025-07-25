# here i am going to plot subplot inside main plot using line chart visual element

import numpy as np
import matplotlib.pyplot as plt

# dataSet for subplot ,so here i am going to plot sine and cosine function as grahp
x = np.linspace(0,10,100)  # 100 values b/w 0-10 i.e linespace divide the range 0-10  into 100 equal parts and store it into a list

y1 = np.sin(x) # return value sin(x) for 100 random value of x as a list form
y2 = np.cos(x) # return value cos(x) for 100 random value of y as a list form

plt.figure(figsize=(8,3))
#plot 1st subplot for sine wave
plt.subplot(1,2,1)
plt.plot(x,y1,'g-') # layout of sine wave will be solid in green color
plt.title('Sine graph')

#plot 2nd subplot for cosine wave
plt.subplot(1,2,2)
plt.plot(x,y2,'b--')
plt.title('Cosine graph')

# Adjust layout to avoid overlap
plt.tight_layout()
plt.show()

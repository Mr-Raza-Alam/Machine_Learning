
# Bar chart

import numpy as np
import matplotlib.pyplot as plt

# Data collection
category = np.array(['Electronics-Device','Grocery-item','Cloths','Accessories','Toy','Beauty-Product','Sports-Item'])
itemSales = np.array([45,120,79,80,50,40,56])

# Data visualization using bar visaul element

plt.figure(figsize=(12,6))
plt.bar(category,itemSales) # here color will set bydefault by python
plt.title('Categorical Value')
plt.xlabel('Item-categories')
plt.ylabel('No. of item sales')
plt.show()

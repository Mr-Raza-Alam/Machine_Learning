# here i am going to draw first chart or graph to visualize the dataFrame of pandas or data of numPy array
'''
so for this , first import some import. libraries to achieve my goal
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#store some data let say store monthly sales record of year 2024 
month = np.array(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
sales = np.array([400,567,1250,565,1460,356,896,980,954,952,943,180])

#plot the line
plt.figure(figsize=(7,5))
plt.plot(month,sales,'k*:',markerfacecolor='blue', linewidth=0.5,alpha=0.8)
# plt.plot(month,sales,marker='o',linestyle='-',color='g') # syntax plt.plot(x-cor. , y-cordi. , formatting_string , **kargs)
plt.title('Monthly Sales Data')
plt.xlabel('Month')
plt.ylabel('Sales')
# plt.grid(True) # for better readability of the data
plt.show()
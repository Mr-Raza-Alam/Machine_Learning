'''
Build a unsupervise learning model ,using K-means clustering algorithm
"C:\\Users\\LENOVO\\Downloads\\wholesale_data.csv"
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import warnings
warnings.filterwarnings("ignore")

#load the dataSet 
data = pd.read_csv("C:\\Users\\LENOVO\\Downloads\\wholesale_data.csv")
#display some values
# print(data.head(6))

# print(data.describe())


from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

scaled_data = scaler.fit_transform(data)  # will return scaled data in list of list of each row's record or value
# print(help(StandardScaler()))
# scaled_data = pd.DataFrame(scaled_data)
# print(scaled_data.head())

# create an intance from KMeans Class for building a model for unsupervise task
# kmeans = KMeans(n_clusters=2,init='k-means++')
# kmeans.fit(scaled_data) # here we instilled scaled_data

# inertia = kmeans.inertia_ # return an inertia value for 2 clusters
# print(inertia) 

# now test 20 different cluster and calculate inertia value for 1-20 no. of clusters

# wscc = []

# for i in range(1,21):
#     kmeans = KMeans(n_clusters= i,init='k-means++')
#     kmeans.fit(scaled_data)
#     wscc.append(kmeans.inertia_)

# print('There are 20 records of inertia \n',wscc)

# plot a Eblow curve to select an optimal value of k i.e appropriate no.of clusters
# plt.figure(figsize=(10,5))
# plt.plot(range(1,21),wscc,'go-',markerfacecolor = 'blue',linewidth=0.7,alpha=0.8)
# plt.title('The Elbow Curve')
# plt.xlabel('No. of Clusters')
# plt.ylabel('Inertia')
# plt.show()

#now build the model with an optimal value of cluster i.e select k = 6 
from sklearn.metrics import silhouette_score
kmeans = KMeans(n_clusters=25,init='k-means++')
kmeans.fit(scaled_data)
pred = kmeans.predict(scaled_data)


df = pd.DataFrame(scaled_data) 
# print(df.head(6))
# now add a new column cluster and assign the predicted value 
df['cluster'] = pred 
accuracy_score = silhouette_score(df,pred)
print(f"\nAccuracy of the model : {accuracy_score*100:.2f}%.")
# print(df.tail(12))
# 
# print('No. of data-points in each cluster among 6 different clusters \n',df['cluster'].value_counts())

# now test the model using user's given records 

def get_cluster_res():
    Channel = int(input('Enter a channel no. (e.g 1,2,3).... : '))
    Region = int(input('Enter a Region (e.g 2,3,5,6,..) : '))
    Fresh = int(input('Enter annaul spending on Fresh product  : '))
    Milk = int(input('Enter annual spending on Milk  : '))
    Grocery  = int(input('Enter annual spending on grocery items : '))
    Frozen = int(input('Enter annual spending on frozen product : '))
    Detergent_Paper = int(input('Enter annual spending on detergent_paper  : '))
    Delicassen = int(input('Enter annual spending on delicassen  : '))
   
   # now create an numpy array to fit a new data point into the model and then check its cluster 
    user_data = np.array([[Channel,Region,Fresh,Milk,Grocery,Frozen,Detergent_Paper,Delicassen]])
    
    #Standardize the user_data
    scaled_userdata = scaler.transform(user_data)

    res = kmeans.predict(scaled_userdata)
    print('The customer belong to cluster : ',res[0])

# get_cluster_res()
# # check accuracy of the model

# accuracy_score = silhouette_score(scaled_data,pred)
# print(f"\nAccuracy of the model : {accuracy_score*100:.2f}%.")



# plt.figure(figsize=(10,5))
# plt.plot(range(1,21),wscc,'go-',markerfacecolor = 'blue',linewidth=0.7,alpha=0.8)
# plt.title('The Elbow Curve')
# plt.xlabel('No. of Clusters')
# plt.ylabel('Inertia')
# plt.show()
'''
Build a model using KNN Alogirthm

'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler,LabelEncoder
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix

import warnings
warnings.filterwarnings("ignore")

# load the dataset from a csv file
df = pd.read_csv("C:\\Users\\LENOVO\\OneDrive\\Desktop\\PythonProg\\ML_Model\\transaction_Records.csv")


label_encoders = {} # this is for mapping non-numerical columns by some label for each column's values

for col in ['TransactionTime','MerchantCategory','CustomerGender','TransactionLocation']:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# Features & target

X = df.drop(['Transaction-id','Fraud'],axis=1)
Y = df['Fraud']
# now our dataset is ready to split into train and test set
# print(X.head())
# print('\n',label_encoders)

# Now its time to split the dataSet into training and testing set

x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.4,random_state=7)

#Feature Scaling
scaler = StandardScaler()

x_train = scaler.fit_transform(x_train)
x_test = scaler.fit_transform(x_test)
# now we have the dataSet that i requried for data modeling

# Logistic Regression Algorthim
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier()
knn.fit(x_train,y_train) # here we are loading the traing the data into the Model to train the model

knn_pred = knn.predict(x_test)
knn_accuracy = accuracy_score(y_test,knn_pred) # it gives the accuracy score of the model over its predicted values

# Display the accuracy and perform other metric for Evaluatin performance of the created model

print(f"K-Nearest Neighbors Model's Accuracy : {knn_accuracy*100:.2f}%")
print('\nKNN Classification Report')
print(classification_report(y_test,knn_pred))

# Confusion Matrix
plt.figure(figsize=(8,4))
sns.heatmap(confusion_matrix(y_test,knn_pred),fmt='d',cmap='coolwarm',annot=True)
plt.title('KNN Confusion Matrix')
plt.show()
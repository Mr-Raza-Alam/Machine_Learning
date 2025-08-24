'''
Build a model to predtic the fraudleant in  Credit Card Detection ,using Decision Tree Algorithm.
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

# print(df.head())
#Handle missing value
# print(df.isnull().sum())


# Distribution of Transaction Amount by Fraud status,using Histogram

plt.figure(figsize=(10,6))
sns.histplot(data=df,x='TransactionAmount',hue='Fraud',multiple='stack',bins=8)
plt.title('Transaction Amount Distribution by Fraud Status')
plt.show()

# label_encoders = {} # this is for mapping non-numerical columns by some label for each column's values

# for col in ['TransactionTime','MerchantCategory','CustomerGender','TransactionLocation']:
#     le = LabelEncoder()
#     df[col] = le.fit_transform(df[col])
#     label_encoders[col] = le

# # Features & target

# X = df.drop(['Transaction-id','Fraud'],axis=1)
# Y = df['Fraud']


# # Now its time to split the dataSet into training and testing set

# x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.4,random_state=7)

# #Feature Scaling
# scaler = StandardScaler()

# x_train = scaler.fit_transform(x_train)
# x_test = scaler.fit_transform(x_test)
# now we have the dataSet that i requried for data modeling

#now import DecisionTreeClassifier An algorithm 
# from sklearn.tree import DecisionTreeClassifier

# decision_tree = DecisionTreeClassifier(random_state=7)
# decision_tree.fit(x_train,y_train)

# pred_val = decision_tree.predict(x_test)

# dtree_accuracy = accuracy_score(y_test,pred_val) # it gives the accuracy score of the model over its predicted values

# # Display the accuracy and perform other metric for Evaluatin performance of the created model

# print(f"Decision Tree Model's Accuracy : {dtree_accuracy*100:.2f}%")
# print('\nDecision Tree Report')
# print(classification_report(y_test,pred_val))

# # confusion matrix

# plt.figure(figsize=(10,5))
# sns.heatmap(confusion_matrix(y_test,pred_val),annot=True, fmt='d',cmap='coolwarm')
# plt.title('Decision Tree Confusion Matrix for classificaton task')
# plt.show()
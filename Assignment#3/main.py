from pandas import read_csv
import pandas
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import numpy as np

# ------------------------
#       load dataset
# ------------------------
path = r'path.csv'
dataset = read_csv(path, header=None)


# ---------------------------
#       check a dataset
# ---------------------------
# print(dataset.head())


# ------------------------
#       splitdataset
# ------------------------
X, y = dataset.values[:, :-1], dataset.values[:,-1]
X = X.astype('float32')
# print(f"X axis parameter is {X.shape}\ty axis parameter is {y.shape}")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=True)
# print(y_test,'\t',y_train)


# ----------------------
#       KNN model
# ----------------------
knn = KNeighborsClassifier(n_neighbors = 18)
knn.fit(X_train,y_train)

y_predict_train = knn.predict(X_train)
y_predict = knn.predict(X_test)
# print(y_test)
# print(y_predict)
accuracy_train = accuracy_score(y_train, y_predict_train)
accuracy = accuracy_score(y_test, y_predict)
print(f'KNN Train Accuracy: {accuracy_train}')
print(f'KNN Predicted Accuracy: {accuracy}\n-------------------------------------------')


# ----------------------
#       SVM model
# ----------------------
model_poly = svm.SVC(kernel='poly', degree=20, C=1.0)
model_poly.fit(X_train,y_train)

y_model_train = model_poly.predict(X_train)
y_model = model_poly.predict(X_test)
# print(f'Lebel of actual output: {y_test}')
# print(f'Lebel of predicted output: {y_model}')

acc_score_train = accuracy_score(y_train,y_model_train)
acc_score = accuracy_score(y_test,y_model)
print(f'SVM Train Accuracy score: {acc_score_train}')
print(f'SVM Predicted Accuracy score: {acc_score}')





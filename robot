import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

df=pd.read_csv("room_cleaning_dataset.csv")
X = df[["Floor Type", "Dust Level", "Foot Traffic", "Battery Level"]]  # Inputs
y = df["Action"]
# dummies = pd.get_dummies(df[['Floor Type','Dust Level','Foot Traffic','Battery Level']],drop_first=True)
# print(dummies)

X_train, X_test, y_train, y_test= train_test_split(X,y,test_size=0.3,random_state=42)
model = LogisticRegression()
model.fit(X_train,y_train)
print(X_train)
print(X_test)
print(model.predict(X_test))
print(model.score(X_test,y_test))
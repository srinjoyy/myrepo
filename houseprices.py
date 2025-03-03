import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
import pickle

# df=pd.read_csv("houseprices.csv")
# # print(df)                                           

# plt.scatter(df.area,df.price)
# # print(plt.show())
# reg=linear_model.LinearRegression()
# reg.fit(df[['area']],df.price)


# print(reg.predict([[1230]]))


# print(reg.score(df[['area']],df[['price']]))

# model=pd.read_csv("new_houseprices.csv")
# reg=linear_model.LinearRegression()
# reg.fit(model[['area']],model.prices)
# # a=reg.predict(model[['area']])

# # model['prices']=a
# # b=model.to_csv("new_houseprices.csv")
# # print(b)

# print(reg.score(model[['area']],model[['prices']]))

t=pd.read_csv("new_houseprices.csv")
# # print(df)

# plt.scatter(df.area,df.price)
# # print(plt.show())
reg=linear_model.LinearRegression()
reg.fit(t[['area']],t.prices)


# print(reg.predict([[1230]]))


# print(reg.score(t[['area']],t[['prices']]))

# print(reg.predict([[6900]]))
# print(reg.score([[6900]],[1038870.95238095]))
# print(reg.predict([[6000]]))

# print(reg.score([[6900],[6000]],[[1038870.95238095],[892970.23809524]]))
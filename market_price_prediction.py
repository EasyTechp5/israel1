# -*- coding: utf-8 -*-
"""Market Price Prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1m5dypIOYTBmJvZhUI1RYBZl-aXKHId8p
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn import metrics

import warnings
warnings.filterwarnings('ignore')

data = pd.read_csv("/content/MarketPricePrediction.csv")
data.head()

data.shape

data.describe()

data.info()

# Exploratory Data Analysis

plt.figure(figsize=(15,7))
plt.plot(data['priceMod'])
plt.title('Market Price Mode.', fontsize=15)
plt.ylabel('Price.')
plt.show()

data.isnull().sum()

data.columns

data.head()

features = ['quantity', 'priceMin', 'priceMax', 'priceMod']

plt.subplots(figsize=(20,10))

for i, col in enumerate(features):
    plt.subplot(2,3,i+1)
    sb.distplot(data[col])
plt.show()

plt.subplots(figsize=(20,10))
for i, col in enumerate(features):
  plt.subplot(2,3,i+1)
  sb.boxplot(data[col])
plt.show()

# Feature Engineering


splitted = data['date'].str.split('-', expand=True)

# data['day'] = splitted[1].astype('int')
data['month'] = splitted[0].astype('str')
# data['year'] = splitted[2].astype('int')

data.head()

data['is_quarter_end'] = np.where(data['month']%3==0,1,0)
data

# # import pandas as pd

# # dates = pd.DataFrame({'date': ['Jan-05', 'Feb-15', 'Mar-10']})

data['date'] = pd.to_datetime(data['date'])
# data['day'] = data['date'].dt.day
data['month'] = data['date'].dt.month

data.head()

data.columns

data['date'].head()


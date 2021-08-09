import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from scipy.stats import mstats

df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')

print(df.head())
'''
ordinal:
    pclass
    age
    sibsp
    parch
    ticket
    fare
nominal:
    sex
    embarked
'''
df.dropna(inplace=True)

y = df['Survived']
X = pd.get_dummies(df, columns=['Sex', 'Embarked'])
del X['Survived']
del X['Name']
del X['PassengerId']
mm_scaler = MinMaxScaler()
X = mm_scaler.fit_transform(X._get_numeric_data())





print(X[0:2])

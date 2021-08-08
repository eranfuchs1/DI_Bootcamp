import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random
import datetime


def create_array(start,length, step):
    return np.array([_ for _ in range(start, start + length, step)])

numpy_array = create_array(6, 100, 4)


a = np.array([1,2,3,np.nan,5,6,7,np.nan])
filter_arr = a * 0 == 0
newa = a[filter_arr]
print(newa)


random_numpy_array = np.array([random.randint(1,100) for _ in range(5 * 6)]).reshape((5,6))

for row in random_numpy_array:
    print(np.max(row))



series = pd.Series(np.take(list('abcdefghijklmnop'), np.random.randint(16, size=500)))
uniques, count = np.unique(series, return_counts = True)

print(list(zip(uniques, count)))


series = pd.Series(['01 Jan 2020', '10-19-2020', '20150303', '2013/04/04', '2012-05-05', '2013-06-06T12:20'])

df = pd.DataFrame([[item.day, item.week, item.day_of_year, item.day_of_week] for item in pd.to_datetime(series)]).rename(columns={0:'day_of_month',1:'week_of_year', 2: 'day_of_year', 3:'day_of_week'}, index={key:value for key, value in enumerate(series)})
print(df)


df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

print(df)
types, counts = np.unique(np.array(df.dtypes), return_counts=True)

print(list(zip(types, counts)))

print(df.rename(columns={'Type':'TypeOfCar'}).head)

sums = df.isnull().sum()

print(sums)

print(sums[sums == sums.max()])

del df['EngineSize']
df.pop('Length')
print('EngineSize' not in df, 'Length' not in df)



df1 = pd.DataFrame({'fruit': ['apple', 'banana', 'orange'] * 3,
    'weight': ['high', 'medium', 'low'] * 3,
    'price': np.random.randint(0, 15, 9)})

df2 = pd.DataFrame({'pazham': ['apple', 'orange', 'pine'] * 2,
    'kilo': ['high', 'low'] * 3,
    'price': np.random.randint(0, 15, 6)})

df_merged = pd.merge(left=df1, right=df2, left_on=['fruit', 'weight'], right_on=['pazham','kilo']).drop_duplicates()
print(df_merged)

df = pd.DataFrame(["STD,City\tState",
    "33,Kolkata\tWest Bengal",
    "44,Chennai\tTamil Nadu",
    "40,Hyderabad\tTelengana",
    "80,Bangalore\tKarnataka"], columns=['row'])


arr = [_.split(',') for _ in df['row']]
arr = [_[0:1] + _[1].split('\t') for _ in arr]
#print(arr)
print(pd.DataFrame(arr[1:]).rename(columns={key:value for key, value in enumerate(arr[0])}))

names = ["mpg", "cylinders", "displacement", "horsepower", "weight", "acceleration", "model_year", "origin", "car_name"]
df_mpg = pd.read_csv("auto-mpg.data", header=None, names=names, delim_whitespace=True)


def scatter_plot(df):
    plt.scatter(df['displacement'], df['acceleration'])
    plt.xlabel('displacement')
    plt.ylabel('acceleration')
    plt.grid()
    plt.show()

scatter_plot(df_mpg)

def bar_plot(df):
    model_year = np.array(df['model_year'])
    car_name = np.array(df['car_name'])
    matching = df.iloc[['toyota' in name and year == 78 for year, name in zip(model_year, car_name)]]
    print(matching)

bar_plot(df_mpg)

def line_plot(df):
    df.dropna(inplace=True)
    diffs = np.diff(np.array(df.sort_values('model_year')['weight']))
    array = np.array(np.array(df.sort_values('model_year')['model_year']))[:-1]
    plt.plot(array, diffs)
    plt.show()

line_plot(df_mpg)

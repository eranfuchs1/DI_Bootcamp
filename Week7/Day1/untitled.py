import numpy as np

lst = [2, 4, 6, 8, 13, 2020]
numpy_arr = np.array(lst)

def func(arr):
    return np.min(arr), np.std(arr), np.prod(arr), np.dot(arr, arr), arr - 4


print(func(numpy_arr))

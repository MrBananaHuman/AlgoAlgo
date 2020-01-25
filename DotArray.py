import numpy as np

def solution(arr1, arr2):
    one = np.array(arr1)
    two = np.array(arr2)
    return np.dot(one, two).tolist()

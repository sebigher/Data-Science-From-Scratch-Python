"""
Created on Sun Sep  12 04:36:40 2019
@author: Neeraj
Description: Computes model assessment metrics like accuracy, precision, recall and F1-score.
Reference: Chapter 11 : Machine Learning
"""

import random
from typing import List, TypeVar, Tuple
X = TypeVar('X') # generic type to represent a data point

def split_data(data: List[X], prob: float) -> Tuple[List[X], List[X]]:
    """Split data into fractions [prob, 1-prob]"""
    data = data[:] # make a shallow copy of the data
    random.shuffle(data)
    cut = int(len(data)*prob)
    return data[:cut], data[cut:]

data = [n for n in range(1000)]
train, test = split_data(data, 0.75)

print(len(train))
print(len(test))
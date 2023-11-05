import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm
from sklearn import datasets
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from math import sqrt
from sklearn.preprocessing import StandardScaler
from scipy.spatial.distance import cdist
from scipy.stats import pearsonr

def Process(sum_order):
    df = pd.DataFrame(sum_order, index = [x+1 for x in range(0,12)], columns = ['BLN'])
    sma_array = []
    accuracy_arr = []
    accuracy = 0
    for x in range(0, 3):
        sma_dump = df['BLN'].rolling(x+2, min_periods=1).mean()
        accuracy_dump = r2_score(df['BLN'], sma_dump)
        if x < 1:
            df['SMA'] = sma_dump
            accuracy = accuracy_dump
        sma_array.append(sma_dump)
        accuracy_arr.append(accuracy_dump)

    for x in range(1, 3):
        if accuracy_arr[x-1] < accuracy_arr[x]:
            df['SMA'] = sma_array[x]
            accuracy = accuracy_arr[x]
    
    return df, accuracy
import pandas as pd
import numpy as np



def preprocessing():
    dataset = pd.read_csv('Testing.csv')
    dataset.keys()

    dataset['PESAN'] = dataset['PESAN'].abs()
    dataset['KODEPRODUK'] = dataset['KODEPRODUK'].str.replace(" ", "")
    dataset['PESAN'] = dataset['PESAN'].astype(int)

    bulan = [x for x in range(0,12)]
    sum_order = [0 for x in range(0,12)]

    data_permonth = [0 for x in range(0, 12)]

    for x in bulan:
        data_permonth[x] = dataset.loc[dataset['BLN'] == x+1].reset_index(drop=True)
        df = pd.DataFrame(data_permonth[x])
        data_permonth[x] = df.sort_values(by='TGL')

    dataset = pd.concat(data_permonth)
    dataset = dataset.reset_index(drop=True)

    return dataset, sum_order

def product_spec(dataset):
    kode_produk = dataset['KODEPRODUK'].unique()
    key = input("Input produk yang kamu ingin prediksi! (1-242)")
    key = int(key)
    key_produk = kode_produk[key]

    dataset_filter = dataset.loc[dataset['KODEPRODUK'] == key_produk]
    dataset = dataset_filter.reset_index(drop=True)

    return dataset, key_produk
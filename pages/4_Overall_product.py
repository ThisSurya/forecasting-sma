import streamlit as st
from Backend.SimpleMovingAverage import *
st.set_page_config(page_title="Overall Product", page_icon="📊")

def Overall_product():
    st.write('## Analisis keseluruhan pesanan produk')
    dataset = Preprocessing()
    sum_order = sum_permonth(dataset)

    df, accuracy = process(sum_order)
    x = [x for x in range(1, 13)]

    st.scatter_chart(df['BLN'])
    
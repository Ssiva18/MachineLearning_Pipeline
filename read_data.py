import pandas as pd
import numpy as np 
import os 


# Reading the dataset
path = r"C:\Users\Admin\Downloads\HuggingFace_Datasets_Hub.csv"

def data_read(path):
    df = pd.read_csv(path)
    return df

def data_overview(df):
    print("\n First 5 rows:")
    print(df.head())

    print("\n Dataset Info:")
    print(df.info())

    print("\n Summary:")
    print(df.describe())




if __name__ == "__main__":
    data = data_read(path)
    print(data)

    data_overview(data)

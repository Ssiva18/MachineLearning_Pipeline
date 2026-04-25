import pandas as pd
import numpy as np 
import os 


# Reading the dataset
path = r"C:\Users\Admin\Downloads\HuggingFace_Datasets_Hub.csv"

def data_read(path):
    df = pd.read_csv(path)
    return df





if __name__ == "__main__":
    data = data_read(path)
    print(data)
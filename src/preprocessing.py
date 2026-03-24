import pandas as pd

# dataset path
path = "data/raw/DataCoSupplyChainDataset.csv"

def load_data():
    df = pd.read_csv(path)
    return df

def clean_data(df):
    # remove duplicates
    df = df.drop_duplicates()
    # fill missing values
    df = df.ffill()
    return df

def preprocess_pipeline():
    df = load_data()
    df = clean_data(df)
    return df

# run preprocessing
df = preprocess_pipeline()

print(df.head())
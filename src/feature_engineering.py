import pandas as pd

def create_features(df):
    # total order value
    if 'Order Item Quantity' in df.columns and 'Sales per customer' in df.columns:
        df['total_value'] = df['Order Item Quantity'] * df['Sales per customer']
    return df

def encode_features(df):
    categorical_cols = df.select_dtypes(include=['object']).columns
    df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)
    return df

def feature_pipeline(df):
    df = create_features(df)
    df = encode_features(df)
    return df
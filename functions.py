import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def preprocess_data(df):
    """Basic preprocessing: fill missing numeric values and encode categoricals."""
    df = df.fillna(df.median(numeric_only=True))
    df = pd.get_dummies(df, drop_first=True)
    return df

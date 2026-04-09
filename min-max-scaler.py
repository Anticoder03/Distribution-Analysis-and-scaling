import pandas as pd

data = pd.read_csv('data.csv')

# Select numeric columns directly
num_cols = data.select_dtypes(include=['number']).columns

def scaler(col):
    min_val = col.min()
    max_val = col.max()
    
    if max_val - min_val == 0:
        return col
    
    return (col - min_val) / (max_val - min_val)

# Apply scaler
data[num_cols] = data[num_cols].apply(scaler)

print(data.head())
import pandas as pd

def load_data():
    df = pd.read_csv("data/student_dataset_10000_rows.csv")
    return df

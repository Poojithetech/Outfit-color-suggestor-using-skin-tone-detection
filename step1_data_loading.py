# step1_load_data.py

import pandas as pd

def load_dataset(file_path):
    df = pd.read_csv(file_path, delimiter=';')

    print("Preview of dataset:")
    print(df.head())

    print("\nDataset info:")
    print(df.info())
    return df

if __name__ == "__main__":
    path = r"D:\python\Skin tone\Profile of Body Metrics and Fashion Colors.csv"
    df = load_dataset(path)

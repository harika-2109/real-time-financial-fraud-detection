import pandas as pd

def main():
    # Load sample transaction data
    df = pd.read_csv("sample_data.csv")

    # Show first few rows
    print("Sample transaction data:")
    print(df.head())

if __name__ == "__main__":
    main()

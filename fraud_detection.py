import pandas as pd

def main():
    # Load sample transaction data
    df = pd.read_csv("sample_data.csv")

    # Show first few rows
    print("Sample transaction data:")
    df["high_amount_flag"] = df["amount"] > 1000

    print("Transaction data with high amount flag:")
    print(df)

if __name__ == "__main__":
    main()

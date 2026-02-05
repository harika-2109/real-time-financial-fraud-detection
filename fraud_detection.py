import pandas as pd

def main():
    # Load sample transaction data
    df = pd.read_csv("sample_data.csv")

    # Convert timestamp to datetime
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    # Sort by time
    df = df.sort_values("timestamp")

    # Feature 1: High-value transaction flag
    df["high_amount_flag"] = df["amount"] > 1000

    # Feature 2: Transaction count per user (simple velocity)
    df["transaction_count"] = df.groupby("user_id")["transaction_id"].transform("count")

    print("Transaction data with engineered features:")
    print(df)

if __name__ == "__main__":
    main()

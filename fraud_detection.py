import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score, recall_score

def main():
    # Load data
    df = pd.read_csv("sample_data.csv")
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    # Feature engineering
    df["high_amount_flag"] = df["amount"] > 1000
    df["transaction_count"] = df.groupby("user_id")["transaction_id"].transform("count")

    # Features and label
    X = df[["amount", "high_amount_flag", "transaction_count"]]
    y = df["is_fraud"]

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    # Train model
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Evaluate model
    y_pred = model.predict(X_test)
    precision = precision_score(y_test, y_pred, zero_division=0)
    recall = recall_score(y_test, y_pred, zero_division=0)

    print("Model Evaluation")
    print("Precision:", precision)
    print("Recall:", recall)
    print("\n--- Real-Time Fraud Detection Simulation ---")

    # Simulate real-time scoring
    for i in range(len(X_test)):
        transaction = X_test.iloc[i]
        prediction = model.predict([transaction])[0]

        label = "FRAUD" if prediction == 1 else "LEGIT"
        print(f"Transaction {i + 1}: {label}")

if __name__ == "__main__":
    main()


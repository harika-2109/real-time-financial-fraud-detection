# Real-Time Financial Fraud Detection using Machine Learning

## Overview
This project demonstrates an end-to-end machine learning pipeline for detecting
fraudulent financial transactions while minimizing false alerts on legitimate activity.

The project is inspired by a real-world fraud detection use case from a financial
services innovation challenge and is implemented as a portfolio project to showcase
data science and applied machine learning skills.


## Business Problem
Financial institutions often face a trade-off between:
- Detecting fraudulent transactions accurately
- Avoiding false positives that block genuine customer transactions

High false-positive rates negatively impact customer experience and increase
operational costs due to manual fraud reviews.

The goal of this project is to build a baseline fraud detection system that balances
fraud detection accuracy with reduced false alerts.


## Data Description
The dataset represents transaction-level financial activity with the following attributes:
- Transaction ID
- User ID
- Transaction amount
- Timestamp
- Location
- Device identifier
- Fraud label (binary)

A small, realistic sample dataset is used to demonstrate the full pipeline.

## Approach

### 1. Data Ingestion
- Loaded structured transaction data from CSV
- Parsed timestamps and prepared data for analysis

### 2. Feature Engineering
Behavioral features were engineered to improve fraud detection:
- **High-value transaction flag** to identify unusually large amounts
- **Transaction velocity** to capture frequent user activity patterns

These features help distinguish fraudulent behavior from normal usage.

### 3. Machine Learning Model
- Trained a **Random Forest classifier** on engineered features
- Selected for its robustness on tabular data and interpretability

### 4. Model Evaluation
- Evaluated using **precision** and **recall**
- Focused on reducing false positives while maintaining fraud detection capability

### 5. Real-Time Simulation
- Simulated real-time fraud detection by scoring transactions one at a time
- Demonstrates how the model could be applied in a streaming or production setting

## Technologies Used
- Python
- Pandas
- Scikit-learn
- Machine Learning (Classification)
- Feature Engineering

## Results
- Implemented a complete baseline fraud detection pipeline
- Demonstrated behavioral feature engineering for fraud use cases
- Evaluated model performance using business-relevant metrics


##  Key Learnings
- Designing end-to-end ML pipelines for financial data
- Engineering behavioral fraud features
- Handling imbalanced classification problems
- Evaluating ML models using precision and recall
- Translating business problems into data science solutions






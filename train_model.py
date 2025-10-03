# Simple Customer Churn Prediction (placeholder demo)
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Example small dataset
data = {
    "tenure": [1, 12, 24, 5],
    "monthly_charges": [70, 20, 50, 90],
    "churn": [1, 0, 0, 1]
}
df = pd.DataFrame(data)

X = df[["tenure", "monthly_charges"]]
y = df["churn"]

# Train model
model = RandomForestClassifier(random_state=42)
model.fit(X, y)

print("Model trained! Example prediction:", model.predict([[6, 40]])[0])

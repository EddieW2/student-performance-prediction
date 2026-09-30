import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

data = pd.read_csv("ml_model/student-mat.csv", sep=";")

print("Dataset loaded successfully.")
print(data.shape)

def classify_performance(grade):
    if grade < 10:
        return "Low"
    elif grade < 14:
        return "Medium"
    else:
        return "High"


data["performance"] = data["G3"].apply(classify_performance)

features = [
    "age",
    "studytime",
    "absences",
    "G1",
    "G2"
]

X = data[features]
y = data["performance"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

print("Model training complete.")

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("\nModel Accuracy:")
print(f"{accuracy * 100:.2f}%")

print("\nClassification Report:")
print(classification_report(y_test, predictions))

joblib.dump(model, "ml_model/student_performance_model.pkl")

print("\nModel saved successfully.")
import joblib
import pandas as pd


# Load the trained model
model = joblib.load("ml_model/student_performance_model.pkl")

# Example student
student = pd.DataFrame([{
    "age": 17,
    "studytime": 3,
    "absences": 4,
    "G1": 14,
    "G2": 15
}])

# Make prediction
prediction = model.predict(student)

print("Predicted performance:", prediction[0])
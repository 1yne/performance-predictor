import joblib
import pandas as pd

model_data = joblib.load("student_model.pkl")
model = model_data["model"]
features = model_data["features"]

student = pd.DataFrame(
    {
        "previous_exam_score": [78],
        "attendance_percentage": [90],
        "study_hours_per_day": [3],
        "assignments_completed": [9],
        "assignment_average": [80],
        "quiz_average": [76],
        "classes_missed": [3],
    }
)

student = student[features]

predicted_score = model.predict(student)[0]

prediction = max(0, min(100, predicted_score))

print(prediction)

import joblib
import pandas as pd
import sys
import json

data = json.loads(sys.argv[1])

model_data = joblib.load("student_model.pkl")
model = model_data["model"]
features = model_data["features"]

student = pd.DataFrame(
    {
        "previous_exam_score": [data[0]],
        "attendance_percentage": [data[1]],
        "study_hours_per_day": [data[2]],
        "assignments_completed": [data[3]],
        "assignment_average": [data[4]],
        "quiz_average": [data[5]],
        "classes_missed": [data[6]],
    }
)

student = student[features]

predicted_score = model.predict(student)[0]

prediction = max(0, min(100, predicted_score))

print(prediction)

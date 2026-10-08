import pandas as pd
import joblib
 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
 
 
# --------------------------------------------------
# 1. Load dataset
# --------------------------------------------------
 
data = pd.read_csv("student_data.csv")
 
print("Dataset loaded successfully")
print()
 
print(data.head())
 
 
# --------------------------------------------------
# 2. Define input features
# --------------------------------------------------
 
features = [
    "previous_exam_score",
    "attendance_percentage",
    "study_hours_per_day",
    "assignments_completed",
    "assignment_average",
    "quiz_average",
    "classes_missed"
]
 
X = data[features]
 
 
# --------------------------------------------------
# 3. Define target variable
# --------------------------------------------------
 
y = data["final_exam_score"]
 
 
# --------------------------------------------------
# 4. Split data into training and testing sets
# --------------------------------------------------
 
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)
 
 
print()
print("Training records:", len(X_train))
print("Testing records:", len(X_test))
 
 
# --------------------------------------------------
# 5. Create Linear Regression model
# --------------------------------------------------
 
model = LinearRegression()
 
 
# --------------------------------------------------
# 6. Train model
# --------------------------------------------------
 
model.fit(X_train, y_train)
 
print()
print("Model training completed")
 
 
# --------------------------------------------------
# 7. Predict test data
# --------------------------------------------------
 
predictions = model.predict(X_test)
 
 
# --------------------------------------------------
# 8. Evaluate model
# --------------------------------------------------
 
mae = mean_absolute_error(
    y_test,
    predictions
)
 
mse = mean_squared_error(
    y_test,
    predictions
)
 
rmse = mse ** 0.5
 
r2 = r2_score(
    y_test,
    predictions
)
 
 
print()
print("----- MODEL PERFORMANCE -----")
 
print(f"Mean Absolute Error: {mae:.2f}")
print(f"Root Mean Squared Error: {rmse:.2f}")
print(f"R2 Score: {r2:.2f}")
 
 
# --------------------------------------------------
# 9. Display actual vs predicted scores
# --------------------------------------------------
 
results = pd.DataFrame({
    "Actual Score": y_test,
    "Predicted Score": predictions
})
 
print()
print("----- ACTUAL VS PREDICTED -----")
 
print(results)
 
 
# --------------------------------------------------
# 10. Display Linear Regression coefficients
# --------------------------------------------------
 
print()
print("----- MODEL COEFFICIENTS -----")
 
for feature, coefficient in zip(
    features,
    model.coef_
):
    print(
        f"{feature}: {coefficient:.3f}"
    )
 
 
print()
print(
    f"Intercept: {model.intercept_:.3f}"
)
 
 
# --------------------------------------------------
# 11. Save trained model
# --------------------------------------------------
 
joblib.dump(
    {
        "model": model,
        "features": features
    },
    "student_model.pkl"
)
 
print()
print("Model saved as student_model.pkl")
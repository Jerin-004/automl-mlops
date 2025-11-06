from supervised.automl import AutoML
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# Load dataset
data = load_iris()
X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# AutoML Training (AUTO ML HAPPENS HERE)
automl = AutoML(mode="Explain", total_time_limit=60)  
automl.fit(X_train, y_train)

# Evaluate Model
y_pred = automl.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print("✅ Model Accuracy:", acc)

# ✅ PROOF OF AUTOML - Show the models AutoML tried
print("\n===== AUTO ML LEADERBOARD (Proof of AutoML) =====")
print(automl.get_leaderboard())

# Save Model
joblib.dump(automl, "model.pkl")
print("\n✅ Model saved as model.pkl")

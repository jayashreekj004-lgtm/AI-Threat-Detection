import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

data = pd.read_csv("dataset.csv")

X = data.drop("threat", axis=1)
y = data["threat"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)

def predict_threat(cpu, login, traffic):
    prediction = model.predict([[cpu, login, traffic]])
    if prediction[0] == 1:
        return "⚠️ Threat Detected"
    else:
        return "✅ Normal Activity"
    
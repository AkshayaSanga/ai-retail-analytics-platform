import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load data
df = pd.read_csv("cleaned_sales.csv")

# Features (input)
X = df[['Month', 'Quantity']]

# Target (output)
y = df['Sales']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

print("✅ Model Trained Successfully")

# Accuracy
score = model.score(X_test, y_test)
print("Model Accuracy:", score)
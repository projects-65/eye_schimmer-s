from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
import pickle
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Load the dataset
data = pd.read_csv("data/dataset.csv")  # Replace "your_dataset.csv" with the actual file path

# List of unnecessary columns
unnecessary_columns = ['Name', 'Age', 'Sex','onlineplatforms', 'Nature']

# Drop unnecessary columns
data = data.drop(columns=unnecessary_columns)

# Impute missing values for numerical features with mean
numerical_features = ['wearables', 'Duration', 'screenillumination', 'workingyears', 'hoursspentdailycurricular', 'hoursspentdailynoncurricular', 'Gadgetsused', 'levelofgadjetwithrespecttoeyes', 'Distancekeptbetweeneyesandgadjet', 'Avgnighttimeusageperday', 'Blinkingduringscreenusage', 'Difficultyinfocusingafterusingscreens', 'freqquencyofcomplaints', 'Severityofcomplaints','Ocularsymptomsobservedlately','Symptomsobservingatleasthalfofthetimes']
for feature in numerical_features:
    data[feature].fillna(data[feature].mean(), inplace=True)

# Detect outliers using z-score
from scipy import stats
z_scores = stats.zscore(data[numerical_features])
abs_z_scores = np.abs(z_scores)
filtered_entries = (abs_z_scores < 3).all(axis=1)
data = data[filtered_entries]

# Split the dataset into features (X) and target variables (y)
X = data.drop(columns=['Schimers1Lefteye', 'Schimers1righteye', 'Schimers2Lefteye', 'Schimers2righteye'])
y = data[['Schimers1Lefteye', 'Schimers1righteye', 'Schimers2Lefteye', 'Schimers2righteye']]

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scaling numerical features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train[numerical_features])
X_test_scaled = scaler.transform(X_test[numerical_features])

# Initialize the model
model = RandomForestRegressor(random_state=42)

# Fit the model on the training data
model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)
# Evaluate the model on the testing data
accuracy = model.score(X_test_scaled, y_test)

print("Model Accuracy:", accuracy)

mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mse)
r_squared = r2_score(y_test, y_pred)

print("Mean Squared Error (MSE):", mse)
print("Mean Absolute Error (MAE):", mae)
print("Root Mean Squared Error (RMSE):", rmse)
print("R-squared (R2):", r_squared)


# Save the model to a file using pickle
with open('models/rf_model.pkl', 'wb') as f:
    pickle.dump(model, f)

# Import required libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
from soil_grid_test import fetch_api_data

api_data = fetch_api_data()

# Print or use the values in your ML model
# print(f"API Data: {api_data}")

# Example: Accessing individual values
latitude = api_data['latitude']
longitude = api_data['longitude']
nitrogen = api_data['nitrogen']
soil_pH = api_data['pH']

# Load your dataset (replace 'crop_data.csv' with your actual dataset)
data = pd.read_csv(r'C:\Users\naman\Downloads\Crop_recommendation1.csv')

# Display the first few rows of the dataset
print(data.head())

# Split the dataset into features (X) and target (y)
# Assuming your dataset has features like 'moisture', 'temperature', 'nitrogen', etc., and the target column is 'crop'
X = data[['N', 'ph']]  # Add other soil features if you have more
y = data['label']  # Target variable - crop to recommend

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize the Decision Tree Classifier
dt_model = DecisionTreeClassifier()

# Train the model
dt_model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = dt_model.predict(X_test)

# Evaluate the model's performance
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")

# Show detailed classification report
print(classification_report(y_test, y_pred))


# Example: Make a prediction on a new set of soil data from API
# Replace with the values you receive from the API
new_soil_data = [[nitrogen,soil_pH]]  # Example input for moisture, temperature, nitrogen, pH, SOC
predicted_crop = dt_model.predict(new_soil_data)

print(f"Recommended Crop: {predicted_crop[0]}")

from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load the trained model
with open('models/rf_model.pkl', 'rb') as f:
    model = pickle.load(f)

# List of dropped columns
dropped_columns = ['Name', 'Age', 'Sex', 'onlineplatforms', 'Nature', 'frequencyofdryeyes','Complaintsfrequency']

# Initialize Flask application
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Define a route for prediction
@app.route('/submit', methods=['POST'])
def submit():
    try:
        # Get data from the request
        input_data = request.form.to_dict()

        # Convert input data to a DataFrame
        input_df = pd.DataFrame(input_data, index=[0])

        # Preprocess the input data (scaling numerical features)
        numerical_features = ['wearables', 'duration', 'screenillumination', 'workingyears', 'hoursspentdailycurricular', 'hoursspentdailynoncurricular', 'Gadgetsused', 'levelofgadjetwithrespecttoeyes', 'Distancekeptbetweeneyesandgadjet', 'Avgnighttimeusageperday', 'Blinkingduringscreenusage', 'Difficultyinfocusingafterusingscreens', 'freqquencyofcomplaints', 'Severityofcomplaints', 'Ocularsymptomsobservedlately', 'Symptomsobservingatleasthalfofthetimes']

        # Preprocess the input data (scaling numerical features)
        scaler = StandardScaler()
        input_df[numerical_features] = scaler.fit_transform(input_df[numerical_features])

        # Make prediction
        prediction = model.predict(input_df[numerical_features])

        # Extract values for keys
        values = prediction[0]

        # Create a dictionary with keys and values
        result = {
            'Schimers1Lefteye': values[0],
            'Schimers1righteye': values[1],
            'Schimers2Lefteye': values[2],
            'Schimers2righteye': values[3]
        }
        # Render result.html with the processed data
        return render_template('result.html', data=result)
    
    except Exception as e:
        # Return error message if prediction fails
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)


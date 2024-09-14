# Eye-schimmers web app

This web application helps users input eye health parameters and display the results in a tabular format. Each time the result page is loaded, a new health-related quote is displayed. The app runs locally using the Flask web framework.

## Features
- Display eye health test results in a structured table.
- Generate a random motivational health-related quote every time the result page is accessed.
- Simple, modern UI with a clean layout.

## Prerequisites

Make sure you have the following installed on your machine:
- **Python 3.x** (Download from [python.org](https://www.python.org/))
- **Flask** (Installable via `pip`)

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/projects-65/eye_schimmer-s.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd eye-health-assessment
    ```

3. **Install the required Python libraries**:
    ```bash
    pip install flask
    ```

## Running the Application

1. Start the Flask development server:
    ```bash
    python app.py
    ```

2. Open your browser and visit:
    ```
    http://127.0.0.1:5000
    ```

## Project Structure

eye-health-assessment/ │
    ├── templates/ │
        ├── result.html # HTML file for showing the results and a random quote │ 
    ├── app.py # Main Flask server script
    ├── README.md # Instructions to set up and run the project 
    └── requirements.txt # Dependencies

## Displaying Results

After submitting the data, the app will show the eye health results in a table like this:

| Test          | Left Eye | Right Eye |
|---------------|----------|-----------|
| Schimers1     | 10       | 12        |
| Schimers2     | 14       | 15        |

Each time you visit the result page, a new health-related quote will be displayed below the table.

## Random Quotes

The result page shows a random health-related quote from a predefined list every time you visit it. Here are some examples:
- "Take care of your body. It’s the only place you have to live."
- "A fit body, a calm mind, a house full of love."
- "Health is the greatest gift."

You can add more quotes by modifying the `quotes` array in `result.html`.
##output images:
![e1](https://github.com/user-attachments/assets/6ea1ea7c-d3ab-475e-94fc-8e9d69b8f0d1)
![e2](https://github.com/user-attachments/assets/8ece04fa-e488-43c1-8262-b13580c44f8d)
![e3](https://github.com/user-attachments/assets/ae63dda8-daad-4a09-b62c-77bf9cbf775e)
![e4](https://github.com/user-attachments/assets/14bf3577-916d-4a23-b835-206ba920c4e1)
![e5](https://github.com/user-attachments/assets/2d6652e0-b715-4e19-b342-5a37398a6923)

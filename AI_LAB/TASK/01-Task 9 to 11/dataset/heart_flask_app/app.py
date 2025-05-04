from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)

# Load pre-trained model
with open('model_SVC.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None

    if request.method == 'POST':
        try:
            age = int(request.form['age'])
            sex = int(request.form['sex'])
            cp = int(request.form['cp'])
            chol = int(request.form['chol'])
            maxhr = int(request.form['maxhr'])

            input_data = np.array([[age, sex, cp, chol, maxhr]])
            pred = model.predict(input_data)[0]
            prediction = "Heart Disease Detected" if pred == 1 else "No Heart Disease"
        except ValueError:
            prediction = "Invalid input. Please enter valid numbers."
        except Exception as e:
            prediction = f"An error occurred: {str(e)}"

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)

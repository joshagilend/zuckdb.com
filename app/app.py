from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import requests, json, os

app = Flask(__name__)

def generate_gemini_secret(date):

    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"
    headers = {
        "Content-Type": "application/json",
    }
    data = {
        "contents": [{
            "parts": [{"text": f"Tell me a fun secret from this day: {date}."}]
        }]
    }
    params = {
        "key": os.getenv("GEMINI_KEY")
    }

    response = requests.post(url, headers=headers, json=data, params=params)
    gemini_text = response.json()["candidates"][0]["content"]["parts"][0]["text"]
    return gemini_text


@app.route('/date', methods=['GET', 'POST'])
def date():
    if request.method == 'POST':
        # Extract the date from the form input
        input_date = request.form.get('date')
        # Convert the input date string to a datetime object
        try:
            formatted_date = datetime.strptime(input_date, "%Y-%m-%d").strftime("%B %d, %Y")
        except ValueError:
            # If the input is invalid, default to today's date
            formatted_date = datetime.now().strftime("%B %d, %Y")
    else:
        # Default to today's date for GET requests
        formatted_date = datetime.now().strftime("%B %d, %Y")
    
    secret_text = generate_gemini_secret(formatted_date)
    return render_template('date.html', date=formatted_date, secret_text=secret_text)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

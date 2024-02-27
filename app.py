from flask import Flask, render_template
from datetime import datetime  # Import datetime

app = Flask(__name__)

@app.route('/')
def home():
    # Get the current date
    today_date = datetime.now().strftime("%B %d, %Y")  # Format the date as you like, e.g., "March 03, 2024"
    return render_template('date.html', date=today_date)

if __name__ == '__main__':
    app.run()
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! This is a simple Flask app.'

if __name__ == '__main__':
    app.run()
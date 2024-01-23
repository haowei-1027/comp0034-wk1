from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to my Paralympics app!'

@app.route('/<name>')
def personalized_home(name):
    return f'Hello {name} and welcome to my Paralympics app!'

if __name__ == '__main__':
    app.run(debug=True)
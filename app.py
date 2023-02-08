from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1> Hello, World! </h1>'

@app.route('/index')
def inde():
    return '<h1> Hello, World! </h1>'

@app.route('/home')
def home():
    return '<h1> Home page! </h1>'

@app.route('/about')
def home():
    return '<h1> About page! </h1>'
    

if __name__ == '__main__':
    app.run()
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>The website Page</h1>'

@app.route('/app')
def myapp():
    return '<h1>The app page</h1>'

@app.route('/api')
def api():
    return '<h1>The API Thing here</h1>'


if __name__=='__main__':
    app.run(debug=True)
from flask import Flask

app = Flask(__name__)

@app.route('/')
def route():
    return {
        'name': ["This app is for test purpose"]
    }

if __name__ == '__main__':
    app.run()

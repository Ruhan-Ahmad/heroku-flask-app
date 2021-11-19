from flask import Flask

app = Flask(__name__)

@app.route('/')
def route():
    return {
        'name': [{"first-Name": "Ruhan", "last-Name": "Ahmad", "father-First-Name": "Faiz", "father-Last-Name": "Rasool"}]
    }

if __name__ == '__main__':
    app.run()
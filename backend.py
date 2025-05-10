from flask import Flask, request

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def odbierz_dane():
    dane = request.json
    print("Dostałem dane:", dane)
    return "OK"

@app.route('/')
def home():
    return "Działa! 🚀"

app.run(host='0.0.0.0', port=8000)

from flask import Flask, render_template, request, jsonify
from phishshield import PhishShield

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    url = request.form.get('url')
    return jsonify(PhishShield().analyze_url(url))

if __name__ == "__main__":
    app.run(debug=True)

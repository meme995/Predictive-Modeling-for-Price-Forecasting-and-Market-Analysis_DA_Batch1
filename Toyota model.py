from flask import Flask, request, jsonify
from joblib import load
import numpy as np

app = Flask(__name__)


model = load("my_model.joblib")

@app.route('/predict', methods=['POST'])
def predict():
    """
    Endpoint to predict Toyota prices.
    Expects JSON input with feature values.
    """

    data = request.get_json()
    if not data or 'features' not in data:
        return jsonify({"error": "Missing 'features' key in request"}), 400

    try:

        features = np.array(data['features']).reshape(1, -1)
    except Exception as e:
        return jsonify({"error": f"Invalid input format: {str(e)}"}), 400

    try:

        prediction = model.predict(features)[0]
    except Exception as e:
        return jsonify({"error": f"Prediction failed: {str(e)}"}), 500


    return jsonify({"prediction": prediction})

@app.route('/', methods=['GET'])
def get_items():
    return jsonify({"name":"mona"})

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask,request,jsonify
from app import predict as model_predict
import traceback

app = Flask(__name__)

@app.route('/', methods=['POST'])
def predict():
    try:
        request_data = request.get_json()
        if not request_data or 'text' not in request_data or not isinstance(request_data['text'], str) or not request_data['text'].strip():
            return jsonify({'error': 'Invalid input'}), 400
        
        text = request_data['text'].strip()
        prediction = model_predict(text)
        return jsonify({'prediction': int(prediction), 'message': 'Spam' if prediction == 1 else 'Ham'}), 200 

    except Exception as e:
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

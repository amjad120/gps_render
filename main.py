from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

latest_data = {}

@app.route('/latest-position', methods=['POST'])
def receive_position():
    global latest_data
    data = request.get_json()

    latest_data = {
        'latitude': data.get('latitude'),
        'longitude': data.get('longitude'),
        'speed': data.get('speed', 0.0),
        'timestamp': datetime.utcnow().isoformat()
    }
    return jsonify({'status': 'ok'}), 200

@app.route('/latest-position', methods=['GET'])
def get_position():
    if not latest_data:
        return jsonify({'error': 'No data yet'}), 404
    return jsonify(latest_data), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)

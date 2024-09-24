from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def handle_post():
    data = request.get_json()
    if not data or 'data' not in data:
        return jsonify({'success': False, 'message': 'Invalid request.'}), 400

    qr_data = data['data']

    # Aqui você colocaria a lógica para processar o QR code
    if qr_data.startswith("OF"):
        result = "OF logic executed"
    elif qr_data.startswith("CI"):
        result = "CI logic executed"
    else:
        result = "Unknown document type"

    return jsonify({'success': True, 'message': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        # Renderiza o arquivo HTML na rota '/'
        return render_template('index.html')
    
    if request.method == 'POST':
        # Lida com a requisição POST (o QR Code escaneado)
        data = request.get_json()
        qr_data = data.get('data')
        ano_atual = datetime.now().year
        
        # Lógica similar à que você tinha no Google App Script
        resultado = {}
        if qr_data.startswith("OF"):
            num_oficio = qr_data.split(" ")[1]
            termo_busca = f"{num_oficio}/SAJ/{ano_atual}"
            resultado = {'success': True, 'message': f"Atualização feita com sucesso para {termo_busca}."}
        elif qr_data.startswith("CI"):
            num_ci = qr_data.split(" ")[1]
            termo_busca = f"CI {num_ci}-SAJ-{ano_atual}"
            resultado = {'success': True, 'message': f"Atualização feita com sucesso para {termo_busca}."}
        else:
            resultado = {'success': False, 'message': "Tipo de documento não reconhecido."}
        
        return jsonify(resultado)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, jsonify
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from flask_cors import CORS

app = Flask(__name__)

# Permitir CORS de qualquer origem
CORS(app)

# Configurações de autenticação para acessar a planilha Google
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('copia-arquivos-para-o-gdrive-9d3fd7c778f6.json', scope)  # Substitua pelo caminho do seu arquivo JSON
client = gspread.authorize(creds)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    
    if request.method == 'POST':
        data = request.get_json()
        qr_data = data.get('data')
        ano_atual = datetime.now().year
        
        spreadsheet = client.open_by_key('16_zlC5bRdyGTqFcVFvRIBCYzP-fjoPN9i64tD5DGe5c')  # ID da planilha
        worksheet = spreadsheet.worksheet('Atual')  # Nome da aba

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
    app.run(debug=False)

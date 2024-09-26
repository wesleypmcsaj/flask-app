from flask import Flask, render_template, request, jsonify
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from flask_cors import CORS
import os  # Importando a biblioteca os para acessar variáveis de ambiente

app = Flask(__name__)

# Permitir CORS de qualquer origem
CORS(app)

# Configurações de autenticação para acessar a planilha Google
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# A chave de API deve ser lida a partir de uma variável de ambiente
google_api_key = os.getenv('GOOGLE_API_KEY')  # Obtendo a chave da variável de ambiente

# Se a chave de API for necessária para a autenticação,
# você deve garantir que ela seja usada corretamente aqui.
# Caso você ainda precise do arquivo JSON para credenciais,
# ele deverá estar presente no seu repositório ou no ambiente onde o app é executado.
creds = ServiceAccountCredentials.from_json_keyfile_name('copia-arquivos-para-o-gdrive-9d3fd7c778f6.json', scope)  # Substitua pelo caminho do seu arquivo JSON
client = gspread.authorize(creds)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    if request.method == 'POST':
        try:
            data = request.get_json()
            qr_data = data.get('data')
            ano_atual = datetime.now().year

            spreadsheet = client.open_by_key('16_zlC5bRdyGTqFcVFvRIBCYzP-fjoPN9i64tD5DGe5c')  # ID da planilha
            worksheet = spreadsheet.worksheet('Atual')  # Nome da aba

            resultado = {}
            if qr_data.startswith("OF"):
                num_oficio = qr_data.split(" ")[1]
                termo_busca = f"{num_oficio}/SAJ/{ano_atual}"

                # Buscar o termo na coluna A
                cell = worksheet.find(termo_busca, in_column=1)  # Coluna A é a 1ª
                if cell:
                    linha = cell.row
                    worksheet.update_cell(linha, 6, datetime.now())  # Atualiza data na coluna 6
                    worksheet.update_cell(linha, 14, "CX Aguardando protocolo")  # Atualiza status na coluna 14
                    resultado = {'success': True, 'message': "Atualização feita com sucesso."}
                else:
                    resultado = {'success': False, 'message': "Documento não encontrado."}

            elif qr_data.startswith("CI"):
                num_ci = qr_data.split(" ")[1]
                termo_busca = f"CI {num_ci}-SAJ-{ano_atual}"

                # Buscar o termo na coluna O
                cell = worksheet.find(termo_busca, in_column=15)  # Coluna O é a 15ª
                if cell:
                    linha = cell.row
                    worksheet.update_cell(linha, 6, datetime.now())  # Atualiza data na coluna 6
                    worksheet.update_cell(linha, 14, "CX aguardando resposta")  # Atualiza status na coluna 14
                    resultado = {'success': True, 'message': "Atualização feita com sucesso."}
                else:
                    resultado = {'success': False, 'message': "Documento não encontrado."}
            else:
                resultado = {'success': False, 'message': "Tipo de documento não reconhecido."}

            return jsonify(resultado)

        except Exception as e:
            return jsonify({'success': False, 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=False)

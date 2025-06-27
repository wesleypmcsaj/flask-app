# 🧾 QRCode Web App - Integração com Google Sheets

### 📄 Descrição (Português)

Este projeto é uma aplicação web originalmente desenvolvida com **Flask** que realiza a **leitura e atualização de dados em uma planilha do Google Sheets** com base nas informações extraídas de QR Codes.  
A aplicação recebe requisições via POST com dados de documentos escaneados (como "OF" ou "CI"), localiza a linha correspondente na planilha, atualiza a data de movimentação e o status do documento de forma automática.

> ⚠️ **Importante:** Esta aplicação foi funcional durante um período, mas foi **substituída por uma versão otimizada desenvolvida com Google Apps Script**, que roda diretamente na nuvem 24 horas por dia, 7 dias por semana. Essa nova abordagem eliminou a necessidade de manter o código Flask rodando localmente ou em servidores externos.

Funcionalidades principais da versão Flask:
- Integração com Google Sheets usando autenticação via `service account`.
- Processamento de dados extraídos de QR Codes.
- Atualização de colunas específicas da planilha conforme o tipo do documento (OF ou CI).
- Suporte a CORS para acesso via front-end externo.
- Preparada para deploy em serviços como Render, Railway ou Heroku, usando variáveis de ambiente.

---

# 🧾 QRCode Web App - Integration with Google Sheets

### 📄 Description (English)

This project is a web application originally developed using **Flask**, designed to **read and update data in a Google Sheets spreadsheet** based on information extracted from QR Codes.  
It receives POST requests with scanned document data (e.g., "OF" or "CI"), finds the corresponding row in the sheet, and automatically updates the timestamp and document status.

> ⚠️ **Note:** This Flask application was functional for a period, but has since been **replaced by an improved version written in Google Apps Script**, which runs 24/7 in the cloud. This eliminates the need to keep the Flask server running locally or on external platforms.

Key features of the Flask version:
- Integration with Google Sheets using `service account` authentication.
- QR Code data parsing and processing.
- Dynamic updating of specific spreadsheet columns based on the document type (OF or CI).
- CORS support for external front-end access.
- Ready for deployment on platforms like Render, Railway, or Heroku using environment variables.

---

### 🔗 Nova versão / New version

Você pode acessar a versão mais recente do projeto, feita em Google Apps Script e hospedada na nuvem, no link abaixo:

👉 [https://github.com/wesleypmcsaj/QRCode_web_app/deployments](https://github.com/wesleypmcsaj/QRCode_web_app/deployments)




### 🔗 New version

You can access the latest version of the project, built with Google Apps Script and hosted in the cloud, at the link below:

👉 [https://github.com/wesleypmcsaj/QRCode_web_app/deployments](https://github.com/wesleypmcsaj/QRCode_web_app/deployments)

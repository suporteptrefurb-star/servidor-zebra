import requests
from flask import Flask, request

app = Flask(__name__)

LOCAL_SERVER = "http://SEU_IP_LOCAL:5000/imprimir"

@app.route('/imprimir', methods=['POST'])
def imprimir():
    zpl = request.get_data(as_text=True)
    try:
        response = requests.post(LOCAL_SERVER, data=zpl)
        return response.text, response.status_code
    except Exception as e:
        return f"Erro ao redirecionar: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

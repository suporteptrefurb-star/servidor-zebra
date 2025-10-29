import socket
from flask import Flask, request

app = Flask(__name__)

ZEBRA_IP = "192.168.1.103"  # IP da impressora Zebra na tua rede
ZEBRA_PORT = 9100

@app.route('/imprimir', methods=['POST'])
def imprimir():
    zpl = request.get_data(as_text=True)
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as zebra:
            zebra.connect((ZEBRA_IP, ZEBRA_PORT))
            zebra.sendall(zpl.encode('utf-8'))
        return "Etiqueta enviada com sucesso!", 200
    except Exception as e:
        return f"Erro ao enviar etiqueta: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

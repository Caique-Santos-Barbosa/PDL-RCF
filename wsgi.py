"""
Arquivo WSGI para produção no Render
"""
import os
import sys

# Adicionar o diretório do projeto ao path
sys.path.insert(0, os.path.dirname(__file__))

# Importar a aplicação Flask
from app import app, socketio

# Configurações para produção
if __name__ == "__main__":
    # Para desenvolvimento local
    socketio.run(app, host='0.0.0.0', port=int(os.environ.get('PORT', 10000)), debug=False)
else:
    # Para produção (Gunicorn)
    application = app 
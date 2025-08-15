"""
Configurações específicas para o ambiente Render
"""
import os

# Configurações do Render
RENDER_MODE = os.environ.get('RENDER') is not None

# Configurações de porta para Render
if RENDER_MODE:
    # No Render, usar a porta definida pelo ambiente
    DEFAULT_PORT = int(os.environ.get('PORT', 10000))
    DEFAULT_HOST = '0.0.0.0'
    
    # Configurações de produção para Render
    DEBUG_MODE = False
    
    # Configurações de upload para Render
    MAX_CONTENT_LENGTH = 50 * 1024 * 1024  # 50MB (limite do Render free)
    
    # Configurações de caminhos para Render
    UPLOAD_FOLDER = '/opt/render/project/src/static/videos'
    USERS_FOLDER = '/opt/render/project/src/static/users'
    
    # Criar diretórios necessários
    for folder in [UPLOAD_FOLDER, USERS_FOLDER, '/opt/render/project/src/static/known_faces', '/opt/render/project/src/static/css']:
        if not os.path.exists(folder):
            os.makedirs(folder, exist_ok=True)
else:
    # Configurações locais (não Render)
    DEFAULT_PORT = 5000
    DEFAULT_HOST = '0.0.0.0'
    DEBUG_MODE = True
    MAX_CONTENT_LENGTH = 500 * 1024 * 1024  # 500MB
    UPLOAD_FOLDER = 'static/videos'
    USERS_FOLDER = 'static/users'

# Configurações de segurança para Render
if RENDER_MODE:
    # No Render, usar chave secreta gerada automaticamente
    SECRET_KEY = os.environ.get('SECRET_KEY', 'render_secret_key_2024')
    
    # Desabilitar algumas funcionalidades que podem não funcionar no Render
    DISABLE_PORT_CONTROL = True  # Controle de porta física
    DISABLE_CAMERA = True  # Câmera física
else:
    SECRET_KEY = 'Gds2024aa@@_PainelFacial_2024_!@#_Un1c0_S3gr3d0'
    DISABLE_PORT_CONTROL = False
    DISABLE_CAMERA = False

# Configurações de logging
LOG_LEVEL = 'INFO' if RENDER_MODE else 'DEBUG'

# Configurações de banco de dados (para futuras implementações)
if RENDER_MODE:
    DATABASE_URL = os.environ.get('DATABASE_URL', None)
else:
    DATABASE_URL = None

# Configurações específicas para face_recognition no Render
try:
    import face_recognition
    FACE_RECOGNITION_AVAILABLE = True
    print("✅ face_recognition carregado com sucesso")
except ImportError:
    FACE_RECOGNITION_AVAILABLE = False
    print("⚠️ face_recognition não disponível - usando modo simulação") 
"""
Configurações específicas para o ambiente Replit
"""
import os

# Configurações do Replit
REPLIT_MODE = os.environ.get('REPL_ID') is not None

# Configurações de porta para Replit
if REPLIT_MODE:
    # No Replit, usar a porta padrão ou a porta definida pelo ambiente
    DEFAULT_PORT = int(os.environ.get('PORT', 5000))
    DEFAULT_HOST = '0.0.0.0'
    
    # Configurações de debug para Replit
    DEBUG_MODE = True
    
    # Configurações de upload para Replit
    MAX_CONTENT_LENGTH = 100 * 1024 * 1024  # 100MB (menor que o original)
    
    # Configurações de caminhos para Replit - usar caminhos relativos
    UPLOAD_FOLDER = 'static/videos'
    USERS_FOLDER = 'static/users'
    
    # Criar diretórios necessários
    for folder in [UPLOAD_FOLDER, USERS_FOLDER, 'static/known_faces', 'static/css']:
        if not os.path.exists(folder):
            os.makedirs(folder, exist_ok=True)
else:
    # Configurações locais (não Replit)
    DEFAULT_PORT = 5000
    DEFAULT_HOST = '0.0.0.0'
    DEBUG_MODE = True
    MAX_CONTENT_LENGTH = 500 * 1024 * 1024  # 500MB
    UPLOAD_FOLDER = 'static/videos'
    USERS_FOLDER = 'static/users'

# Configurações de segurança para Replit
if REPLIT_MODE:
    # No Replit, usar uma chave secreta mais simples
    SECRET_KEY = 'replit_secret_key_2024'
    
    # Desabilitar algumas funcionalidades que podem não funcionar no Replit
    DISABLE_PORT_CONTROL = True  # Controle de porta física
    DISABLE_CAMERA = True  # Câmera física
else:
    SECRET_KEY = 'Gds2024aa@@_PainelFacial_2024_!@#_Un1c0_S3gr3d0'
    DISABLE_PORT_CONTROL = False
    DISABLE_CAMERA = False

# Configurações de logging
LOG_LEVEL = 'INFO' if REPLIT_MODE else 'DEBUG' 
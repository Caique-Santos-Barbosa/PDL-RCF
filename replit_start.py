#!/usr/bin/env python3
"""
Script de inicialização para o Replit
Verifica dependências e configura o ambiente
"""

import os
import sys
import subprocess
import importlib

def check_dependencies():
    """Verifica se todas as dependências estão instaladas"""
    required_packages = [
        'flask',
        'flask_socketio',
        'opencv-python',
        'face_recognition',
        'numpy',
        'PIL',
        'requests',
        'werkzeug'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            if package == 'PIL':
                importlib.import_module('PIL')
            elif package == 'opencv-python':
                importlib.import_module('cv2')
            elif package == 'face_recognition':
                importlib.import_module('face_recognition')
            else:
                importlib.import_module(package.replace('-', '_'))
            print(f"✅ {package} - OK")
        except ImportError:
            print(f"❌ {package} - FALTANDO")
            missing_packages.append(package)
    
    return missing_packages

def install_missing_packages(packages):
    """Instala pacotes faltantes"""
    if not packages:
        return True
    
    print(f"\nInstalando {len(packages)} pacotes faltantes...")
    
    for package in packages:
        try:
            print(f"Instalando {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"✅ {package} instalado com sucesso")
        except subprocess.CalledProcessError:
            print(f"❌ Erro ao instalar {package}")
            return False
    
    return True

def create_directories():
    """Cria diretórios necessários"""
    directories = [
        'static/videos',
        'static/users',
        'static/known_faces',
        'static/css',
        'templates'
    ]
    
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)
            print(f"📁 Criado diretório: {directory}")

def check_replit_environment():
    """Verifica se está rodando no Replit"""
    is_replit = os.environ.get('REPL_ID') is not None
    if is_replit:
        print("🌐 Ambiente Replit detectado")
        print(f"   REPL_ID: {os.environ.get('REPL_ID')}")
        print(f"   REPL_SLUG: {os.environ.get('REPL_SLUG')}")
        print(f"   PORT: {os.environ.get('PORT', '5000')}")
    else:
        print("💻 Ambiente local detectado")
    
    return is_replit

def main():
    """Função principal"""
    print("🚀 Inicializando Porta Facial V1 para Replit")
    print("=" * 50)
    
    # Verificar ambiente
    is_replit = check_replit_environment()
    
    # Criar diretórios
    print("\n📁 Verificando estrutura de diretórios...")
    create_directories()
    
    # Verificar dependências
    print("\n📦 Verificando dependências...")
    missing_packages = check_dependencies()
    
    if missing_packages:
        print(f"\n⚠️  {len(missing_packages)} dependências faltando")
        if is_replit:
            print("Tentando instalar automaticamente...")
            if not install_missing_packages(missing_packages):
                print("❌ Erro ao instalar dependências")
                print("Execute manualmente: pip install -r requirements.txt")
                return False
        else:
            print("Execute: pip install -r requirements.txt")
            return False
    else:
        print("\n✅ Todas as dependências estão instaladas")
    
    # Verificar arquivos essenciais
    essential_files = ['app.py', 'replit_config.py']
    missing_files = []
    
    for file in essential_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print(f"\n❌ Arquivos essenciais faltando: {missing_files}")
        return False
    
    print("\n✅ Verificação concluída com sucesso!")
    print("\n🎯 Para iniciar o servidor:")
    print("   python app.py")
    
    return True

if __name__ == "__main__":
    success = main()
    if not success:
        sys.exit(1) 
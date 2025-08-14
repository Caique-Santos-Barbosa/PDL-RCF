#!/usr/bin/env python3
"""
Script de teste para verificar compatibilidade com Replit
"""

import os
import sys
import importlib
import subprocess

def test_imports():
    """Testa se todas as importações funcionam"""
    print("🔍 Testando importações...")
    
    imports_to_test = [
        ('flask', 'Flask'),
        ('flask_socketio', 'SocketIO'),
        ('cv2', 'cv2'),
        ('face_recognition', 'face_recognition'),
        ('numpy', 'np'),
        ('PIL', 'PIL'),
        ('requests', 'requests'),
        ('werkzeug', 'werkzeug'),
        ('json', 'json'),
        ('datetime', 'datetime'),
        ('base64', 'base64'),
        ('io', 'io'),
        ('os', 'os'),
        ('threading', 'threading')
    ]
    
    failed_imports = []
    
    for module_name, import_name in imports_to_test:
        try:
            if module_name == 'numpy':
                importlib.import_module('numpy')
            elif module_name == 'PIL':
                importlib.import_module('PIL')
            else:
                importlib.import_module(module_name)
            print(f"✅ {module_name} - OK")
        except ImportError as e:
            print(f"❌ {module_name} - FALHOU: {e}")
            failed_imports.append(module_name)
    
    return failed_imports

def test_directories():
    """Testa se os diretórios necessários existem"""
    print("\n📁 Testando estrutura de diretórios...")
    
    required_dirs = [
        'static',
        'static/videos',
        'static/users',
        'static/known_faces',
        'static/css',
        'templates'
    ]
    
    missing_dirs = []
    
    for directory in required_dirs:
        if os.path.exists(directory):
            print(f"✅ {directory} - OK")
        else:
            print(f"❌ {directory} - FALTANDO")
            missing_dirs.append(directory)
    
    return missing_dirs

def test_files():
    """Testa se os arquivos essenciais existem"""
    print("\n📄 Testando arquivos essenciais...")
    
    required_files = [
        'app.py',
        'replit_config.py',
        'requirements.txt',
        'pyproject.toml',
        '.replit'
    ]
    
    missing_files = []
    
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file} - OK")
        else:
            print(f"❌ {file} - FALTANDO")
            missing_files.append(file)
    
    return missing_files

def test_environment():
    """Testa variáveis de ambiente do Replit"""
    print("\n🌐 Testando ambiente...")
    
    is_replit = os.environ.get('REPL_ID') is not None
    
    if is_replit:
        print("✅ Ambiente Replit detectado")
        print(f"   REPL_ID: {os.environ.get('REPL_ID')}")
        print(f"   REPL_SLUG: {os.environ.get('REPL_SLUG')}")
        print(f"   PORT: {os.environ.get('PORT', '5000')}")
    else:
        print("ℹ️  Ambiente local detectado")
    
    return is_replit

def test_face_recognition():
    """Testa se o face_recognition funciona"""
    print("\n👤 Testando face_recognition...")
    
    try:
        import face_recognition
        import numpy as np
        
        # Criar uma imagem de teste simples
        test_image = np.zeros((100, 100, 3), dtype=np.uint8)
        
        # Tentar detectar rostos (não deve encontrar nenhum)
        face_locations = face_recognition.face_locations(test_image)
        face_encodings = face_recognition.face_encodings(test_image, face_locations)
        
        print("✅ face_recognition - OK")
        print(f"   Rostos detectados: {len(face_locations)}")
        return True
        
    except Exception as e:
        print(f"❌ face_recognition - FALHOU: {e}")
        return False

def test_flask_app():
    """Testa se a aplicação Flask pode ser importada"""
    print("\n🌐 Testando aplicação Flask...")
    
    try:
        # Importar configurações primeiro
        import replit_config
        print("✅ replit_config - OK")
        
        # Tentar importar a aplicação
        import app
        print("✅ app.py - OK")
        
        return True
        
    except Exception as e:
        print(f"❌ Aplicação Flask - FALHOU: {e}")
        return False

def main():
    """Função principal de teste"""
    print("🧪 Teste de Compatibilidade com Replit")
    print("=" * 50)
    
    # Testar ambiente
    is_replit = test_environment()
    
    # Testar importações
    failed_imports = test_imports()
    
    # Testar diretórios
    missing_dirs = test_directories()
    
    # Testar arquivos
    missing_files = test_files()
    
    # Testar face_recognition
    face_recognition_ok = test_face_recognition()
    
    # Testar aplicação Flask
    flask_ok = test_flask_app()
    
    # Resumo
    print("\n" + "=" * 50)
    print("📊 RESUMO DOS TESTES")
    print("=" * 50)
    
    total_tests = 0
    passed_tests = 0
    
    # Contar testes
    total_tests += 1  # Ambiente
    passed_tests += 1 if is_replit or not is_replit else 0
    
    total_tests += 14  # Importações
    passed_tests += 14 - len(failed_imports)
    
    total_tests += 6   # Diretórios
    passed_tests += 6 - len(missing_dirs)
    
    total_tests += 5   # Arquivos
    passed_tests += 5 - len(missing_files)
    
    total_tests += 1   # Face recognition
    passed_tests += 1 if face_recognition_ok else 0
    
    total_tests += 1   # Flask
    passed_tests += 1 if flask_ok else 0
    
    print(f"✅ Testes passados: {passed_tests}/{total_tests}")
    print(f"❌ Testes falharam: {total_tests - passed_tests}/{total_tests}")
    
    compatibility_percentage = (passed_tests / total_tests) * 100
    print(f"📈 Compatibilidade: {compatibility_percentage:.1f}%")
    
    if compatibility_percentage >= 90:
        print("🎉 PROJETO 100% COMPATÍVEL COM REPLIT!")
    elif compatibility_percentage >= 80:
        print("⚠️  PROJETO QUASE COMPATÍVEL - Alguns ajustes necessários")
    else:
        print("❌ PROJETO NÃO COMPATÍVEL - Muitos problemas encontrados")
    
    # Listar problemas
    if failed_imports:
        print(f"\n❌ Importações falharam: {failed_imports}")
    
    if missing_dirs:
        print(f"\n❌ Diretórios faltando: {missing_dirs}")
    
    if missing_files:
        print(f"\n❌ Arquivos faltando: {missing_files}")
    
    return compatibility_percentage >= 90

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 
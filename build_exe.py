#!/usr/bin/env python3
"""
Script para compilar o abrir_porta.py em um executável
"""

import subprocess
import sys
import os

def build_executable():
    """Compila o abrir_porta.py em um executável"""
    
    print("=== Compilando abrir_porta.exe ===")
    
    # Verificar se PyInstaller está instalado
    try:
        import PyInstaller
        print("✓ PyInstaller encontrado")
    except ImportError:
        print("✗ PyInstaller não encontrado. Instalando...")
        subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"])
    
    # Comando para compilar
    cmd = [
        "pyinstaller",
        "--onefile",                    # Criar um único arquivo executável
        "--windowed",                   # Não mostrar console
        "--name=abrir_porta",           # Nome do executável
        "--icon=static/logo.ico",       # Ícone (se existir)
        "--add-data=README_abrir_porta.txt;.",  # Incluir README
        "abrir_porta.py"
    ]
    
    print("Executando comando:", " ".join(cmd))
    
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print("✓ Compilação bem-sucedida!")
        print("Executável criado em: dist/abrir_porta.exe")
        
        # Copiar para a pasta raiz
        if os.path.exists("dist/abrir_porta.exe"):
            import shutil
            shutil.copy("dist/abrir_porta.exe", "abrir_porta_new.exe")
            print("✓ Executável copiado como: abrir_porta_new.exe")
            
    except subprocess.CalledProcessError as e:
        print(f"✗ Erro na compilação: {e}")
        print("Saída de erro:", e.stderr)
    except Exception as e:
        print(f"✗ Erro inesperado: {e}")

if __name__ == "__main__":
    build_executable() 
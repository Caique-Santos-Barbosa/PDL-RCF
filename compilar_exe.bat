@echo off
echo ========================================
echo    Compilando abrir_porta.exe
echo ========================================
echo.

echo Instalando dependencias...
pip install pyinstaller requests urllib3

echo.
echo Compilando executavel...
pyinstaller --onefile --windowed --name=abrir_porta abrir_porta.py

echo.
echo Copiando executavel...
copy dist\abrir_porta.exe abrir_porta_new.exe

echo.
echo ========================================
echo    Compilacao concluida!
echo    Novo executavel: abrir_porta_new.exe
echo ========================================
pause 
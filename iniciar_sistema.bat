@echo off
title SGF_CORE - Backend Municipal
echo [SGI] Iniciando Sistema de Gestion de Infracciones...

:: 1. Verificar si existe el entorno virtual
if not exist "venv\Scripts\activate.bat" (
    echo [ERROR] No se encuentra el entorno virtual (venv).
    echo Asegurate de haber ejecutado 'python -m venv venv' y 'pip install -r requirements.txt'
    pause
    exit /b
)

:: 2. Activar entorno virtual
call venv\Scripts\activate

:: 3. Abrir automáticamente el navegador en la documentación
echo [SGI] Abriendo interfaz en el navegador...
start http://127.0.0.1:8000/docs

:: 4. Lanzar el servidor
echo [SGI] Servidor iniciado. No cierres esta ventana.
uvicorn app.main:app --reload

pause
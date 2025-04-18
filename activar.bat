@echo off
REM — Crear entorno (si no existe) —
if not exist "venv" (
    python -m venv venv
)

REM — Activar el entorno virtual —
call venv\Scripts\activate.bat

REM — Actualizar pip e instalar dependencias —
python -m pip install --upgrade pip
if exist "requirements.txt" (
    pip install -r requirements.txt
) else (
    echo No se ha encontrado requirements.txt
)

echo.
echo Entorno virtual listo y dependencias instaladas.
pause

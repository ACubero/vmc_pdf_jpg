@echo off
REM =============================================
REM  Script para limpiar carpetas csv y jpgs
REM =============================================

REM Comprobar y eliminar archivos en la carpeta csv
if exist "csv\*.*" (
    echo Eliminando contenido de carpeta csv...
    del /Q "csv\*.*"
) else (
    echo La carpeta csv está vacía o no existe.
)

REM Comprobar y eliminar archivos en la carpeta jpgs
if exist "jpgs\*.*" (
    echo Eliminando contenido de carpeta jpgs...
    del /Q "jpgs\*.*"
) else (
    echo La carpeta jpgs está vacía o no existe.
)

echo Limpieza completada.
pause


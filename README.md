<!-- README.md -->

# Asignaciones Reunión Vida y Ministerio

Este repositorio contiene un script en Python (`process_assignments.py`) para procesar ficheros PDF de asignaciones mensuales de la reunión **Vida y Ministerio Cristianos**. Por cada página del PDF:

- Se genera una imagen JPG en `jpgs/`, nombrada como `n_página_nombre.jpg`.  
- Se crea un fichero CSV en `csv/`, con un mensaje personalizado para la persona asignada, con la fecha entre **asteriscos dobles**.

## Estructura de directorios

```plain
/ pdf/                 # Colocar aquí los archivos PDF de entrada
/ jpgs/                # Salida: imágenes JPG generadas
/ csv/                 # Salida: ficheros CSV generados
process_assignments.py
cleanup.bat
requirements.txt
README.md
.gitignore

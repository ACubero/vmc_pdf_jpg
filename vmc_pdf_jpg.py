# process_assignments.py

import fitz  # PyMuPDF
import os
import re

# Configuración de rutas
directorio_pdf = 'pdf'
directorio_jpg = 'jpgs'
directorio_csv = 'csv'

# Crear carpetas si no existen
def ensure_dirs():
    for d in (directorio_pdf, directorio_jpg, directorio_csv):
        os.makedirs(d, exist_ok=True)

# Limpiar carpetas jpgs y csv antes de procesar
def limpiar_carpetas():
    for carpeta in (directorio_jpg, directorio_csv):
        if os.path.isdir(carpeta):
            for nombre in os.listdir(carpeta):
                ruta = os.path.join(carpeta, nombre)
                if os.path.isfile(ruta):
                    os.remove(ruta)

# Función principal
def procesar_pdfs():
    ensure_dirs()
    limpiar_carpetas()

    for archivo in os.listdir(directorio_pdf):
        if not archivo.lower().endswith('.pdf'):
            continue
        nombre_base = os.path.splitext(archivo)[0]
        ruta_pdf = os.path.join(directorio_pdf, archivo)
        doc = fitz.open(ruta_pdf)
        mensajes = []

        for idx in range(len(doc)):
            pagina = doc.load_page(idx)
            texto = pagina.get_text("text")
            lines = texto.splitlines()
            nombre = None
            fecha = None
            prev_line = ''

            # Extraer nombre
            for ln in lines:
                if 'Nombre:' in ln:
                    parte = ln.split('Nombre:')[0].strip()
                    nombre_completo = parte or prev_line.strip()
                    nombre = nombre_completo.split()[0]
                    break
                prev_line = ln

            # Extraer fecha
            for ln in lines:
                if 'Fecha:' in ln:
                    m = re.search(r"(\d{1,2}/\d{1,2}/\d{4})", ln)
                    if m:
                        fecha = m.group(1)
                    break
            if not fecha:
                m = re.search(r"(\d{1,2}/\d{1,2}/\d{4})", texto)
                fecha = m.group(1) if m else ''

            # Fallback nombre
            if not nombre:
                nombre = f"{nombre_base}_p{idx+1}"

            # Guardar JPG con nombre 'página_nombre'
            numero_pagina = idx + 1
            nombre_sanitizado = nombre.replace(' ', '_')
            nombre_jpg = f"{numero_pagina}_{nombre_sanitizado}.jpg"
            pix = pagina.get_pixmap(dpi=300)
            pix.save(os.path.join(directorio_jpg, nombre_jpg))

            # Componer mensaje
            mensaje = (
                f"Hola {nombre}, espero que te encuentres bien tú y los tuyos. "
                f"Te adjunto una asignación para el día **{fecha}**. "
                "Muchas gracias por tu preparación. Un saludo"
            )
            mensajes.append(mensaje)

        # Guardar CSV (solo mensajes, sin comillas) en UTF-8
        nombre_csv = f"{nombre_base}.csv"
        ruta_csv = os.path.join(directorio_csv, nombre_csv)
        with open(ruta_csv, 'w', encoding='utf-8') as f:
            for msg in mensajes:
                f.write(msg + '\n')

        print(f"Procesado {archivo}: {len(mensajes)} páginas -> {nombre_csv}")

if __name__ == '__main__':
    procesar_pdfs()

```markdown
# VMC PDF → JPG & CSV

Un sencillo proyecto en Python para automatizar el procesamiento de tus asignaciones mensuales de la reunión **Vida y Ministerio Cristianos**.  
Por cada página de cada PDF en `pdf/`:

1. Genera una imagen JPG en `jpgs/` nombrada como `número_página_nombre.jpg`.  
2. Crea un CSV en `csv/` con un mensaje personalizado para la persona asignada (la fecha va entre **dobles asteriscos**).

---

## 📁 Estructura de directorios

```text
/
├─ pdf/                   # PDFs de entrada
├─ jpgs/                  # Imágenes JPG generadas (salida)
├─ csv/                   # CSVs generados (salida)
├─ vmc_pdf_jpg.py         # Script principal
├─ cleanup.bat            # Limpia carpetas jpgs/ y csv/
├─ requirements.txt       # Dependencias Python
├─ README.md              # Este archivo
└─ .gitignore             # Archivos/carpetas ignorados por Git
```

---

## 🛠 Prerrequisitos

- Python 3.7+  
- Windows (o Linux/Mac con adaptación de `cleanup.bat` a `cleanup.sh`)  
- Paquete PyMuPDF  

---

## ⚙️ Instalación

1. **Clona este repositorio**  
   ```bash
   git clone <url-del-repositorio>
   cd <nombre-del-repositorio>
   ```

2. **Crea y activa un entorno virtual**  
   - Windows:
     ```bat
     python -m venv venv
     venv\Scripts\activate.bat
     ```
   - Linux / macOS:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Instala las dependencias**  
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

---

## 🚀 Uso

1. Coloca tus PDFs en la carpeta `pdf/`.  
2. Ejecuta el script principal:
   ```bash
   python vmc_pdf_jpg.py
   ```
   - Esto vaciará automáticamente `jpgs/` y `csv/` antes de generar los nuevos archivos.

3. Al finalizar, encontrarás:
   - Imágenes en `jpgs/` con nombres como `1_Daniel.jpg`, `2_Remedios.jpg`, etc.  
   - CSVs en `csv/` llamados `Mes2025.csv`, cada línea con:
     ```
     Hola Daniel, espero que te encuentres bien tú y los tuyos. Te adjunto una asignación para el día **05/06/2025**. Muchas gracias por tu preparación. Un saludo
     ```

---

## 🧹 Limpieza manual

Si necesitas limpiar las carpetas sin ejecutar el script:

- **Windows**:  
  ```bat
  cleanup.bat
  ```
- **Linux/macOS**:  
  ```bash
  rm -f jpgs/* csv/*
  ```

---

## 🤝 Contribuir

¡Contribuciones, sugerencias y pull requests son bienvenidos!  
1. Abre un _issue_ para discutir cambios grandes.  
2. Crea tu _branch_ (`git checkout -b feature/nueva-funcionalidad`).  
3. Realiza _commit_ de tus cambios (`git commit -m "Añade X"`).  
4. Haz _push_ a tu branch (`git push origin feature/nueva-funcionalidad`).  
5. Abre un _pull request_.

---

## 📄 Licencia

Este proyecto está bajo la **MIT License**. Consulta el fichero `LICENSE` para más detalles.
```
# Usa una imagen oficial de Python como base
FROM python:3.11-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Instala las dependencias del sistema primero (si son necesarias)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copia el archivo de requerimientos primero para aprovechar la caché de Docker
COPY requirements.txt .

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de los archivos de la aplicación
COPY src/ ./src/

# Expone el puerto que usa la aplicación (ej: Flask usa 5000 por defecto)
EXPOSE 7860

# Define la variable de entorno (ajusta según tu aplicación)
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Comando para ejecutar la aplicación
CMD ["python", "src/app.py"]
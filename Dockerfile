# Usa una imagen base de Python
FROM python:3.11.1

# Define el directorio de trabajo
WORKDIR /app

# Copia los archivos necesarios al contenedor
COPY . /app

# Actualiza el sistema e instala SQLite con la versión correcta
RUN apt-get update && \
    apt-get install -y sqlite3 libsqlite3-dev && \
    rm -rf /var/lib/apt/lists/*

# Instala las dependencias del proyecto
RUN pip install -r requirements.txt

# Expone el puerto en el que se ejecutará la aplicación
EXPOSE 8000

# Comando para ejecutar el servidor de Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# 1. Usamos una imagen ligera de Python 3.11
FROM python:3.11-slim

# 2. Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# 3. Copiamos solo el archivo de requerimientos primero (para aprovechar el caché de Docker)
COPY requirements.txt .

# 4. Instalamos las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiamos el resto de los archivos (app.py, .env, etc.)
COPY . .

# 6. Exponemos el puerto 8080 que definimos en la API
EXPOSE 8080

# 7. Comando para ejecutar la aplicación
CMD ["python", "app.py"]
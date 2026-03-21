<<<<<<< HEAD
# Imagen base de Python
FROM python:3.10-slim

# Directorio de trabajo
WORKDIR /app

# Copiar archivos
COPY . .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer puerto
EXPOSE 8080

# Comando para ejecutar la app
=======
# 1. Usamos una imagen de Python
FROM python:3.11-slim

# 2. Directorio de trabajo
WORKDIR /app

# 3. Copiamos archivo de requerimiento
COPY requirements.txt .

# 4. Instalamos las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiamos todos los archivos
COPY . .

# 6. Exponemos el puerto 8080
EXPOSE 8080

# 7. Comando para ejecutar la aplicación
>>>>>>> 93dae089beccf253fa659d3cfdb53fb5e3db388f
CMD ["python", "app.py"]

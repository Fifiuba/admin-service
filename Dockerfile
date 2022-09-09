FROM python:3

# Declaro mi directorio de trabajo
WORKDIR /usr/src/app

ENV PYTHONPATH=${PYTHONPATH}:${PWD} 

# Copio los archivos de poetry a /app
COPY  pyproject.toml ./
COPY  poetry.lock ./

# Corro los comandos para instalar poetry
RUN pip3 install poetry
# Este comando deshabilito crear el entorno virtual (ya que estoy con imagenes)
RUN poetry config virtualenvs.create false
# Este comando installa las dependencias que no son de dev y --no-root es para no copiar el proyecto
RUN poetry install --only main --no-root

# Creo una carpeta admin_service
RUN mkdir admin_service

# Copio todo lo de admin_service local a admin_service
COPY ./admin_service/ ./admin_service

# Expongo el puerto de la imagen en 8000
EXPOSE 8000

# Corro comando para levantar el servidor
CMD poetry run uvicorn admin_service.app:app --host 0.0.0.0
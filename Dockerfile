# Dockerfile para Porta Facial V1
FROM python:3.9-slim

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    cmake \
    pkg-config \
    libopencv-dev \
    libdlib-dev \
    libboost-all-dev \
    libeigen3-dev \
    gcc \
    g++ \
    make \
    git \
    && rm -rf /var/lib/apt/lists/*

# Definir diretório de trabalho
WORKDIR /app

# Copiar arquivos de dependências
COPY requirements.txt pyproject.toml ./

# Instalar dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código da aplicação
COPY . .

# Criar diretórios necessários
RUN mkdir -p static/videos static/users static/css templates

# Expor porta
EXPOSE 5000

# Comando para executar a aplicação
CMD ["python", "app.py"] 
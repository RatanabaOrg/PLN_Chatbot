# Use a imagem oficial do Python como base
FROM python:3.9-slim

# Defina o diretório de trabalho no container
WORKDIR /app

# Copie os arquivos de dependência para o container
COPY requirements.txt .

# Instale as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante dos arquivos para o container
COPY . .

# Exponha a porta onde o Flask será executado
EXPOSE 5000

# Defina o comando para iniciar o servidor Flask
CMD ["python", "app.py"]

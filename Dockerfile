FROM python:3.9-slim-buster

## cria workdir
WORKDIR /app

## copia os arquivos do diretório raíz para dentro do workdir
COPY . .

## instala as dependências
RUN pip install -r requiriments.txt

## coda aplicação na porta 8080
ENTRYPOINT [ "streamlit", "run", "main.py", "--server.port=8080", "server.address=0.0.0.0" ]
import os
import psycopg2
import boto3
from dotenv import load_dotenv

load_dotenv()

# Configurações do banco de dados
DB_HOST = os.getenv('DB_HOST')
DB_PORT = int(os.getenv('DB_PORT', 5432))
DB_NAME_INIT = os.getenv('DB_NAME_INIT')
DB_NAME_FINAL = os.getenv('DB_NAME_FINAL')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

# Configurações do S3
AWS_REGION = os.getenv('AWS_REGION')
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
BUCKET_NAME = os.getenv('BUCKET_NAME')
PREFIX = os.getenv('PREFIX', 'Imagens/')

# Criando o banco
try:
    con = psycopg2.connect(host=DB_HOST, port=DB_PORT, dbname=DB_NAME_INIT, user=DB_USER, password=DB_PASSWORD)
    con.autocommit = True
    cur = con.cursor()
    cur.execute(f'CREATE DATABASE {DB_NAME_FINAL};')
    con.close()
    print("Banco de dados criado com sucesso.")
except Exception as e:
    print("Erro ao criar banco:", e)

# Criando a tabela
try:
    con = psycopg2.connect(host=DB_HOST, port=DB_PORT, dbname=DB_NAME_FINAL, user=DB_USER, password=DB_PASSWORD)
    con.autocommit = True
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS arquivos (idarquivo INT, nomearquivo VARCHAR(256));')
    con.close()
    print("Tabela criada com sucesso.")
except Exception as e:
    print("Erro ao criar tabela:", e)

# Conectando ao S3
try:
    s3 = boto3.resource(
        service_name='s3',
        region_name=AWS_REGION,
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY
    )
    print("Conectado ao S3 com sucesso.")
except Exception as e:
    print("Erro ao conectar ao S3:", e)

# Inserindo arquivos no banco
try:
    con = psycopg2.connect(host=DB_HOST, port=DB_PORT, dbname=DB_NAME_FINAL, user=DB_USER, password=DB_PASSWORD)
    con.autocommit = True
    cur = con.cursor()

    id = 0
    for obj in s3.Bucket(BUCKET_NAME).objects.filter(Prefix=PREFIX):
        if obj.key.lower().endswith('.jpg'):
            filename = obj.key.split('/')[-1]
            id += 1
            print(f"Inserindo: {filename}")
            cur.execute("INSERT INTO arquivos (idarquivo, nomearquivo) VALUES (%s, %s)", (id, filename))

    con.close()
    print("Inserções concluídas com sucesso.")
except Exception as e:
    print("Erro ao inserir dados:", e)

# Consultando registros
try:
    con = psycopg2.connect(host=DB_HOST, port=DB_PORT, dbname=DB_NAME_FINAL, user=DB_USER, password=DB_PASSWORD)
    cur = con.cursor()
    cur.execute('SELECT * FROM arquivos;')
    for row in cur.fetchall():
        print(row)
    con.close()
except Exception as e:
    print("Erro ao consultar dados:", e)
# Integração S3 + PostgreSQL com Python

Projeto de integração entre um bucket S3 e um banco de dados PostgreSQL hospedado na AWS RDS. O script Python realiza a leitura de nomes de arquivos `.jpg` do bucket e insere essas informações em uma tabela no banco de dados.

---

## 🔧 Tecnologias Utilizadas

- Python 3
- [Boto3](https://boto3.amazonaws.com/) (SDK AWS)
- [psycopg2](https://www.psycopg.org/) (Driver PostgreSQL)
- [python-dotenv](https://pypi.org/project/python-dotenv/) (Variáveis de ambiente)
- AWS S3
- AWS RDS (PostgreSQL)

---

## ⚙️ Como executar

## 1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/banco-s3-postgres.git
cd banco-s3-postgres
```

---

## 2. Crie um ambiente virtual (opcional, mas eu recomendo):
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

---

## 3. Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## 4. Crie o arquivo .env com suas credenciais:

```DB_HOST=seu_host_rds
DB_PORT=5432
DB_NAME_INIT=postgres
DB_NAME_FINAL=inventario
DB_USER=seu_usuario
DB_PASSWORD=sua_senha

AWS_REGION=us-east-1
AWS_ACCESS_KEY_ID=sua_chave
AWS_SECRET_ACCESS_KEY=sua_chave_secreta
BUCKET_NAME=seu_bucket
PREFIX=Imagens/
```

---

## 5. Execute o script:

```bash
BancodeDadosRDS.py
```

---

## 6. Estrutura Geral:
```bash
banco-s3-postgres/
├── src/
│   └── BancodeDadosRDS.py
├── imgs/                 
├── .env                
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 7. Segurança(Importante):
Credenciais sensíveis são armazenadas em variáveis de ambiente (.env).

O arquivo .env está listado no .gitignore para evitar exposição pública.

Nunca compartilhe suas chaves de acesso (AWS ou banco de dados) em repositórios públicos.

---

## 8. Conclusão:
Este projeto foi desenvolvido com o objetivo de demonstrar, na prática, conhecimentos em integração de dados na nuvem, utilizando serviços da AWS (S3 e RDS) e Python. Ele mostra minha capacidade de trabalhar com automação de processos, manipulação de arquivos, acesso seguro a bancos de dados e boas práticas de versionamento com Git. É um exemplo real de como aplico conceitos de engenharia de dados em um cenário próximo ao ambiente de produção.

---


## 9. Licença:

Este projeto está licenciado sob a MIT License.

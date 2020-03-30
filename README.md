# Flask API

Escolhi utilizar Flask por se tratar de um framework que te da a liberdade de escolhas. Apesar de existirem bibliotecas externas 
consolidadas na comunidade, escolher algo que te traga garantia na sequencia do projeto é grande responsabilidade.
Procurei fazer um projeto o mais desacoplado possível utilizando uma estrutura onde usei Brueprints e o padrão Factory.


## Iniciando...
### Para executar este projeto, você precisa seguir as instruções abaixo.
---

## Clone

```bash
git clone git@github.com:gitfilipegoncalves/boleto_flex.git
```

## ou faça o download

https://github.com/gitfilipegoncalves/boleto_flex/archive/master.zip

ou

```bash
wget https://github.com/gitfilipegoncalves/boleto_flex/archive/master.zip
```

## Ambiente

Python 3.6+
Ative a sua virtualenv

```bash
pip install -r requirements.txt
```

## Executando

Entre na pasta do projeto (backend/app) e digite;

```bash
flask db init # rodar uma vez
flask db migrate # rodar uma vez
flask db upgrade # rodar uma vez
flask run
```

Acesse:

- Website: http://localhost:5000

- API GET:
  - https://localhost:5000/api/v1/customers/
  - https://localhost:5000/api/v1/customers/1
  - https://localhost:5000/api/v1/users/1
- API POST:
  - https://localhost:5000/api/v1/customers/1
  - https://localhost:5000/api/v1/register
  - https://localhost:5000/api/v1/login
  - https://localhost:5000/api/v1/logout
- API DELETE:
  - https://localhost:5000/api/v1/users/1


## Structure

```bash
.
├── app
│   ├── app.py
│   ├── bf.db
│   ├── ext
│   │   ├── auth.py
│   │   ├── database.py
│   │   └── __init__.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── alembic.ini
│   │   ├── env.py
│   │   ├── README
│   │   ├── script.py.mako
│   │   └── versions
│   │       ├── 2e837ee9a138_criação_de_user_para_autenticação.py
│   │       └── ea30b2f1c392_migração_inicial.py
│   ├── restapi
│   │   ├── customer
│   │   │   ├── __init__.py
│   │   │   ├── models.py
│   │   │   └── resources.py
│   │   ├── __init__.py
│   │   └── user
│   │       ├── __init__.py
│   │       ├── models.py
│   │       └── resources.py
│   └── tests
│       └── __init__.py
├── blacklist.py
├── config.py
└── requirements.txt

8 directories, 23 files
```

# SETUP.md

# CarWashSys

Guia de instalação e configuração do ambiente de desenvolvimento.

---

## Requisitos

- Python 3.13 ou superior
- Git
- Visual Studio Code
- Banco de dados (SQLite durante o desenvolvimento)

---

## Clonar o projeto

```bash
git clone <repositorio>
cd CarWashSys
```

---

## Criar ambiente virtual

```bash
python -m venv venv
```

---

## Ativar ambiente virtual

Windows

```bash
venv\Scripts\activate
```

Linux

```bash
source venv/bin/activate
```

---

## Instalar dependências

```bash
pip install -r requirements.txt
```

---

## Aplicar migrações

```bash
python manage.py makemigrations

python manage.py migrate
```

---

## Executar o servidor

```bash
python manage.py runserver
```

---

## Acessar

http://127.0.0.1:8000/
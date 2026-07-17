# COMANDOS.md

# Comandos úteis - CarWashSys

Este documento reúne os principais comandos utilizados durante o desenvolvimento do projeto.

---

# Ambiente Virtual

Criar

```bash
python -m venv venv
```

Ativar (Windows)

```bash
venv\Scripts\activate
```

Desativar

```bash
deactivate
```

---

# Instalar dependências

```bash
pip install -r requirements.txt
```

---

# Servidor

Executar

```bash
python manage.py runserver
```

Executar em outra porta

```bash
python manage.py runserver 8001
```

---

# Migrações

Criar migrações

```bash
python manage.py makemigrations
```

Aplicar migrações

```bash
python manage.py migrate
```

Mostrar migrações

```bash
python manage.py showmigrations
```

---

# Criar Apps

```bash
python manage.py startapp nome_app apps/nome_app
```

---

# Superusuário

```bash
python manage.py createsuperuser
```

---

# Coletar arquivos estáticos

```bash
python manage.py collectstatic
```

---

# Git

Verificar alterações

```bash
git status
```

Adicionar arquivos

```bash
git add .
```

Criar commit

```bash
git commit -m "mensagem"
```

Enviar para o GitHub

```bash
git push
```

Atualizar projeto

```bash
git pull
```

---

# Informações do projeto

Verificar erros

```bash
python manage.py check
```

Mostrar configurações

```bash
python manage.py diffsettings
```
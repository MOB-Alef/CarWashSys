# ROTINA_DE_DESENVOLVIMENTO

## Objetivo

Este documento descreve a rotina recomendada para desenvolver o CarWashSys.

Seguir esta sequência ajuda a manter o projeto organizado e reduz a chance de esquecer etapas importantes.

---

## Iniciando o trabalho

1. Abrir o Visual Studio Code.
2. Abrir a pasta do projeto.
3. Ativar o ambiente virtual.

Windows:

```bash
venv\Scripts\activate
```

Linux:

```bash
source venv/bin/activate
```

4. Verificar o status do Git.

```bash
git status
```

5. Atualizar o projeto (quando necessário).

```bash
git pull
```

6. Executar o servidor.

```bash
python manage.py runserver
```

---

## Durante o desenvolvimento

- Implementar apenas uma funcionalidade por vez.
- Testar cada alteração antes de continuar.
- Manter o padrão definido em `PADRAO_DO_PROJETO.md`.
- Atualizar a documentação quando necessário.

---

## Finalizando o trabalho

1. Executar os testes.
2. Verificar o status do Git.

```bash
git status
```

3. Adicionar os arquivos.

```bash
git add .
```

4. Criar o commit.

```bash
git commit -m "mensagem"
```

5. Enviar para o GitHub.

```bash
git push
```

6. Atualizar o CHANGELOG.
7. Atualizar o Diário de Desenvolvimento.
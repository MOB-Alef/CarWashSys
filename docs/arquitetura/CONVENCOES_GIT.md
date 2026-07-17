# CONVENCOES_GIT

## Objetivo

Este documento define o padrão de utilização do Git durante o desenvolvimento do CarWashSys.

O objetivo é manter um histórico organizado, facilitando a manutenção e o acompanhamento da evolução do projeto.

---

## Fluxo de Trabalho

Durante o desenvolvimento, recomenda-se seguir a seguinte sequência:

1. Verificar o status do projeto.

```bash
git status
```

2. Adicionar as alterações.

```bash
git add .
```

3. Criar um commit.

```bash
git commit -m "mensagem"
```

4. Enviar para o GitHub.

```bash
git push
```

---

## Padrão de Commits

Utilizar mensagens curtas e objetivas.

Exemplos:

- feat: cria módulo financeiro
- feat: adiciona CRUD de funcionários
- fix: corrige formulário de produtos
- docs: atualiza documentação
- refactor: reorganiza estrutura do projeto

---

## Boas práticas

- Realizar commits apenas após concluir uma funcionalidade.
- Evitar commits com alterações incompletas.
- Testar o sistema antes de enviar para o GitHub.
- Manter o histórico organizado e descritivo.
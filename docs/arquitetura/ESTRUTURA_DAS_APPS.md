# ESTRUTURA_DAS_APPS

## Objetivo

Este documento descreve a responsabilidade de cada aplicativo (app) do CarWashSys.

Cada módulo possui uma função específica e deve permanecer o mais independente possível, facilitando a manutenção e a expansão do sistema.

---

## accounts

Responsável pela autenticação dos usuários, login, logout e controle de acesso ao sistema.

---

## clientes

Gerencia o cadastro de clientes da empresa.

Exemplos:

- Cadastro
- Consulta
- Atualização
- Exclusão

---

## dashboard

Responsável pela tela inicial do sistema.

Apresentará informações resumidas como:

- Total de clientes
- Ordens de serviço
- Estoque
- Financeiro
- Indicadores gerais

---

## estoque

Controla os produtos utilizados pela empresa.

Exemplos:

- Cadastro de produtos
- Quantidade em estoque
- Fornecedores
- Controle de ativos

---

## financeiro

Responsável pelo controle financeiro.

Exemplos:

- Entradas
- Saídas
- Fluxo de caixa
- Relatórios financeiros (futuramente)

---

## funcionarios

Gerencia os colaboradores da empresa.

Exemplos:

- Cadastro
- Cargo
- Salário
- Situação

---

## ordens

Responsável pelas Ordens de Serviço (OS).

Será um dos principais módulos do sistema.

Nele serão registrados:

- Cliente
- Veículo
- Serviços realizados
- Produtos utilizados
- Valor
- Situação da lavagem

---

## veiculos

Gerencia os veículos cadastrados.

Exemplos:

- Marca
- Modelo
- Placa
- Ano
- Cliente proprietário

---

## Organização

Cada aplicativo deve conter, sempre que necessário:

- models.py
- forms.py
- views.py
- urls.py
- admin.py

Além disso, cada app possui sua própria pasta em `templates/`, mantendo a organização e a separação das responsabilidades.
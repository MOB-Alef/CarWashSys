# PADRAO_DO_PROJETO

## Objetivo

O CarWashSys foi desenvolvido seguindo uma arquitetura simples, organizada e de fácil manutenção.

O objetivo é permitir que qualquer desenvolvedor consiga compreender rapidamente a estrutura do sistema, mantendo um padrão único em todos os módulos.

Toda nova funcionalidade deverá seguir as convenções descritas neste documento.

---

## Estrutura de Pastas

O projeto está organizado da seguinte maneira:

```text
CarWashSys/
│
├── apps/
│   ├── accounts/
│   ├── clientes/
│   ├── dashboard/
│   ├── estoque/
│   ├── financeiro/
│   ├── funcionarios/
│   ├── ordens/
│   └── veiculos/
│
├── templates/
│
├── static/
│
├── media/
│
├── docs/
│   ├── arquitetura/
│   ├── banco_de_dados/
│   ├── diario/
│   ├── imagens/
│   ├── prototipos/
│   └── backup/
│
└── manage.py
```

Cada módulo possui sua própria responsabilidade e deve permanecer independente sempre que possível.

---

## Requisitos

Antes de executar o projeto, certifique-se de possuir instalado:

- Python 3.13 ou superior
- Git
- Visual Studio Code (recomendado)
- Ambiente Virtual (venv)
- pip atualizado

---

## Padrão dos Models

Todos os modelos do projeto devem seguir um padrão de organização para facilitar a manutenção e a leitura do código.

**Regras adotadas:**

- Um model por responsabilidade.
- Utilizar nomes em português.
- Utilizar `BigAutoField` como chave primária padrão.
- Declarar os campos em ordem lógica.
- Utilizar `choices` quando houver opções fixas.
- Implementar o método `__str__()` para facilitar a identificação dos registros.
- Evitar lógica de negócio complexa dentro dos models.

---

## Padrão dos Forms

Todos os formulários do CarWashSys deverão herdar de `forms.ModelForm`.

**Regras adotadas:**

- Utilizar uma classe Form para cada Model.
- Declarar a classe `Meta`.
- Utilizar `fields = "__all__"` quando todos os campos forem utilizados.
- Personalizar os widgets para manter a identidade visual do sistema.
- Utilizar classes do Bootstrap nos campos (`form-control`, `form-select`, `form-check-input`).
- Centralizar toda a configuração visual dos formulários no próprio arquivo `forms.py`.

---

## Padrão das Views

Todas as Views do projeto deverão seguir um padrão único de organização.

**Regras adotadas:**

- Importações sempre no início do arquivo.
- Uma função para cada operação (listar, criar, editar e excluir).
- Utilizar `get_object_or_404()` para localizar registros.
- Utilizar `redirect()` após salvar ou excluir um registro.
- Utilizar `render()` para retornar os templates.
- Organizar o contexto em um dicionário chamado `context`.
- Manter uma separação clara entre a lógica da View e a interface.

---

## Padrão das URLs

Cada aplicativo deve possuir seu próprio arquivo `urls.py`.

As rotas devem seguir um padrão de CRUD para manter consistência entre todos os módulos.

**Exemplo:**

- lista
- novo
- editar
- excluir

As URLs devem utilizar nomes claros e padronizados para facilitar o uso das tags `{% url %}` nos templates.

---

## Padrão dos Templates

Cada módulo possui sua própria pasta dentro de `templates/`.

**Exemplo:**

```text
templates/
├── estoque/
├── financeiro/
├── funcionarios/
```

Os templates seguem um padrão visual único utilizando Bootstrap.

Cada módulo normalmente possui:

- `lista.html`
- `formulario.html`
- `excluir.html`

Todos os templates devem herdar de `base.html`, garantindo uma interface consistente em todo o sistema.

---

## Padrão de Organização

Cada funcionalidade do sistema deverá ser criada em um módulo (app) próprio.

Cada módulo deve conter, sempre que necessário:

- `models.py`
- `forms.py`
- `views.py`
- `urls.py`
- `admin.py`

Além disso, cada módulo deverá possuir sua própria pasta dentro de `templates/`.

Sempre que possível, os módulos devem permanecer independentes, evitando dependências desnecessárias entre eles.

A organização do projeto prioriza simplicidade, manutenção e facilidade de expansão.

---

## Padrão dos Commits

Ao finalizar uma etapa importante do desenvolvimento, deve ser realizado um commit.

Sempre que possível, utilizar mensagens claras e objetivas.

**Exemplos:**

- `feat: cria módulo de estoque`
- `feat: adiciona CRUD de funcionários`
- `fix: corrige formulário de produtos`
- `docs: atualiza documentação`
- `refactor: reorganiza estrutura do projeto`

Após cada commit:

1. Verificar o `git status`;
2. Executar os testes necessários;
3. Enviar as alterações para o GitHub utilizando `git push`.

---

## Convenções Gerais

Durante o desenvolvimento do CarWashSys, devem ser seguidas as seguintes convenções:

- Utilizar nomes claros e descritivos para classes, funções e variáveis.
- Manter a indentação padronizada em quatro espaços.
- Evitar código duplicado sempre que possível.
- Comentar apenas quando realmente necessário.
- Organizar o código em pequenos blocos para facilitar a leitura.
- Testar cada funcionalidade antes de realizar um commit.
- Manter a documentação sempre atualizada conforme o projeto evoluir.

O principal objetivo é manter o sistema simples de entender, fácil de manter e preparado para futuras expansões.

---

## Clonando o Projeto

Para executar o CarWashSys em outro computador:

### 1. Clonar o repositório

```bash
git clone <URL_DO_REPOSITORIO>
```

### 2. Entrar na pasta do projeto

```bash
cd CarWashSys
```

### 3. Criar o ambiente virtual

```bash
python -m venv venv
```

### 4. Ativar o ambiente virtual

#### Windows

```bash
venv\Scripts\activate
```

#### Linux

```bash
source venv/bin/activate
```

### 5. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 6. Aplicar as migrações

```bash
python manage.py migrate
```

### 7. Executar o servidor

```bash
python manage.py runserver
```

---

## Considerações Finais

Este documento deverá ser atualizado sempre que um novo padrão de desenvolvimento for adotado.

O objetivo é manter o CarWashSys organizado, padronizado e preparado para crescer ao longo do tempo.
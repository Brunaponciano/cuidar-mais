# 💜 CUIDAR+

**Seu cuidado, organizado em um só lugar.**

O CUIDAR+ é um projeto desenvolvido em Python com o objetivo de organizar informações sobre medicamentos, registrar doses tomadas e acompanhar consultas.

O projeto surgiu da ideia de utilizar a tecnologia para facilitar a organização da rotina de cuidados com a saúde.

> 📚 **Status:** versão inicial funcional — projeto em desenvolvimento.

## 🎯 Objetivo

Desenvolver uma aplicação de linha de comando que permita organizar informações sobre medicamentos e consultas de maneira simples.

Este projeto tem finalidade educacional e não substitui orientações de profissionais de saúde.

## ✨ Funcionalidades

### 💊 Medicamentos
- Cadastrar medicamentos.
- Listar medicamentos cadastrados.
- Editar informações dos medicamentos.
- Excluir medicamentos.
- Registrar doses tomadas.
- Consultar o histórico de doses registradas.

### 🩺 Consultas
- Cadastrar consultas com nome, data, horário e local.
- Visualizar consultas cadastradas em ordem cronológica.

### 💾 Armazenamento de dados
- Salvar informações em arquivos JSON.
- Carregar os dados salvos quando o programa é iniciado.

## 🛠️ Tecnologias utilizadas

- **Python 3** — linguagem utilizada no desenvolvimento.
- **JSON** — formato utilizado para armazenar os dados localmente.
- **Git** — controle de versão.
- **GitHub** — hospedagem do código-fonte.

## ▶️ Como executar o projeto

### Pré-requisitos

- Python 3 instalado.
- Git instalado, caso queira clonar o repositório.

### 1. Clonar o repositório

```bash
git clone https://github.com/Brunaponciano/cuidar-mais.git
```

### 2. Entrar na pasta do projeto

```bash
cd cuidar-mais
```

### 3. Executar o programa

```bash
python main.py
```

Dependendo da instalação do Python, pode ser necessário utilizar `py main.py` no Windows.

### 📁 Arquivos de dados

Na primeira execução, o programa pode criar os arquivos `medicamentos.json` e `consultas.json` quando os dados forem salvos.

Esses arquivos são utilizados para armazenar informações localmente. Eles estão no `.gitignore` para evitar que registros locais sejam enviados ao repositório por engano.

## 📚 Aprendizados

Durante o desenvolvimento deste projeto, estou praticando:

- Lógica de programação com Python.
- Uso de variáveis, listas e dicionários.
- Estruturas condicionais e laços de repetição.
- Criação e utilização de funções.
- Tratamento de erros com `try` e `except`.
- Manipulação de datas e horários.
- Leitura e gravação de arquivos JSON.
- Controle de versão com Git e GitHub.

## 🔮 Próximos passos

- Melhorar a validação dos dados inseridos.
- Ampliar os testes das funcionalidades.
- Continuar aprimorando a organização e a legibilidade do código.
- Avaliar futuras melhorias para a experiência de uso.

## 👩‍💻 Desenvolvedora

**Bruna Santos Silva**

Projeto pessoal desenvolvido como parte da minha jornada de aprendizado em programação e desenvolvimento de software.

---

💜 *Tecnologia também pode ser uma forma de cuidar.*
# Agente Inteligente para Escolha de Local

Este projeto implementa um agente inteligente que auxilia na escolha do local mais adequado para realizar atividades, considerando características como clima, horário e ambiente. Utiliza a linguagem de programação Python e o sistema lógico Prolog para inferência de regras.

## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **PySwip**: Biblioteca Python para o SWI-Prolog.
- **SWI-Prolog**: Sistema lógico utilizado para inferência de regras.

## 📦 Pré-requisitos

Antes de rodar o projeto, é necessário:

1. **Instalar o SWI-Prolog**: Baixe e instale o SWI-Prolog a partir do [site oficial](https://www.swi-prolog.org/Download.html).

2. **Instalar o Python 3.8 ou superior**: Certifique-se de que o Python esteja instalado em sua máquina. Você pode verificar isso executando `python --version` ou `python3 --version` no terminal.

3. **Instalar o `pip`**: O `pip` é o gerenciador de pacotes do Python. Caso não o tenha, siga as instruções em [https://pip.pypa.io/en/stable/installation/](https://pip.pypa.io/en/stable/installation/).

## 🚀 Como Rodar o Projeto

Siga os passos abaixo para configurar e executar o projeto:

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/trabalho_agente_inteligente.git
cd agente-inteligente
```

### 2. Crie e ative um ambiente virtual

#### No Windows 11 (PowerShell)

```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

#### No Linux/macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

*Nota:* O uso de ambientes virtuais é recomendado para isolar as dependências do projeto.

### 3. Instale as dependências

Se você ainda não tem um arquivo `requirements.txt`, pode gerar um com o seguinte comando:

```bash
pip freeze > requirements.txt
```

Em seguida, instale as dependências:

```bash
pip install -r requirements.txt
```

### 4. Verifique se o arquivo `regras.pl` está presente

Este arquivo contém as regras Prolog necessárias para o funcionamento do agente.

### 5. Execute o script Python

```bash
python agente.py
```

O agente irá consultar os locais adequados com base no clima e horário definidos no código.

## 📄 Estrutura do Projeto

- `agente.py`: Script principal que contém a implementação do agente inteligente.
- `regras.pl`: Arquivo Prolog contendo as regras de inferência e fatos sobre os locais.
- `requirements.txt`: Arquivo contendo as dependências do projeto.
- `README.md`: Este arquivo, contendo informações sobre o projeto e como utilizá-lo.

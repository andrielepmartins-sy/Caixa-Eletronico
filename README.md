# ATM • Caixa Eletrônico

Um simulador de caixa eletrônico desenvolvido em **Python** com **Tkinter**, criado para praticar conceitos de programação, interface gráfica, funções, estruturas de decisão, manipulação de arquivos e persistência de dados.

## Sobre o projeto

O sistema simula algumas operações básicas de um caixa eletrônico através de uma interface gráfica:

* Login com número da conta e senha
* Consulta de saldo
* Saque
* Depósito
* Cálculo das cédulas utilizadas no saque
* Salvamento do saldo em arquivo
* Encerramento de sessão
* Interface gráfica inspirada em caixas eletrônicos reais

O saldo das contas é armazenado no arquivo `contas.txt`, permitindo que o valor continue disponível mesmo depois de fechar e executar o programa novamente.

## Tecnologias

* Python
* Tkinter
* Manipulação de arquivos `.txt`
* Programação procedural
* Interface gráfica (GUI)

## Funcionalidades

### Login

O usuário informa o número da conta e uma senha para acessar o sistema.

O programa verifica se os campos foram preenchidos e, após o acesso, carrega o saldo associado à conta.

### Consulta de saldo

Exibe o saldo atual da conta através de uma janela de informação.

### Saque

O usuário informa o valor desejado.

O sistema verifica:

* Se existe saldo suficiente
* Se o valor pode ser formado pelas cédulas disponíveis
* Quantas cédulas de cada valor serão utilizadas

As cédulas disponíveis são:

`R$ 100 • R$ 50 • R$ 20 • R$ 10 • R$ 5 • R$ 2`

### Depósito

Permite adicionar um valor ao saldo atual da conta.

### Persistência

Os saldos são armazenados em `contas.txt` no formato:

```text
numero_da_conta;saldo
```

O programa lê o arquivo ao entrar na conta e salva o saldo ao encerrar a sessão.

## Interface

A interface foi desenvolvida utilizando Tkinter e possui:

* Tema escuro
* Painéis para organização das informações
* Área de saldo
* Menu de operações
* Botões para as principais funções
* Mensagens de confirmação e erro

A janela principal possui resolução de `900x600`.

## Estrutura

```text
📁 projeto
│
├── main.py
├── contas.txt
└── README.md
```

> O nome do arquivo Python pode ser alterado de acordo com a organização do projeto.

## Como executar

### 1. Instale o Python

Baixe o Python pelo site oficial:

https://www.python.org/downloads/

Durante a instalação no Windows, marque a opção:

```text
Add Python to PATH
```

### 2. Clone o repositório

```bash
git clone URL_DO_REPOSITORIO
```

### 3. Entre na pasta

```bash
cd nome-do-projeto
```

### 4. Execute o programa

```bash
python main.py
```

O Tkinter utilizado pelo projeto faz parte da instalação padrão do Python em instalações comuns para Windows.

## Conceitos praticados

Este projeto foi desenvolvido para colocar em prática conceitos como:

* Variáveis
* Funções
* `if`, `elif` e `else`
* Laços `for`
* Dicionários
* Manipulação de arquivos
* Leitura e escrita de dados
* Interface gráfica
* Eventos e botões
* Entrada de dados
* Validação de informações
* Organização de código

## Observação

Este projeto é um **simulador educacional**. Ele não representa um sistema bancário real e não deve ser utilizado para armazenar informações financeiras reais.

## Desenvolvido para estudos

Projeto desenvolvido durante os estudos de **Desenvolvimento de Sistemas no SENAI**.

---

**Python + Tkinter + lógica de programação**

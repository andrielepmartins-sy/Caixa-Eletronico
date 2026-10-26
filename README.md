# ATM • Caixa Eletrônico

Um simulador de caixa eletrônico desenvolvido em **Python** com **Tkinter**, criado para praticar conceitos de programação, interface gráfica, funções, estruturas de decisão e manipulação de arquivos.

## Sobre o projeto

O sistema simula operações básicas de um caixa eletrônico por meio de uma interface gráfica. O usuário pode acessar uma conta, consultar o saldo, realizar saques e depósitos, além de consultar o extrato bancário.

Cada conta nova começa com um saldo de **R$ 1.000,00**. Os dados são armazenados em arquivos `.txt`, permitindo que as informações sejam recuperadas quando o programa for executado novamente.

## Tecnologias

- Python
- Tkinter
- Manipulação de arquivos `.txt`
- Programação procedural
- Interface gráfica (GUI)

## Funcionalidades

### Login e criação de conta

O usuário informa o número da conta e uma senha para acessar o sistema.

O programa verifica se os campos foram preenchidos e se o número da conta contém apenas números. Caso a conta já exista, a senha é verificada. Caso contrário, uma nova conta é criada com saldo inicial de R$ 1.000,00.

### Consulta de saldo

Permite consultar o saldo disponível e visualizar o número da conta utilizada na sessão.

### Saque

O usuário informa o valor que deseja sacar. O sistema verifica:

- Se o valor digitado é um número inteiro positivo.
- Se existe saldo suficiente na conta.
- Se o valor não ultrapassa R$ 100.000,00.
- Se é possível formar o valor com as cédulas disponíveis.

Antes de confirmar o saque, o programa apresenta a quantidade de cédulas que serão utilizadas. O saldo só é descontado depois da confirmação do usuário.

As cédulas disponíveis são:

`R$ 100 • R$ 50 • R$ 20 • R$ 10 • R$ 5 • R$ 2`

### Depósito

Permite adicionar um valor inteiro positivo ao saldo da conta. Após a confirmação, o sistema atualiza o saldo, salva os dados e apresenta o valor depositado e o novo saldo.

### Extrato bancário

Exibe as movimentações registradas na conta atual, incluindo:

- Data e horário da operação.
- Tipo de operação.
- Valor movimentado.
- Detalhes do saque, como as cédulas utilizadas.

A lista de movimentações possui uma barra de rolagem para facilitar a consulta.

### Persistência de dados

O programa utiliza dois arquivos de texto:

**`contas.txt`**

Armazena o número da conta, a senha e o saldo, separados por ponto e vírgula.

Formato:

```text
numero_da_conta;senha;saldo
```

**`extrato.txt`**

Armazena o número da conta, a data e o horário da operação, o tipo, o valor e os detalhes, quando houver.

Formato:

```text
numero_da_conta;data_hora;tipo;valor;detalhes
```

Os dados das contas são atualizados após as operações e ao encerrar o programa. As movimentações são acrescentadas ao extrato, sem apagar os registros anteriores.

## Interface

A interface foi desenvolvida com Tkinter e possui:

- Tema claro com tons de azul, verde e cinza.
- Campos de entrada para o número da conta e a senha.
- Botões para acessar as operações.
- Exibição do saldo disponível.
- Janelas de confirmação, informação e erro.
- Lista de movimentações com barra de rolagem.
- Navegação entre as telas de login, menu, saque, depósito e extrato.

A janela principal possui resolução de `450x500` pixels e não pode ser redimensionada.

## Estrutura do projeto

```text
📁 projeto
│
├── main.py
├── contas.txt
├── extrato.txt
└── README.md
```

Os arquivos `contas.txt` e `extrato.txt` são utilizados para armazenar os dados. O programa cria esses arquivos quando necessário, durante a execução.

O nome `main.py` pode ser alterado de acordo com a organização do projeto.

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

Substitua `URL_DO_REPOSITORIO` pelo endereço do repositório no GitHub.

### 3. Entre na pasta do projeto

```bash
cd nome-do-projeto
```

### 4. Execute o programa

```bash
python main.py
```

O Tkinter normalmente já acompanha a instalação do Python para Windows.

## Conceitos praticados

Durante o desenvolvimento, foram praticados conceitos como:

- Variáveis e tipos de dados.
- Funções e parâmetros.
- Estruturas condicionais (`if`, `elif` e `else`).
- Laços de repetição (`for` e `while`).
- Listas e dicionários.
- Validação de entradas.
- Manipulação de arquivos.
- Leitura e escrita de dados.
- Interface gráfica com Tkinter.
- Eventos e botões.
- Funções com retorno.
- Tratamento de erros com `try` e `except`.
- Organização e reutilização de código.
- Cálculo de combinações de cédulas para saques.

## Observação

Este projeto é um **simulador educacional** desenvolvido para fins de estudo. Ele não representa um sistema bancário real.

As senhas são armazenadas em arquivos de texto sem criptografia. Portanto, não utilize senhas reais nem informações financeiras pessoais.

## Desenvolvido para estudos

Projeto desenvolvido durante os estudos de **Desenvolvimento de Sistemas no SENAI**.

**Python + Tkinter + lógica de programação**

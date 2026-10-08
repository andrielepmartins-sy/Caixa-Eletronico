import tkinter as tk
from tkinter import messagebox
import os

# Arquivo onde os saldos serão salvos
ARQUIVO = "contas.txt"

# Saldo inicial para contas novas
SALDO_INICIAL = 1000

# Cédulas disponíveis no caixa
CEDULAS = [100, 50, 20, 10, 5, 2]


# Cores do sistema
FUNDO = "#0D0914"
CARD = "#171020"
CARD_2 = "#21152E"

ROXO = "#9B5DE5"
ROXO_CLARO = "#B87CFF"
ROXO_ESCURO = "#6A35A8"

BRANCO = "#F5F0FA"
CINZA = "#9B91A8"
VERMELHO = "#FF5577"


# Variáveis da conta atual
conta_atual = ""
saldo = 0


# ---------------------------------------------------------
# CARREGAR SALDO
# ---------------------------------------------------------

def carregar_saldo(conta):
    """Busca o saldo da conta no arquivo."""

    if not os.path.exists(ARQUIVO):
        return SALDO_INICIAL

    arquivo = open(ARQUIVO, "r", encoding="utf-8")

    for linha in arquivo:
        linha = linha.strip()

        if linha != "":
            dados = linha.split(";")

            if len(dados) == 2 and dados[0] == conta:
                arquivo.close()
                return int(dados[1])

    arquivo.close()

    return SALDO_INICIAL


# ---------------------------------------------------------
# SALVAR SALDO
# ---------------------------------------------------------

def salvar_saldo(conta, novo_saldo):
    """Salva o saldo da conta no arquivo."""

    contas = []

    if os.path.exists(ARQUIVO):
        arquivo = open(ARQUIVO, "r", encoding="utf-8")

        for linha in arquivo:
            linha = linha.strip()

            if linha != "":
                dados = linha.split(";")

                if len(dados) == 2:

                    if dados[0] == conta:
                        contas.append(
                            conta + ";" + str(novo_saldo)
                        )
                    else:
                        contas.append(
                            dados[0] + ";" + dados[1]
                        )

        arquivo.close()

    conta_encontrada = False

    for linha in contas:
        dados = linha.split(";")

        if dados[0] == conta:
            conta_encontrada = True
            break

    if not conta_encontrada:
        contas.append(
            conta + ";" + str(novo_saldo)
        )

    arquivo = open(ARQUIVO, "w", encoding="utf-8")

    for linha in contas:
        arquivo.write(linha + "\n")

    arquivo.close()


# ---------------------------------------------------------
# CALCULAR CÉDULAS
# ---------------------------------------------------------

def calcular_cedulas(valor):

    cedulas_entregues = {}

    valor_restante = valor

    indice = 0

    while valor_restante > 0 and indice < len(CEDULAS):

        cedula = CEDULAS[indice]

        quantidade = valor_restante // cedula

        if quantidade > 0:

            cedulas_entregues[cedula] = quantidade

            valor_restante = valor_restante % cedula

        indice += 1

    # Se sobrou algum valor,
    # significa que o caixa não consegue formar o valor.
    if valor_restante != 0:
        return None

    return cedulas_entregues


# ---------------------------------------------------------
# FUNÇÕES DA INTERFACE
# ---------------------------------------------------------

def limpar_tela():

    for widget in janela.winfo_children():
        widget.destroy()


def criar_botao(pai, texto, comando, largura=20):

    return tk.Button(
        pai,
        text=texto,
        command=comando,
        width=largura,
        height=2,
        bg=CARD_2,
        fg=BRANCO,
        activebackground=ROXO_ESCURO,
        activeforeground=BRANCO,
        relief="flat",
        bd=0,
        cursor="hand2",
        font=("Arial", 10, "bold")
    )


def criar_entrada(pai, largura=30):

    return tk.Entry(
        pai,
        width=largura,
        bg=CARD_2,
        fg=BRANCO,
        insertbackground=ROXO_CLARO,
        relief="flat",
        bd=0,
        font=("Arial", 12)
    )


# ---------------------------------------------------------
# LOGIN

def entrar():

    global conta_atual
    global saldo

    conta = entrada_conta.get().strip()
    senha = entrada_senha.get().strip()

    if conta == "":
        messagebox.showerror(
            "Erro",
            "Digite sua conta."
        )
        return

    if senha == "":
        messagebox.showerror(
            "Erro",
            "Digite sua senha."
        )
        return

    # A senha não precisa ser validada,
    # conforme o enunciado do trabalho.

    conta_atual = conta

    saldo = carregar_saldo(conta_atual)

    tela_menu()


# ---------------------------------------------------------
# TELA DE LOGIN

def tela_login():

    global entrada_conta
    global entrada_senha

    limpar_tela()

    fundo = tk.Frame(
        janela,
        bg=FUNDO
    )

    fundo.pack(
        fill="both",
        expand=True
    )

    tk.Label(
        fundo,
        text="MIT",
        bg=FUNDO,
        fg=ROXO_CLARO,
        font=("Arial", 46, "bold")
    ).pack(
        pady=(65, 0)
    )

    tk.Label(
        fundo,
        text="• MIT SYSTEM •",
        bg=FUNDO,
        fg=CINZA,
        font=("Arial", 10, "bold")
    ).pack(
        pady=(0, 25)
    )

    card = tk.Frame(
        fundo,
        bg=CARD,
        width=420,
        height=290
    )

    card.pack()

    card.pack_propagate(False)

    tk.Label(
        card,
        text="Acessar sistema",
        bg=CARD,
        fg=BRANCO,
        font=("Arial", 19, "bold")
    ).pack(
        pady=(25, 20)
    )

    tk.Label(
        card,
        text="CONTA",
        bg=CARD,
        fg=CINZA,
        font=("Arial", 9, "bold")
    ).pack(
        anchor="w",
        padx=55
    )

    entrada_conta = criar_entrada(
        card,
        30
    )

    entrada_conta.pack(
        pady=(5, 12)
    )

    tk.Label(
        card,
        text="SENHA",
        bg=CARD,
        fg=CINZA,
        font=("Arial", 9, "bold")
    ).pack(
        anchor="w",
        padx=55
    )

    entrada_senha = criar_entrada(
        card,
        30
    )

    entrada_senha.config(
        show="*"
    )

    entrada_senha.pack(
        pady=5
    )

    tk.Button(
        card,
        text="ENTRAR  →",
        command=entrar,
        width=28,
        height=2,
        bg=ROXO,
        fg=BRANCO,
        activebackground=ROXO_ESCURO,
        activeforeground=BRANCO,
        relief="flat",
        bd=0,
        cursor="hand2",
        font=("Arial", 10, "bold")
    ).pack(
        pady=18
    )

    tk.Label(
        fundo,
        text="● SYSTEM ONLINE",
        bg=FUNDO,
        fg=ROXO_CLARO,
        font=("Arial", 8, "bold")
    ).pack(
        pady=20
    )


# ---------------------------------------------------------
# MENU PRINCIPAL

def tela_menu():

    global label_saldo

    limpar_tela()

    header = tk.Frame(
        janela,
        bg=CARD,
        height=75
    )

    header.pack(
        fill="x"
    )

    header.pack_propagate(False)

    tk.Label(
        header,
        text="MIT",
        bg=CARD,
        fg=ROXO_CLARO,
        font=("Arial", 25, "bold")
    ).pack(
        side="left",
        padx=30
    )

    tk.Label(
        header,
        text="ATM SYSTEM / ONLINE",
        bg=CARD,
        fg=CINZA,
        font=("Arial", 9, "bold")
    ).pack(
        side="left"
    )

    tk.Label(
        header,
        text="CONTA: " + conta_atual,
        bg=CARD,
        fg=BRANCO,
        font=("Arial", 10, "bold")
    ).pack(
        side="right",
        padx=30
    )

    conteudo = tk.Frame(
        janela,
        bg=FUNDO
    )

    conteudo.pack(
        fill="both",
        expand=True,
        padx=40,
        pady=30
    )

    tk.Label(
        conteudo,
        text="Painel de operações",
        bg=FUNDO,
        fg=BRANCO,
        font=("Arial", 24, "bold")
    ).pack(
        anchor="w"
    )

    tk.Label(
        conteudo,
        text="Escolha uma operação para continuar",
        bg=FUNDO,
        fg=CINZA,
        font=("Arial", 10)
    ).pack(
        anchor="w",
        pady=(3, 20)
    )

    saldo_card = tk.Frame(
        conteudo,
        bg=CARD,
        height=105
    )

    saldo_card.pack(
        fill="x"
    )

    saldo_card.pack_propagate(False)

    tk.Label(
        saldo_card,
        text="SALDO DISPONÍVEL",
        bg=CARD,
        fg=CINZA,
        font=("Arial", 9, "bold")
    ).pack(
        anchor="w",
        padx=25,
        pady=(15, 0)
    )

    label_saldo = tk.Label(
        saldo_card,
        text="R$ {:.2f}".format(
            saldo
        ).replace(".", ","),
        bg=CARD,
        fg=ROXO_CLARO,
        font=("Arial", 25, "bold")
    )

    label_saldo.pack(
        anchor="w",
        padx=25
    )

    operacoes = tk.Frame(
        conteudo,
        bg=FUNDO
    )

    operacoes.pack(
        fill="x",
        pady=25
    )

    criar_card_operacao(
        operacoes,
        "01",
        "Consultar saldo",
        consultar_saldo
    )

    criar_card_operacao(
        operacoes,
        "02",
        "Sacar dinheiro",
        tela_saque
    )

    criar_card_operacao(
        operacoes,
        "03",
        "Depositar dinheiro",
        tela_deposito
    )

    tk.Button(
        conteudo,
        text="ENCERRAR SESSÃO",
        command=sair,
        width=25,
        height=2,
        bg=CARD_2,
        fg=VERMELHO,
        activebackground=VERMELHO,
        activeforeground=BRANCO,
        relief="flat",
        bd=0,
        cursor="hand2",
        font=("Arial", 9, "bold")
    ).pack(
        pady=5
    )


# ---------------------------------------------------------
# CARDS DE OPERAÇÃO

def criar_card_operacao(
    pai,
    numero,
    texto,
    comando
):

    card = tk.Frame(
        pai,
        bg=CARD,
        width=230,
        height=115
    )

    card.pack(
        side="left",
        padx=10
    )

    card.pack_propagate(False)

    tk.Label(
        card,
        text=numero,
        bg=CARD,
        fg=ROXO_CLARO,
        font=("Arial", 9, "bold")
    ).pack(
        anchor="w",
        padx=20,
        pady=(15, 0)
    )

    tk.Label(
        card,
        text=texto,
        bg=CARD,
        fg=BRANCO,
        font=("Arial", 11, "bold")
    ).pack(
        anchor="w",
        padx=20,
        pady=3
    )

    tk.Button(
        card,
        text="ACESSAR",
        command=comando,
        bg=CARD,
        fg=ROXO_CLARO,
        activebackground=CARD,
        activeforeground=BRANCO,
        relief="flat",
        bd=0,
        cursor="hand2",
        font=("Arial", 8, "bold")
    ).pack(
        anchor="w",
        padx=15
    )


# ---------------------------------------------------------
# CONSULTAR SALDO


def consultar_saldo():

    messagebox.showinfo(
        "Saldo",
        "Conta: " + conta_atual +
        "\n\nSaldo atual:\nR$ {:.2f}".format(
            saldo
        ).replace(".", ",")
    )


# ---------------------------------------------------------
# TELA DE SAQUE

def tela_saque():

    global entrada_saque

    limpar_tela()

    tk.Label(
        janela,
        text="Saque de dinheiro",
        bg=FUNDO,
        fg=BRANCO,
        font=("Arial", 25, "bold")
    ).pack(
        pady=(70, 5)
    )

    tk.Label(
        janela,
        text="Digite o valor que deseja retirar",
        bg=FUNDO,
        fg=CINZA,
        font=("Arial", 10)
    ).pack()

    card = tk.Frame(
        janela,
        bg=CARD,
        width=450,
        height=230
    )

    card.pack(
        pady=30
    )

    card.pack_propagate(False)

    tk.Label(
        card,
        text="VALOR DO SAQUE",
        bg=CARD,
        fg=CINZA,
        font=("Arial", 9, "bold")
    ).pack(
        pady=(35, 5)
    )

    entrada_saque = criar_entrada(
        card,
        25
    )

    entrada_saque.pack()

    tk.Label(
        card,
        text="Somente números inteiros",
        bg=CARD,
        fg=CINZA,
        font=("Arial", 8)
    ).pack(
        pady=5
    )

    tk.Button(
        card,
        text="CONFIRMAR SAQUE",
        command=sacar,
        width=25,
        height=2,
        bg=ROXO,
        fg=BRANCO,
        activebackground=ROXO_ESCURO,
        activeforeground=BRANCO,
        relief="flat",
        bd=0,
        cursor="hand2",
        font=("Arial", 9, "bold")
    ).pack(
        pady=15
    )

    criar_botao(
        janela,
        "← VOLTAR",
        tela_menu,
        15
    ).pack()


# ---------------------------------------------------------
# REALIZAR SAQUE

def sacar():

    global saldo

    valor_texto = entrada_saque.get().strip()

    if valor_texto == "":
        messagebox.showerror(
            "Erro",
            "Digite o valor do saque."
        )
        return

    if "." in valor_texto or "," in valor_texto:
        messagebox.showerror(
            "Erro",
            "Somente valores inteiros são aceitos."
        )
        return

    try:
        valor = int(valor_texto)

    except ValueError:
        messagebox.showerror(
            "Erro",
            "Digite um valor inteiro válido."
        )
        return

    if valor <= 0:
        messagebox.showerror(
            "Erro",
            "O valor deve ser maior que zero."
        )
        return

    if valor > saldo:
        messagebox.showerror(
            "Erro",
            "Saldo insuficiente."
        )
        return

    cedulas = calcular_cedulas(valor)

    if cedulas is None:

        messagebox.showerror(
            "Erro",
            "Esse valor não pode ser formado pelas "
            "cédulas disponíveis.\n\n"
            "R$ 100 | R$ 50 | R$ 20 | "
            "R$ 10 | R$ 5 | R$ 2"
        )

        return

    mensagem = "SAQUE REALIZADO\n\n"
    mensagem += "Cédulas entregues:\n\n"

    for cedula in CEDULAS:

        if cedula in cedulas:

            quantidade = cedulas[cedula]

            if quantidade == 1:

                mensagem += (
                    "1 cédula de R$ {}\n"
                    .format(cedula)
                )

            else:

                mensagem += (
                    "{} cédulas de R$ {}\n"
                    .format(
                        quantidade,
                        cedula
                    )
                )

    saldo = saldo - valor

    mensagem += (
        "\nNovo saldo: R$ {:.2f}"
        .format(saldo)
        .replace(".", ",")
    )

    messagebox.showinfo(
        "Saque",
        mensagem
    )

    tela_menu()


# ---------------------------------------------------------
# TELA DE DEPÓSITO

def tela_deposito():

    global entrada_deposito

    limpar_tela()

    tk.Label(
        janela,
        text="Depósito",
        bg=FUNDO,
        fg=BRANCO,
        font=("Arial", 25, "bold")
    ).pack(
        pady=(70, 5)
    )

    tk.Label(
        janela,
        text="Digite o valor que deseja depositar",
        bg=FUNDO,
        fg=CINZA,
        font=("Arial", 10)
    ).pack()

    card = tk.Frame(
        janela,
        bg=CARD,
        width=450,
        height=230
    )

    card.pack(
        pady=30
    )

    card.pack_propagate(False)

    tk.Label(
        card,
        text="VALOR DO DEPÓSITO",
        bg=CARD,
        fg=CINZA,
        font=("Arial", 9, "bold")
    ).pack(
        pady=(35, 5)
    )

    entrada_deposito = criar_entrada(
        card,
        25
    )

    entrada_deposito.pack()

    tk.Label(
        card,
        text="Somente números inteiros",
        bg=CARD,
        fg=CINZA,
        font=("Arial", 8)
    ).pack(
        pady=5
    )

    tk.Button(
        card,
        text="CONFIRMAR DEPÓSITO",
        command=depositar,
        width=25,
        height=2,
        bg=ROXO,
        fg=BRANCO,
        activebackground=ROXO_ESCURO,
        activeforeground=BRANCO,
        relief="flat",
        bd=0,
        cursor="hand2",
        font=("Arial", 9, "bold")
    ).pack(
        pady=15
    )

    criar_botao(
        janela,
        "← VOLTAR",
        tela_menu,
        15
    ).pack()


# ---------------------------------------------------------
# REALIZAR DEPÓSITO

def depositar():

    global saldo

    valor_texto = entrada_deposito.get().strip()

    if valor_texto == "":
        messagebox.showerror(
            "Erro",
            "Digite o valor do depósito."
        )
        return

    if "." in valor_texto or "," in valor_texto:
        messagebox.showerror(
            "Erro",
            "Somente valores inteiros são aceitos."
        )
        return

    try:
        valor = int(valor_texto)

    except ValueError:
        messagebox.showerror(
            "Erro",
            "Digite um valor inteiro válido."
        )
        return

    if valor <= 0:
        messagebox.showerror(
            "Erro",
            "O valor deve ser maior que zero."
        )
        return

    saldo = saldo + valor

    messagebox.showinfo(
        "Depósito",
        "Depósito realizado!\n\n"
        "Valor: R$ {:.2f}\n"
        "Novo saldo: R$ {:.2f}".format(
            valor,
            saldo
        ).replace(".", ",")
    )

    tela_menu()


# ---------------------------------------------------------
# SAIR

def sair():

    salvar_saldo(
        conta_atual,
        saldo
    )

    messagebox.showinfo(
        "MIT ATM",
        "Saldo salvo com sucesso.\n\n"
        "Sessão encerrada."
    )

    janela.destroy()


# ---------------------------------------------------------
# PROGRAMA PRINCIPAL


janela = tk.Tk()

janela.title(
    "MIT ATM"
)

janela.geometry(
    "850x600"
)

janela.resizable(
    False,
    False
)

janela.configure(
    bg=FUNDO
)

tela_login()

janela.mainloop()
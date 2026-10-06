import os
import tkinter as tk
from tkinter import messagebox, simpledialog


# ==========================================
# CONFIGURAÇÕES
# ==========================================

ARQUIVO = "contas.txt"
SALDO_INICIAL = 1000


# ==========================================
# CORES
# ==========================================

FUNDO = "#05090D"
PAINEL = "#0A1118"
PAINEL_2 = "#101B24"
BORDA = "#18313B"

VERDE = "#00F5A0"
VERDE_ESCURO = "#00B87A"
CIANO = "#00D9FF"

BRANCO = "#EFFFFA"
CINZA = "#70818D"
CINZA_CLARO = "#B8C8CF"

VERMELHO = "#FF4567"


# ==========================================
# VARIÁVEIS
# ==========================================

conta = ""
senha = ""
saldo = 0


# ==========================================
# ARQUIVO
# ==========================================

def carregar_saldo(conta):

    if not os.path.exists(ARQUIVO):
        return SALDO_INICIAL

    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:

        for linha in arquivo:

            dados = linha.strip().split(";")

            if len(dados) == 2 and dados[0] == conta:
                return int(dados[1])

    return SALDO_INICIAL


def salvar_saldo(conta, saldo):

    contas = {}

    if os.path.exists(ARQUIVO):

        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:

            for linha in arquivo:

                dados = linha.strip().split(";")

                if len(dados) == 2:
                    contas[dados[0]] = int(dados[1])

    contas[conta] = saldo

    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:

        for numero_conta, valor in contas.items():

            arquivo.write(
                f"{numero_conta};{valor}\n"
            )


# ==========================================
# CÉDULAS
# ==========================================

def calcular_cedulas(valor):

    cedulas = [100, 50, 20, 10, 5, 2]

    resultado = {}

    restante = valor

    for cedula in cedulas:

        quantidade = restante // cedula

        restante = restante % cedula

        if quantidade > 0:
            resultado[cedula] = quantidade

    if restante != 0:
        return None

    return resultado


def mostrar_cedulas(cedulas):

    texto = ""

    for valor, quantidade in cedulas.items():

        if quantidade == 1:
            texto += f"1 cédula de R$ {valor}\n"

        else:
            texto += f"{quantidade} cédulas de R$ {valor}\n"

    return texto


# ==========================================
# JANELA
# ==========================================

janela = tk.Tk()

janela.title("ATM // FUTURE BANK")
janela.geometry("950x620")
janela.resizable(False, False)

janela.configure(
    bg=FUNDO
)


# ==========================================
# FUNÇÕES VISUAIS
# ==========================================

def limpar_tela():

    for widget in janela.winfo_children():
        widget.destroy()


def linha_tecnologica(pai):

    linha = tk.Frame(
        pai,
        bg=VERDE,
        height=1
    )

    linha.pack(
        fill="x"
    )

    return linha


def botao_menu(
    pai,
    texto,
    comando,
    cor=PAINEL_2
):

    botao = tk.Button(

        pai,

        text=texto,

        command=comando,

        font=(
            "Consolas",
            10,
            "bold"
        ),

        fg=BRANCO,

        bg=cor,

        activebackground=VERDE,

        activeforeground=FUNDO,

        relief="flat",

        bd=0,

        cursor="hand2",

        anchor="w",

        padx=20,

        height=2
    )

    def entrar(event):

        botao.config(
            bg=VERDE,
            fg=FUNDO
        )

    def sair(event):

        botao.config(
            bg=cor,
            fg=BRANCO
        )

    botao.bind(
        "<Enter>",
        entrar
    )

    botao.bind(
        "<Leave>",
        sair
    )

    return botao


# ==========================================
# LOGIN
# ==========================================

def tela_login():

    limpar_tela()

    # --------------------------------------
    # HEADER
    # --------------------------------------

    topo = tk.Frame(
        janela,
        bg=PAINEL,
        height=72
    )

    topo.pack(
        fill="x"
    )

    tk.Label(
        topo,
        text="ATM",
        font=(
            "Consolas",
            24,
            "bold"
        ),
        fg=VERDE,
        bg=PAINEL
    ).pack(
        side="left",
        padx=30
    )

    tk.Label(
        topo,
        text="// FUTURE BANK SYSTEM",
        font=(
            "Consolas",
            10,
            "bold"
        ),
        fg=CINZA,
        bg=PAINEL
    ).pack(
        side="left"
    )

    tk.Label(
        topo,
        text="● SYSTEM ONLINE",
        font=(
            "Consolas",
            9,
            "bold"
        ),
        fg=VERDE,
        bg=PAINEL
    ).pack(
        side="right",
        padx=30
    )

    # Linha
    tk.Frame(
        janela,
        bg=VERDE,
        height=2
    ).pack(
        fill="x"
    )

    # --------------------------------------
    # ÁREA CENTRAL
    # --------------------------------------

    centro = tk.Frame(
        janela,
        bg=FUNDO
    )

    centro.place(
        relx=0.5,
        rely=0.53,
        anchor="center"
    )

    tk.Label(
        centro,
        text="ACCESS TERMINAL",
        font=(
            "Consolas",
            25,
            "bold"
        ),
        fg=BRANCO,
        bg=FUNDO
    ).pack()

    tk.Label(
        centro,
        text="SECURE BANKING INTERFACE",
        font=(
            "Consolas",
            9
        ),
        fg=CIANO,
        bg=FUNDO
    ).pack(
        pady=(5, 20)
    )

    # --------------------------------------
    # CARD
    # --------------------------------------

    painel = tk.Frame(
        centro,
        bg=PAINEL,
        padx=35,
        pady=30,
        highlightbackground=BORDA,
        highlightthickness=1
    )

    painel.pack()

    # Pequeno indicador
    tk.Label(
        painel,
        text="[ AUTHENTICATION REQUIRED ]",
        font=(
            "Consolas",
            8,
            "bold"
        ),
        fg=VERDE,
        bg=PAINEL
    ).pack(
        pady=(0, 22)
    )

    # Conta
    tk.Label(
        painel,
        text="ACCOUNT ID",
        font=(
            "Consolas",
            9,
            "bold"
        ),
        fg=CINZA_CLARO,
        bg=PAINEL
    ).pack(
        anchor="w"
    )

    entrada_conta = tk.Entry(
        painel,
        font=(
            "Consolas",
            12
        ),
        bg=PAINEL_2,
        fg=BRANCO,
        insertbackground=VERDE,
        relief="flat",
        width=34
    )

    entrada_conta.pack(
        pady=(6, 18),
        ipady=9
    )

    # Senha
    tk.Label(
        painel,
        text="ACCESS CODE",
        font=(
            "Consolas",
            9,
            "bold"
        ),
        fg=CINZA_CLARO,
        bg=PAINEL
    ).pack(
        anchor="w"
    )

    entrada_senha = tk.Entry(
        painel,
        font=(
            "Consolas",
            12
        ),
        bg=PAINEL_2,
        fg=BRANCO,
        insertbackground=VERDE,
        relief="flat",
        show="*",
        width=34
    )

    entrada_senha.pack(
        pady=(6, 22),
        ipady=9
    )

    # --------------------------------------
    # ENTRAR
    # --------------------------------------

    def entrar():

        global conta
        global senha
        global saldo

        conta_digitada = (
            entrada_conta
            .get()
            .strip()
        )

        senha_digitada = (
            entrada_senha
            .get()
            .strip()
        )

        if conta_digitada == "":

            messagebox.showerror(
                "ACCESS ERROR",
                "Digite o número da conta."
            )

            return

        if senha_digitada == "":

            messagebox.showerror(
                "ACCESS ERROR",
                "Digite a senha."
            )

            return

        conta = conta_digitada

        senha = senha_digitada

        saldo = carregar_saldo(
            conta
        )

        tela_menu()

    botao = tk.Button(
        painel,
        text="[ ENTER SYSTEM ]",
        command=entrar,
        font=(
            "Consolas",
            10,
            "bold"
        ),
        fg=FUNDO,
        bg=VERDE,
        activebackground=VERDE_ESCURO,
        activeforeground=FUNDO,
        relief="flat",
        cursor="hand2",
        width=34,
        height=2
    )

    botao.pack()

    def hover_entrar(event):

        botao.config(
            bg=CIANO
        )

    def sair_entrar(event):

        botao.config(
            bg=VERDE
        )

    botao.bind(
        "<Enter>",
        hover_entrar
    )

    botao.bind(
        "<Leave>",
        sair_entrar
    )

    # Rodapé
    tk.Label(
        janela,
        text="SENAI // BANKING SIMULATION // v1.0",
        font=(
            "Consolas",
            8
        ),
        fg=CINZA,
        bg=FUNDO
    ).pack(
        side="bottom",
        pady=12
    )


# ==========================================
# MENU
# ==========================================

def tela_menu():

    limpar_tela()

    # --------------------------------------
    # HEADER
    # --------------------------------------

    topo = tk.Frame(
        janela,
        bg=PAINEL,
        height=75
    )

    topo.pack(
        fill="x"
    )

    tk.Label(
        topo,
        text="ATM",
        font=(
            "Consolas",
            24,
            "bold"
        ),
        fg=VERDE,
        bg=PAINEL
    ).pack(
        side="left",
        padx=25
    )

    tk.Label(
        topo,
        text="// CONTROL PANEL",
        font=(
            "Consolas",
            10,
            "bold"
        ),
        fg=CINZA,
        bg=PAINEL
    ).pack(
        side="left"
    )

    tk.Label(
        topo,
        text="● ONLINE",
        font=(
            "Consolas",
            9,
            "bold"
        ),
        fg=VERDE,
        bg=PAINEL
    ).pack(
        side="right",
        padx=25
    )

    # Linha
    tk.Frame(
        janela,
        bg=VERDE,
        height=2
    ).pack(
        fill="x"
    )

    # --------------------------------------
    # CONTEÚDO
    # --------------------------------------

    conteudo = tk.Frame(
        janela,
        bg=FUNDO
    )

    conteudo.pack(
        fill="both",
        expand=True,
        padx=35,
        pady=25
    )

    # --------------------------------------
    # ESQUERDA
    # --------------------------------------

    esquerda = tk.Frame(
        conteudo,
        bg=FUNDO
    )

    esquerda.pack(
        side="left",
        fill="both",
        expand=True,
        padx=(0, 18)
    )

    tk.Label(
        esquerda,
        text="SYSTEM OVERVIEW",
        font=(
            "Consolas",
            10,
            "bold"
        ),
        fg=CINZA,
        bg=FUNDO
    ).pack(
        anchor="w"
    )

    # --------------------------------------
    # CARD SALDO
    # --------------------------------------

    cartao = tk.Frame(
        esquerda,
        bg=PAINEL,
        padx=28,
        pady=25,
        highlightbackground=BORDA,
        highlightthickness=1
    )

    cartao.pack(
        fill="x",
        pady=(10, 15)
    )

    tk.Label(
        cartao,
        text="AVAILABLE BALANCE",
        font=(
            "Consolas",
            9,
            "bold"
        ),
        fg=CINZA,
        bg=PAINEL
    ).pack(
        anchor="w"
    )

    tk.Label(
        cartao,
        text=f"R$ {saldo},00",
        font=(
            "Consolas",
            30,
            "bold"
        ),
        fg=VERDE,
        bg=PAINEL
    ).pack(
        anchor="w",
        pady=8
    )

    tk.Label(
        cartao,
        text="// BALANCE UPDATED",
        font=(
            "Consolas",
            8
        ),
        fg=CINZA,
        bg=PAINEL
    ).pack(
        anchor="w"
    )

    # --------------------------------------
    # INFORMAÇÕES
    # --------------------------------------

    informacao = tk.Frame(
        esquerda,
        bg=PAINEL,
        padx=25,
        pady=20,
        highlightbackground=BORDA,
        highlightthickness=1
    )

    informacao.pack(
        fill="x"
    )

    tk.Label(
        informacao,
        text="ACCOUNT STATUS",
        font=(
            "Consolas",
            9,
            "bold"
        ),
        fg=CINZA,
        bg=PAINEL
    ).pack(
        anchor="w"
    )

    tk.Label(
        informacao,
        text="●  ACCOUNT ACTIVE",
        font=(
            "Consolas",
            11,
            "bold"
        ),
        fg=VERDE,
        bg=PAINEL
    ).pack(
        anchor="w",
        pady=(8, 4)
    )

    tk.Label(
        informacao,
        text=f"ID: {conta}",
        font=(
            "Consolas",
            9
        ),
        fg=CINZA_CLARO,
        bg=PAINEL
    ).pack(
        anchor="w"
    )

    # --------------------------------------
    # DIREITA
    # --------------------------------------

    direita = tk.Frame(
        conteudo,
        bg=FUNDO
    )

    direita.pack(
        side="right",
        fill="both",
        expand=True
    )

    tk.Label(
        direita,
        text="AVAILABLE OPERATIONS",
        font=(
            "Consolas",
            10,
            "bold"
        ),
        fg=CINZA,
        bg=FUNDO
    ).pack(
        anchor="w"
    )

    # Botões
    botao_menu(
        direita,
        "▣   CONSULT BALANCE",
        consultar_saldo
    ).pack(
        fill="x",
        pady=(10, 6)
    )

    botao_menu(
        direita,
        "↓   WITHDRAW MONEY",
        sacar
    ).pack(
        fill="x",
        pady=6
    )

    botao_menu(
        direita,
        "↑   DEPOSIT MONEY",
        depositar
    ).pack(
        fill="x",
        pady=6
    )

    # Separador
    tk.Frame(
        direita,
        bg=BORDA,
        height=1
    ).pack(
        fill="x",
        pady=18
    )

    # Sair
    botao_sair = tk.Button(
        direita,
        text="[ TERMINATE SESSION ]",
        font=(
            "Consolas",
            10,
            "bold"
        ),
        fg=BRANCO,
        bg="#251018",
        activebackground=VERMELHO,
        activeforeground=BRANCO,
        relief="flat",
        cursor="hand2",
        height=2,
        command=sair
    )

    botao_sair.pack(
        fill="x"
    )

    def hover_sair(event):

        botao_sair.config(
            bg=VERMELHO
        )

    def sair_sair(event):

        botao_sair.config(
            bg="#251018"
        )

    botao_sair.bind(
        "<Enter>",
        hover_sair
    )

    botao_sair.bind(
        "<Leave>",
        sair_sair
    )

    # --------------------------------------
    # RODAPÉ
    # --------------------------------------

    tk.Label(
        janela,
        text="ATM SYSTEM // SECURE CONNECTION // SENAI",
        font=(
            "Consolas",
            8
        ),
        fg=CINZA,
        bg=FUNDO
    ).pack(
        pady=(0, 10)
    )


# ==========================================
# CONSULTAR SALDO
# ==========================================

def consultar_saldo():

    messagebox.showinfo(
        "BALANCE",
        f"CURRENT BALANCE\n\n"
        f"R$ {saldo},00"
    )


# ==========================================
# SAQUE
# ==========================================

def sacar():

    global saldo

    valor = simpledialog.askinteger(
        "WITHDRAW",
        "Digite o valor que deseja sacar:",
        parent=janela,
        minvalue=1
    )

    if valor is None:
        return

    if valor > saldo:

        messagebox.showerror(
            "INSUFFICIENT BALANCE",
            "O valor solicitado é maior "
            "que o saldo disponível."
        )

        return

    cedulas = calcular_cedulas(
        valor
    )

    if cedulas is None:

        messagebox.showerror(
            "INVALID VALUE",
            "Não é possível formar esse valor "
            "com as cédulas disponíveis.\n\n"
            "R$ 100 • R$ 50 • R$ 20\n"
            "R$ 10 • R$ 5 • R$ 2"
        )

        return

    saldo -= valor

    texto = (
        "WITHDRAW COMPLETED\n\n"
        f"Valor: R$ {valor},00\n\n"
    )

    texto += mostrar_cedulas(
        cedulas
    )

    texto += (
        f"\nSaldo restante: "
        f"R$ {saldo},00"
    )

    messagebox.showinfo(
        "WITHDRAW",
        texto
    )

    tela_menu()


# ==========================================
# DEPÓSITO
# ==========================================

def depositar():

    global saldo

    valor = simpledialog.askinteger(
        "DEPOSIT",
        "Digite o valor que deseja depositar:",
        parent=janela,
        minvalue=1
    )

    if valor is None:
        return

    saldo += valor

    messagebox.showinfo(
        "DEPOSIT COMPLETED",
        "DEPÓSITO CONCLUÍDO!\n\n"
        f"Valor: R$ {valor},00\n\n"
        f"Novo saldo: R$ {saldo},00"
    )

    tela_menu()


# ==========================================
# SAIR
# ==========================================

def sair():

    salvar_saldo(
        conta,
        saldo
    )

    resposta = messagebox.askyesno(
        "TERMINATE SESSION",
        "O saldo foi salvo com sucesso.\n\n"
        "Deseja realmente encerrar?"
    )

    if resposta:

        janela.destroy()

    else:

        tela_menu()


# ==========================================
# INICIAR
# ==========================================

tela_login()

janela.mainloop()

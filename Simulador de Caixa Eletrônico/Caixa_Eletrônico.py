import os
import tkinter as tk
from tkinter import messagebox, simpledialog


ARQUIVO = "contas.txt"
SALDO_INICIAL = 1000


# ==========================================
# CORES
# ==========================================

FUNDO = "#0B1117"
PAINEL = "#111A23"
PAINEL_2 = "#17232E"
BORDA = "#263746"

VERDE = "#00E096"
VERDE_ESCuro = "#00B878"

BRANCO = "#F5F7FA"
CINZA = "#8D9AA8"
CINZA_CLARO = "#C8D0D8"

VERMELHO = "#FF5C5C"
AZUL = "#3D8BFF"


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

            texto += (
                f"1 cédula de R$ {valor}\n"
            )

        else:

            texto += (
                f"{quantidade} cédulas de R$ {valor}\n"
            )

    return texto


# ==========================================
# JANELA
# ==========================================

janela = tk.Tk()

janela.title("ATM • Caixa Eletrônico")
janela.geometry("900x600")
janela.resizable(False, False)

janela.configure(
    bg=FUNDO
)


conta = ""
senha = ""
saldo = 0


# ==========================================
# FUNÇÕES VISUAIS
# ==========================================

def limpar_tela():

    for widget in janela.winfo_children():
        widget.destroy()


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
            "Arial",
            11,
            "bold"
        ),

        fg=BRANCO,

        bg=cor,

        activebackground=VERDE,

        activeforeground=FUNDO,

        relief="flat",

        cursor="hand2",

        width=25,

        height=2

    )

    return botao


# ==========================================
# LOGIN
# ==========================================

def tela_login():

    limpar_tela()

    # Container central
    centro = tk.Frame(
        janela,
        bg=FUNDO
    )

    centro.place(
        relx=0.5,
        rely=0.5,
        anchor="center"
    )

    # Logo
    tk.Label(

        centro,

        text="ATM",

        font=(
            "Arial",
            42,
            "bold"
        ),

        fg=VERDE,

        bg=FUNDO

    ).pack()

    tk.Label(

        centro,

        text="CAIXA ELETRÔNICO",

        font=(
            "Arial",
            20,
            "bold"
        ),

        fg=BRANCO,

        bg=FUNDO

    ).pack(
        pady=(0, 5)
    )

    tk.Label(

        centro,

        text="ACESSO SEGURO AO SISTEMA",

        font=(
            "Arial",
            9,
            "bold"
        ),

        fg=CINZA,

        bg=FUNDO

    ).pack(
        pady=(0, 25)
    )

    # Painel
    painel = tk.Frame(

        centro,

        bg=PAINEL,

        padx=45,

        pady=35,

        highlightbackground=BORDA,

        highlightthickness=1

    )

    painel.pack()

    tk.Label(

        painel,

        text="NÚMERO DA CONTA",

        font=(
            "Arial",
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
            "Arial",
            13
        ),

        bg=PAINEL_2,

        fg=BRANCO,

        insertbackground=VERDE,

        relief="flat",

        width=34

    )

    entrada_conta.pack(
        pady=(7, 20),
        ipady=9
    )

    tk.Label(

        painel,

        text="SENHA",

        font=(
            "Arial",
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
            "Arial",
            13
        ),

        bg=PAINEL_2,

        fg=BRANCO,

        insertbackground=VERDE,

        relief="flat",

        show="*",

        width=34

    )

    entrada_senha.pack(
        pady=(7, 25),
        ipady=9
    )

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
                "Erro",
                "Digite o número da conta."
            )

            return

        if senha_digitada == "":

            messagebox.showerror(
                "Erro",
                "Digite a senha."
            )

            return

        conta = conta_digitada

        senha = senha_digitada

        saldo = carregar_saldo(
            conta
        )

        tela_menu()

    tk.Button(

        painel,

        text="ENTRAR  →",

        command=entrar,

        font=(
            "Arial",
            11,
            "bold"
        ),

        fg=FUNDO,

        bg=VERDE,

        activebackground=VERDE_ESCuro,

        activeforeground=FUNDO,

        relief="flat",

        cursor="hand2",

        width=34,

        height=2

    ).pack()

    tk.Label(

        centro,

        text="SIMULADOR BANCÁRIO • SENAI",

        font=(
            "Arial",
            8
        ),

        fg=CINZA,

        bg=FUNDO

    ).pack(
        pady=18
    )


# ==========================================
# MENU
# ==========================================

def tela_menu():

    limpar_tela()

    # ===============================
    # BARRA SUPERIOR
    # ===============================

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
            "Arial",
            24,
            "bold"
        ),

        fg=VERDE,

        bg=PAINEL

    ).pack(
        side="left",
        padx=30,
        pady=20
    )

    tk.Label(

        topo,

        text="CAIXA ELETRÔNICO",

        font=(
            "Arial",
            12,
            "bold"
        ),

        fg=BRANCO,

        bg=PAINEL

    ).pack(
        side="left"
    )

    tk.Label(

        topo,

        text=f"CONTA  •  {conta}",

        font=(
            "Arial",
            10,
            "bold"
        ),

        fg=CINZA,

        bg=PAINEL

    ).pack(
        side="right",
        padx=30
    )

    # ===============================
    # CONTEÚDO
    # ===============================

    conteudo = tk.Frame(
        janela,
        bg=FUNDO
    )

    conteudo.pack(
        fill="both",
        expand=True,
        padx=35,
        pady=30
    )

    # ===============================
    # LADO ESQUERDO
    # ===============================

    esquerda = tk.Frame(
        conteudo,
        bg=FUNDO
    )

    esquerda.pack(
        side="left",
        fill="both",
        expand=True,
        padx=(0, 20)
    )

    tk.Label(

        esquerda,

        text="VISÃO GERAL",

        font=(
            "Arial",
            10,
            "bold"
        ),

        fg=CINZA,

        bg=FUNDO

    ).pack(
        anchor="w"
    )

    # Cartão de saldo
    cartao = tk.Frame(

        esquerda,

        bg=PAINEL,

        padx=30,

        pady=25,

        highlightbackground=BORDA,

        highlightthickness=1

    )

    cartao.pack(
        fill="x",
        pady=(10, 20)
    )

    tk.Label(

        cartao,

        text="SALDO DISPONÍVEL",

        font=(
            "Arial",
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
            "Arial",
            30,
            "bold"
        ),

        fg=VERDE,

        bg=PAINEL

    ).pack(
        anchor="w",
        pady=5
    )

    tk.Label(

        cartao,

        text="Saldo atualizado",

        font=(
            "Arial",
            9
        ),

        fg=CINZA,

        bg=PAINEL

    ).pack(
        anchor="w"
    )

    # Informação da conta
    informacao = tk.Frame(

        esquerda,

        bg=PAINEL,

        padx=25,

        pady=20

    )

    informacao.pack(
        fill="x"
    )

    tk.Label(

        informacao,

        text="STATUS DA CONTA",

        font=(
            "Arial",
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

        text="●  CONTA ATIVA",

        font=(
            "Arial",
            11,
            "bold"
        ),

        fg=VERDE,

        bg=PAINEL

    ).pack(
        anchor="w",
        pady=(8, 0)
    )

    # ===============================
    # LADO DIREITO
    # ===============================

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

        text="OPERAÇÕES",

        font=(
            "Arial",
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
        "CONSULTAR SALDO",
        consultar_saldo
    ).pack(
        pady=(10, 7),
        fill="x"
    )

    botao_menu(
        direita,
        "SACAR DINHEIRO",
        sacar
    ).pack(
        pady=7,
        fill="x"
    )

    botao_menu(
        direita,
        "DEPOSITAR",
        depositar
    ).pack(
        pady=7,
        fill="x"
    )

    tk.Frame(
        direita,
        bg=BORDA,
        height=1
    ).pack(
        fill="x",
        pady=18
    )

    botao_menu(
        direita,
        "ENCERRAR SESSÃO",
        sair,
        VERMELHO
    ).pack(
        pady=7,
        fill="x"
    )

    # Rodapé
    tk.Label(

        janela,

        text="Sistema de simulação bancária • SENAI",

        font=(
            "Arial",
            8
        ),

        fg=CINZA,

        bg=FUNDO

    ).pack(
        pady=(0, 12)
    )


# ==========================================
# CONSULTAR SALDO
# ==========================================

def consultar_saldo():

    messagebox.showinfo(

        "Saldo disponível",

        f"SALDO ATUAL\n\n"
        f"R$ {saldo},00"

    )


# ==========================================
# SAQUE
# ==========================================

def sacar():

    global saldo

    valor = simpledialog.askinteger(

        "Saque",

        "Digite o valor que deseja sacar:",

        parent=janela,

        minvalue=1

    )

    if valor is None:
        return

    if valor > saldo:

        messagebox.showerror(

            "Saldo insuficiente",

            "O valor solicitado é maior que "
            "o saldo disponível."

        )

        return

    cedulas = calcular_cedulas(
        valor
    )

    if cedulas is None:

        messagebox.showerror(

            "Valor indisponível",

            "Não é possível formar esse valor "
            "com as cédulas disponíveis.\n\n"

            "Cédulas:\n"
            "R$ 100 • R$ 50 • R$ 20\n"
            "R$ 10 • R$ 5 • R$ 2"

        )

        return

    saldo -= valor

    texto = (
        "SAQUE REALIZADO!\n\n"
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
        "Saque",
        texto
    )

    tela_menu()


# ==========================================
# DEPÓSITO
# ==========================================

def depositar():

    global saldo

    valor = simpledialog.askinteger(

        "Depósito",

        "Digite o valor que deseja depositar:",

        parent=janela,

        minvalue=1

    )

    if valor is None:
        return

    saldo += valor

    messagebox.showinfo(

        "Depósito realizado",

        "DEPÓSITO CONCLUÍDO!\n\n"

        f"Valor depositado: R$ {valor},00\n\n"

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

        "Encerrar sessão",

        "O saldo foi salvo com sucesso.\n\n"
        "Deseja realmente encerrar o programa?"

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

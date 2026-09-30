import os
import tkinter as tk
from tkinter import messagebox, simpledialog


ARQUIVO = "contas.txt"
SALDO_INICIAL = 1000


def carregar_saldo(conta):
    """Busca o saldo da conta no arquivo."""
    if not os.path.exists(ARQUIVO):
        return SALDO_INICIAL

    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(";")

            if len(dados) == 2 and dados[0] == conta:
                return int(dados[1])

    return SALDO_INICIAL


def salvar_saldo(conta, saldo):
    """Salva ou atualiza o saldo da conta."""
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
            arquivo.write(f"{numero_conta};{valor}\n")


def calcular_cedulas(valor):
    """Calcula as cédulas necessárias para o saque."""
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
    """Monta o texto mostrando as cédulas."""
    texto = "Cédulas entregues:\n\n"

    for valor, quantidade in cedulas.items():

        if quantidade == 1:
            texto += f"1 cédula de R$ {valor}\n"
        else:
            texto += f"{quantidade} cédulas de R$ {valor}\n"

    return texto


# --------------------------------------------------
# INTERFACE
# --------------------------------------------------

janela = tk.Tk()
janela.title("Caixa Eletrônico")
janela.geometry("500x500")
janela.resizable(False, False)

conta = ""
senha = ""
saldo = 0


def limpar_tela():
    """Apaga todos os componentes da tela."""
    for widget in janela.winfo_children():
        widget.destroy()


def tela_login():
    """Mostra a tela de login."""
    limpar_tela()

    titulo = tk.Label(
        janela,
        text="CAIXA ELETRÔNICO",
        font=("Arial", 24, "bold")
    )
    titulo.pack(pady=30)

    subtitulo = tk.Label(
        janela,
        text="Informe seus dados para acessar",
        font=("Arial", 12)
    )
    subtitulo.pack(pady=5)

    tk.Label(
        janela,
        text="Número da conta:"
    ).pack(pady=(30, 5))

    entrada_conta = tk.Entry(
        janela,
        width=30
    )
    entrada_conta.pack()

    tk.Label(
        janela,
        text="Senha:"
    ).pack(pady=(20, 5))

    entrada_senha = tk.Entry(
        janela,
        width=30,
        show="*"
    )
    entrada_senha.pack()

    def entrar():
        global conta, senha, saldo

        conta_digitada = entrada_conta.get().strip()
        senha_digitada = entrada_senha.get().strip()

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

        saldo = carregar_saldo(conta)

        tela_menu()

    botao = tk.Button(
        janela,
        text="ENTRAR",
        width=20,
        command=entrar
    )
    botao.pack(pady=30)


def tela_menu():
    """Mostra o menu principal."""
    limpar_tela()

    tk.Label(
        janela,
        text="CAIXA ELETRÔNICO",
        font=("Arial", 22, "bold")
    ).pack(pady=25)

    tk.Label(
        janela,
        text=f"Conta: {conta}",
        font=("Arial", 12)
    ).pack(pady=5)

    tk.Label(
        janela,
        text="Escolha uma opção",
        font=("Arial", 14)
    ).pack(pady=20)

    tk.Button(
        janela,
        text="CONSULTAR SALDO",
        width=25,
        height=2,
        command=consultar_saldo
    ).pack(pady=5)

    tk.Button(
        janela,
        text="SACAR",
        width=25,
        height=2,
        command=sacar
    ).pack(pady=5)

    tk.Button(
        janela,
        text="DEPOSITAR",
        width=25,
        height=2,
        command=depositar
    ).pack(pady=5)

    tk.Button(
        janela,
        text="SAIR",
        width=25,
        height=2,
        command=sair
    ).pack(pady=20)


def consultar_saldo():
    """Mostra o saldo atual."""
    messagebox.showinfo(
        "Saldo",
        f"Seu saldo atual é:\n\nR$ {saldo},00"
    )


def sacar():
    """Realiza um saque."""
    global saldo

    valor = simpledialog.askinteger(
        "Saque",
        "Digite o valor para saque:",
        parent=janela,
        minvalue=1
    )

    if valor is None:
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
            "O caixa não possui cédulas para formar esse valor.\n\n"
            "Cédulas disponíveis:\n"
            "R$ 100, R$ 50, R$ 20, R$ 10, R$ 5 e R$ 2."
        )
        return

    saldo -= valor

    texto = mostrar_cedulas(cedulas)

    texto += f"\nSaldo atual: R$ {saldo},00"

    messagebox.showinfo(
        "Saque realizado",
        texto
    )


def depositar():
    """Realiza um depósito."""
    global saldo

    valor = simpledialog.askinteger(
        "Depósito",
        "Digite o valor para depósito:",
        parent=janela,
        minvalue=1
    )

    if valor is None:
        return

    saldo += valor

    messagebox.showinfo(
        "Depósito realizado",
        f"Depósito realizado com sucesso!\n\n"
        f"Saldo atual: R$ {saldo},00"
    )


def sair():
    """Salva o saldo e volta para a tela de login."""
    salvar_saldo(conta, saldo)

    resposta = messagebox.askyesno(
        "Sair",
        "Saldo salvo com sucesso.\n\n"
        "Deseja fechar o programa?"
    )

    if resposta:
        janela.destroy()
    else:
        tela_login()


tela_login()

janela.mainloop()
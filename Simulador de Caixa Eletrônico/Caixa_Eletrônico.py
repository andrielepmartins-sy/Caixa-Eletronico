
# Importa as bibliotecas utilizadas
import tkinter as tk
from tkinter import messagebox
import os
from datetime import datetime

# Arquivos para salvar os dados
arquivo = "contas.txt"
arquivo_extrato = "extrato.txt"

# Saldo inicial de contas novas
saldo = 1000

# Conta que está sendo utilizada
conta = ""

# Cédulas disponíveis no caixa
cedulas = [100, 50, 20, 10, 5, 2]

# Cores da interface
fundo = "#F2F2F2"
azul = "#4A83B8"
azul_claro = "#D9E6F2"
texto_cor = "#263746"
verde = "#26734D"

# Lista de contas cadastradas
contas = {}


# ==========================================
# CARREGAR AS CONTAS DO ARQUIVO
# ==========================================

def carregar_contas():
    global contas

    contas = {}

    if os.path.exists(arquivo):
        with open(arquivo, "r", encoding="utf-8") as f:
            for linha in f:
                dados = linha.strip().split(";")

                if len(dados) == 3:
                    numero = dados[0]
                    senha = dados[1]

                    try:
                        valor = int(dados[2])

                        contas[numero] = {
                            "senha": senha,
                            "saldo": valor
                        }
                    except ValueError:
                        continue


# ==========================================
# SALVAR AS CONTAS NO ARQUIVO
# ==========================================

def salvar_saldo():
    # Atualiza o saldo da conta atual
    if conta in contas:
        contas[conta]["saldo"] = saldo

    # Salva todas as contas cadastradas
    with open(arquivo, "w", encoding="utf-8") as f:
        for numero, dados in contas.items():
            f.write(
                numero + ";"
                + dados["senha"] + ";"
                + str(dados["saldo"]) + "\n"
            )


# ==========================================
# REGISTRAR UMA OPERAÇÃO NO EXTRATO
# ==========================================

def registrar_operacao(tipo, valor, detalhes=""):
    data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    with open(arquivo_extrato, "a", encoding="utf-8") as f:
        f.write(
            conta + ";"
            + data + ";"
            + tipo + ";"
            + str(valor) + ";"
            + detalhes.replace(";", ",").replace("\n", " ")
            + "\n"
        )


# ==========================================
# FORMATAR VALORES EM REAIS
# ==========================================

def formatar_dinheiro(valor):
    texto = f"{valor:,.2f}"
    texto = texto.replace(",", "X")
    texto = texto.replace(".", ",")
    texto = texto.replace("X", ".")

    return "R$ " + texto


# ==========================================
# FUNÇÕES PARA CRIAR ELEMENTOS DA INTERFACE
# ==========================================

def criar_titulo(texto, tamanho=14):
    return tk.Label(
        janela,
        text=texto,
        font=("Arial", tamanho, "bold"),
        bg=fundo,
        fg=texto_cor
    )


def criar_botao(texto, comando):
    return tk.Button(
        janela,
        text=texto,
        command=comando,
        font=("Arial", 10),
        bg=azul_claro,
        fg=texto_cor,
        activebackground="#B8D0E5",
        width=25,
        relief="flat",
        cursor="hand2",
        pady=6
    )


# ==========================================
# FUNÇÃO PARA LIMPAR A TELA
# ==========================================

def limpar():
    for item in janela.winfo_children():
        item.destroy()


# ==========================================
# ENTRAR NO SISTEMA
# ==========================================

def entrar():
    global conta, saldo

    numero = campo_conta.get().strip()
    senha = campo_senha.get()

    # Verifica se os campos estão preenchidos
    if numero == "" or senha == "":
        messagebox.showerror(
            "Erro",
            "Preencha a conta e a senha."
        )
        return

    # Verifica se o número da conta contém apenas números
    if not numero.isdigit():
        messagebox.showerror(
            "Erro",
            "O número da conta deve conter apenas números."
        )
        return

    # Atualiza a lista de contas
    carregar_contas()

    # Verifica se a conta já existe
    if numero in contas:
        if contas[numero]["senha"] != senha:
            messagebox.showerror(
                "Erro",
                "Senha incorreta."
            )
            return

        # Recupera o saldo salvo
        conta = numero
        saldo = contas[conta]["saldo"]

    else:
        # Cria uma conta nova
        conta = numero
        saldo = 1000

        contas[conta] = {
            "senha": senha,
            "saldo": saldo
        }

        salvar_saldo()

        registrar_operacao(
            "Conta criada",
            1000,
            "Saldo inicial"
        )

        messagebox.showinfo(
            "Conta criada",
            "Sua conta foi criada com saldo inicial de R$ 1.000,00."
        )

    # Abre o menu principal
    menu()


# ==========================================
# CONSULTAR SALDO
# ==========================================

def consultar():
    messagebox.showinfo(
        "Consulta de saldo",
        "Conta: " + conta
        + "\nSaldo disponível: "
        + formatar_dinheiro(saldo)
    )


# ==========================================
# TELA DE DEPÓSITO
# ==========================================

def tela_deposito():
    limpar()

    criar_titulo("Depósito", 16).pack(pady=(25, 10))

    tk.Label(
        janela,
        text="Digite o valor que deseja depositar:",
        bg=fundo,
        fg=texto_cor
    ).pack(pady=5)

    campo_valor = tk.Entry(
        janela,
        font=("Arial", 12),
        width=25,
        justify="center"
    )
    campo_valor.pack(pady=10, ipady=4)
    campo_valor.focus_set()

    def confirmar():
        global saldo

        texto = campo_valor.get().strip()

        # Aceita apenas números inteiros positivos
        if not texto.isdigit():
            messagebox.showerror(
                "Erro",
                "Digite um valor inteiro positivo."
            )
            return

        valor = int(texto)

        if valor <= 0:
            messagebox.showerror(
                "Erro",
                "O valor deve ser maior que zero."
            )
            return

        # Adiciona o valor ao saldo
        saldo += valor

        salvar_saldo()
        registrar_operacao("Depósito", valor)

        messagebox.showinfo(
            "Depósito realizado",
            "Valor depositado: " + formatar_dinheiro(valor)
            + "\nNovo saldo: " + formatar_dinheiro(saldo)
        )

        menu()

    criar_botao(
        "Confirmar depósito",
        confirmar
    ).pack(pady=8)

    criar_botao(
        "Voltar ao menu",
        menu
    ).pack(pady=5)


# ==========================================
# CALCULAR AS CÉDULAS DO SAQUE
# ==========================================

def calcular_cedulas(valor):
    # Guarda a menor quantidade de cédulas para cada valor
    melhor = [None] * (valor + 1)

    # Guarda a cédula utilizada em cada etapa
    anterior = [None] * (valor + 1)

    melhor[0] = 0

    # Procura uma combinação para formar o valor
    for quantia in range(1, valor + 1):
        for cedula in cedulas:

            if quantia >= cedula:
                anterior_valor = melhor[quantia - cedula]

                if anterior_valor is not None:
                    tentativa = anterior_valor + 1

                    if (
                        melhor[quantia] is None
                        or tentativa < melhor[quantia]
                    ):
                        melhor[quantia] = tentativa
                        anterior[quantia] = cedula

    # Verifica se foi encontrada uma combinação
    if melhor[valor] is None:
        return None

    # Monta a lista de cédulas utilizadas
    resultado = {}
    restante = valor

    while restante > 0:
        cedula = anterior[restante]

        resultado[cedula] = resultado.get(cedula, 0) + 1
        restante -= cedula

    return resultado


# ==========================================
# TELA DE SAQUE
# ==========================================

def tela_saque():
    limpar()

    criar_titulo("Saque", 16).pack(pady=(25, 10))

    tk.Label(
        janela,
        text="Saldo disponível: " + formatar_dinheiro(saldo),
        bg=fundo,
        fg=verde,
        font=("Arial", 11, "bold")
    ).pack(pady=5)

    tk.Label(
        janela,
        text="Digite o valor que deseja sacar:",
        bg=fundo,
        fg=texto_cor
    ).pack(pady=5)

    campo_valor = tk.Entry(
        janela,
        font=("Arial", 12),
        width=25,
        justify="center"
    )
    campo_valor.pack(pady=10, ipady=4)
    campo_valor.focus_set()

    def confirmar():
        global saldo

        texto = campo_valor.get().strip()

        if not texto.isdigit():
            messagebox.showerror(
                "Erro",
                "Digite um valor inteiro positivo."
            )
            return

        valor = int(texto)

        if valor <= 0:
            messagebox.showerror(
                "Erro",
                "O valor deve ser maior que zero."
            )
            return

        if valor > saldo:
            messagebox.showerror(
                "Erro",
                "Você não possui saldo suficiente."
            )
            return

        # Evita cálculos muito grandes
        if valor > 100000:
            messagebox.showerror(
                "Erro",
                "Digite um valor de até R$ 100.000."
            )
            return

        # Calcula a combinação de cédulas
        resultado = calcular_cedulas(valor)

        if resultado is None:
            messagebox.showerror(
                "Saque impossível",
                "Não é possível formar esse valor "
                "com as cédulas disponíveis."
            )
            return

        # Monta o texto com as cédulas
        mensagem = ""

        for cedula in sorted(resultado, reverse=True):
            quantidade = resultado[cedula]

            mensagem += (
                str(quantidade)
                + " cédula(s) de R$ "
                + str(cedula)
                + "\n"
            )

        # Confirma o saque antes de descontar o saldo
        confirmar_saque = messagebox.askyesno(
            "Confirmar saque",
            "Valor: " + formatar_dinheiro(valor)
            + "\n\nCédulas:\n" + mensagem
            + "\nDeseja continuar?"
        )

        if not confirmar_saque:
            return

        # Desconta o valor do saldo
        saldo -= valor

        salvar_saldo()
        registrar_operacao("Saque", valor, mensagem)

        messagebox.showinfo(
            "Saque realizado",
            mensagem
            + "\nSaldo atual: " + formatar_dinheiro(saldo)
        )

        menu()

    criar_botao(
        "Confirmar saque",
        confirmar
    ).pack(pady=8)

    criar_botao(
        "Voltar ao menu",
        menu
    ).pack(pady=5)


# ==========================================
# CONSULTAR O EXTRATO
# ==========================================

def tela_extrato():
    limpar()

    criar_titulo("Extrato bancário", 16).pack(pady=(20, 10))

    tk.Label(
        janela,
        text="Conta: " + conta,
        bg=fundo,
        fg=texto_cor
    ).pack(pady=3)

    tk.Label(
        janela,
        text="Saldo atual: " + formatar_dinheiro(saldo),
        bg=fundo,
        fg=verde,
        font=("Arial", 11, "bold")
    ).pack(pady=3)

    # Cria a área que mostra as movimentações
    quadro = tk.Frame(janela, bg=fundo)
    quadro.pack(fill="both", expand=True, padx=15, pady=10)

    lista = tk.Listbox(
        quadro,
        font=("Arial", 9),
        height=12,
        width=55
    )
    lista.pack(side="left", fill="both", expand=True)

    rolagem = tk.Scrollbar(
        quadro,
        command=lista.yview
    )
    rolagem.pack(side="right", fill="y")

    lista.config(yscrollcommand=rolagem.set)

    # Procura as movimentações da conta atual
    if os.path.exists(arquivo_extrato):
        with open(
            arquivo_extrato,
            "r",
            encoding="utf-8"
        ) as f:

            for linha in f:
                dados = linha.strip().split(";", 4)

                if len(dados) >= 4 and dados[0] == conta:
                    data = dados[1]
                    tipo = dados[2]
                    valor = int(dados[3])

                    texto = (
                        data + " | "
                        + tipo + " | "
                        + formatar_dinheiro(valor)
                    )

                    lista.insert(tk.END, texto)

                    if len(dados) == 5 and dados[4]:
                        lista.insert(
                            tk.END,
                            "   " + dados[4]
                        )

    criar_botao(
        "Voltar ao menu",
        menu
    ).pack(pady=(0, 15))


# ==========================================
# MOSTRAR O MENU PRINCIPAL
# ==========================================

def menu():
    limpar()

    criar_titulo("CAIXA ELETRÔNICO", 18).pack(pady=(25, 8))

    tk.Label(
        janela,
        text="Bem-vindo! Conta: " + conta,
        font=("Arial", 10),
        bg=fundo,
        fg="#555555"
    ).pack()

    tk.Label(
        janela,
        text="Saldo disponível",
        font=("Arial", 10),
        bg=fundo,
        fg=texto_cor
    ).pack(pady=(18, 3))

    tk.Label(
        janela,
        text=formatar_dinheiro(saldo),
        font=("Arial", 17, "bold"),
        bg=fundo,
        fg=verde
    ).pack(pady=(0, 15))

    criar_botao(
        "1 - Consultar saldo",
        consultar
    ).pack(pady=5)

    criar_botao(
        "2 - Sacar dinheiro",
        tela_saque
    ).pack(pady=5)

    criar_botao(
        "3 - Depositar dinheiro",
        tela_deposito
    ).pack(pady=5)

    criar_botao(
        "4 - Extrato bancário",
        tela_extrato
    ).pack(pady=5)

    criar_botao(
        "5 - Sair",
        sair
    ).pack(pady=(12, 5))


# ==========================================
# SALVAR E ENCERRAR O PROGRAMA
# ==========================================

def sair():
    salvar_saldo()

    messagebox.showinfo(
        "Caixa eletrônico",
        "Dados salvos!\nObrigado por utilizar o sistema."
    )

    janela.destroy()


# ==========================================
# CRIAR A JANELA PRINCIPAL
# ==========================================

janela = tk.Tk()
janela.title("Caixa Eletrônico")
janela.geometry("450x500")
janela.configure(bg=fundo)
janela.resizable(False, False)

# Carrega as contas que já foram salvas
carregar_contas()


# ==========================================
# TELA DE LOGIN
# ==========================================

criar_titulo("Bem-vindo!", 18).pack(pady=(35, 5))

tk.Label(
    janela,
    text="Caixa Eletrônico",
    font=("Arial", 11),
    bg=fundo,
    fg="#555555"
).pack(pady=(0, 20))

# Campo para digitar a conta
tk.Label(
    janela,
    text="Número da conta",
    bg=fundo,
    fg=texto_cor
).pack()

campo_conta = tk.Entry(
    janela,
    font=("Arial", 11),
    width=28,
    justify="center"
)
campo_conta.pack(pady=(5, 12), ipady=4)

# Campo para digitar a senha
tk.Label(
    janela,
    text="Senha",
    bg=fundo,
    fg=texto_cor
).pack()

campo_senha = tk.Entry(
    janela,
    font=("Arial", 11),
    width=28,
    show="*",
    justify="center"
)
campo_senha.pack(pady=(5, 18), ipady=4)

# Botão para entrar no sistema
tk.Button(
    janela,
    text="Entrar",
    command=entrar,
    font=("Arial", 11, "bold"),
    bg=azul,
    fg="white",
    activebackground="#356895",
    activeforeground="white",
    width=22,
    relief="flat",
    cursor="hand2",
    pady=7
).pack()

# Permite apertar Enter para entrar
janela.bind("<Return>", lambda evento: entrar())

# Mantém a janela aberta
janela.mainloop()

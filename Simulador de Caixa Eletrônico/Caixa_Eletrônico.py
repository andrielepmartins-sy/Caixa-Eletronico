import tkinter as tk
from tkinter import messagebox
import os

# Nome do arquivo que vai guardar as contas e os saldos
ARQUIVO = "contas.txt"

# Toda conta nova começa com mil reais
SALDO_INICIAL = 1000

# Notas que o caixa consegue entregar
CEDULAS = [100, 50, 20, 10, 5, 2]


# Cores usadas nas telas do programa
FUNDO = "#0D0914"
CARD = "#171020"
CARD_2 = "#21152E"

ROXO = "#9B5DE5"
ROXO_CLARO = "#B87CFF"
ROXO_ESCURO = "#6A35A8"

BRANCO = "#F5F0FA"
CINZA = "#9B91A8"
VERMELHO = "#FF5577"


# Guarda os dados da conta que está sendo usada
conta_atual = ""
saldo = 0


# Procura o saldo da conta no arquivo
def carregar_saldo(conta):

    # Se o arquivo ainda não existe, usa o saldo inicial
    if not os.path.exists(ARQUIVO):
        return SALDO_INICIAL

    arquivo = open(ARQUIVO, "r", encoding="utf-8")

    for linha in arquivo:
        linha = linha.strip()

        if linha != "":
            dados = linha.split(";")

            # Confere se a conta da linha é a mesma que foi digitada
            if len(dados) == 2 and dados[0] == conta:
                arquivo.close()
                return int(dados[1])

    arquivo.close()

    # Se a conta não estiver salva, começa com mil reais
    return SALDO_INICIAL


# Salva o saldo atualizado sem apagar as outras contas
def salvar_saldo(conta, novo_saldo):

    contas = []

    # Se já existe um arquivo, lê as contas que estão salvas
    if os.path.exists(ARQUIVO):
        arquivo = open(ARQUIVO, "r", encoding="utf-8")

        for linha in arquivo:
            linha = linha.strip()

            if linha != "":
                dados = linha.split(";")

                if len(dados) == 2:

                    # Atualiza o saldo da conta que está sendo usada
                    if dados[0] == conta:
                        contas.append(
                            conta + ";" + str(novo_saldo)
                        )
                    else:
                        # Mantém os dados das outras contas
                        contas.append(
                            dados[0] + ";" + dados[1]
                        )

        arquivo.close()

    # Verifica se a conta já estava salva
    conta_encontrada = False

    for linha in contas:
        dados = linha.split(";")

        if dados[0] == conta:
            conta_encontrada = True
            break

    # Se for uma conta nova, adiciona ela ao arquivo
    if not conta_encontrada:
        contas.append(
            conta + ";" + str(novo_saldo)
        )

    # Escreve os dados atualizados no arquivo
    arquivo = open(ARQUIVO, "w", encoding="utf-8")

    for linha in contas:
        arquivo.write(linha + "\n")

    arquivo.close()


# Calcula quantas notas serão usadas no saque
def calcular_cedulas(valor):

    cedulas_entregues = {}

    valor_restante = valor

    indice = 0

    # Vai testando as notas da maior para a menor
    while valor_restante > 0 and indice < len(CEDULAS):

        cedula = CEDULAS[indice]

        # Descobre quantas notas desse valor podem ser usadas
        quantidade = valor_restante // cedula

        if quantidade > 0:

            cedulas_entregues[cedula] = quantidade

            # Atualiza o valor que ainda falta entregar
            valor_restante = valor_restante % cedula

        indice += 1

    # Se sobrar algum valor, não dá para fazer esse saque
    if valor_restante != 0:
        return None

    return cedulas_entregues


# Apaga os elementos da tela antes de abrir outra
def limpar_tela():

    for widget in janela.winfo_children():
        widget.destroy()


# Cria os botões com o mesmo estilo
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


# Cria os campos onde o usuário digita as informações
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


# Pega os dados digitados e abre a conta
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

    # A senha só é solicitada, não precisa ser conferida
    conta_atual = conta

    # Carrega o saldo que já estiver salvo para essa conta
    saldo = carregar_saldo(conta_atual)

    tela_menu()


# Monta a primeira tela do sistema
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


# Mostra as opções disponíveis depois do login
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


# Cria os cards das opções do menu
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


# Mostra o saldo da conta em uma janela
def consultar_saldo():

    messagebox.showinfo(
        "Saldo",
        "Conta: " + conta_atual +
        "\n\nSaldo atual:\nR$ {:.2f}".format(
            saldo
        ).replace(".", ",")
    )


# Monta a tela para digitar o valor do saque
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


# Confere o valor e faz o saque
def sacar():

    global saldo

    valor_texto = entrada_saque.get().strip()

    if valor_texto == "":
        messagebox.showerror(
            "Erro",
            "Digite o valor do saque."
        )
        return

    # Não aceita valores com casas decimais
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

    # Confere se tem dinheiro suficiente na conta
    if valor > saldo:
        messagebox.showerror(
            "Erro",
            "Saldo insuficiente."
        )
        return

    # Confere se o caixa consegue entregar esse valor
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

    # Monta a lista das notas que serão entregues
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

    # Desconta o valor retirado do saldo
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


# Monta a tela para fazer um depósito
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


# Confere o valor e adiciona o depósito ao saldo
def depositar():

    global saldo

    valor_texto = entrada_deposito.get().strip()

    if valor_texto == "":
        messagebox.showerror(
            "Erro",
            "Digite o valor do depósito."
        )
        return

    # Impede que sejam digitados valores fracionários
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

    # Soma o depósito ao saldo atual
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


# Salva o saldo e fecha o sistema
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


# Cria a janela principal do programa
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

# Abre o login e mantém a janela funcionando
tela_login()

janela.mainloop()
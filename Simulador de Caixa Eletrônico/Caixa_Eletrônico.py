import os

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

    # Se a conta ainda não existe, começa com R$ 1.000,00
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


def pausar():
    input("\nPressione ENTER para retornar ao menu...")


def ler_valor(mensagem):
    """Lê somente valores inteiros e impede valores negativos."""
    valor = input(mensagem).strip()

    if valor == "":
        print("Erro: digite um valor.")
        return None

    # Impede valores como 250.75
    if not valor.isdigit():
        print("Erro: valores fracionários ou inválidos não são aceitos.")
        print("Digite um valor inteiro, sem ponto ou vírgula.")
        return None

    valor = int(valor)

    if valor < 0:
        print("Erro: valores negativos não são permitidos.")
        return None

    return valor


def calcular_cedulas(valor):
    """Calcula a quantidade de cada cédula necessária para o saque."""
    cedulas = [100, 50, 20, 10, 5, 2]
    resultado = {}

    restante = valor

    for cedula in cedulas:
        quantidade = restante // cedula
        restante = restante % cedula

        if quantidade > 0:
            resultado[cedula] = quantidade

    # Se sobrou algum valor, o caixa não consegue montar o saque.
    if restante != 0:
        return None

    return resultado


def mostrar_cedulas(cedulas):
    print("\nEntregar:")

    for valor, quantidade in cedulas.items():
        if quantidade == 1:
            print(f"1 cédula de R${valor}")
        else:
            print(f"{quantidade} cédulas de R${valor}")


def main():
    print("=" * 40)
    print("      BEM-VINDO AO CAIXA ELETRÔNICO")
    print("=" * 40)

    conta = input("Digite sua conta: ").strip()
    senha = input("Digite sua senha: ").strip()

    # A senha é apenas solicitada, conforme o enunciado.
    saldo = carregar_saldo(conta)

    print("\nAcesso realizado com sucesso!")

    while True:
        print("\n" + "=" * 40)
        print("MENU")
        print("1 - Consultar saldo")
        print("2 - Sacar")
        print("3 - Depositar")
        print("4 - Sair")
        print("=" * 40)

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            print(f"\nSeu saldo atual é: R$ {saldo},00")
            pausar()

        elif opcao == "2":
            valor = ler_valor("\nDigite o valor para saque: R$ ")

            if valor is None:
                pausar()
                continue

            if valor == 0:
                print("Erro: o valor do saque deve ser maior que zero.")
                pausar()
                continue

            if valor > saldo:
                print("Erro: saldo insuficiente.")
                pausar()
                continue

            cedulas = calcular_cedulas(valor)

            if cedulas is None:
                print("Erro: o caixa não possui cédulas para formar esse valor.")
                print("Cédulas disponíveis: R$100, R$50, R$20, R$10, R$5 e R$2.")
                pausar()
                continue

            saldo -= valor

            print("\nSaque realizado com sucesso.")
            mostrar_cedulas(cedulas)
            print(f"Saldo atual: R$ {saldo},00")
            pausar()

        elif opcao == "3":
            valor = ler_valor("\nDigite o valor para depósito: R$ ")

            if valor is None:
                pausar()
                continue

            if valor == 0:
                print("Erro: o valor do depósito deve ser maior que zero.")
                pausar()
                continue

            saldo += valor

            print("Depósito realizado com sucesso!")
            print(f"Saldo atual: R$ {saldo},00")
            pausar()

        elif opcao == "4":
            salvar_saldo(conta, saldo)

            print("\n" + "=" * 40)
            print("Obrigado por usar nosso sistema!")
            print("Saldo salvo com sucesso.")
            print("Retornando para a tela de conta e senha.")
            print("=" * 40)

            break

        else:
            print("\nOpção inválida!")
            print("Por favor, escolha uma opção de 1 a 4.")
            pausar()


if __name__ == "__main__":
    main()
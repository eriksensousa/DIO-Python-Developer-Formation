menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
        valor = float(input("Valor do Deposito: "))

        if (valor > 0 and valor <= 500):
            saldo += valor
            extrato += f'Déposito: R$ {valor:.2f}\n'
        else:
            print('O valor informado é invalido')

    elif opcao == 's':
        valor = float(input("Valor do Saque: "))

        if (valor > 0 and valor < saldo and numero_saques < LIMITE_SAQUES):
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saques += 1
        else:
            print('O valor informado é invalido ou voce atingiu seu limite de saques')

    elif opcao == "e":
        print(extrato)

    elif opcao == "q":
        print("Operações realizadas")
        break

    else:
        print("Não foi identificada sua operação!!")

menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """
saldo = 0.0
lancamentos = []
qtde_saques_dia = 0
LIMITE_SAQUE_DIARIO = 3
LIMITE_MAX_SAQUE = 500.0

def depositar(valor, saldo):
    saldo = saldo + valor
    lancamentos.append(valor)
    print(f"Deposito de {valor} realizado com sucesso e o seu saldo atual é R$ {saldo}")
    return saldo

def sacar (valor, saldo, qtde_saques_dia):
    valor = valor
    saldo = saldo
    qtde_saques_dia = qtde_saques_dia
    if valor > saldo:
        print("Valor supera o saldo disponível em conta. Peça um extrato pra verificar o saldo.")

    elif qtde_saques_dia < 3:
        if valor <= 500:
            saldo = saldo - valor
            valor = valor * -1
            print(valor)
            lancamentos.append(valor)
            qtde_saques_dia += 1
        else:
            print("O valor máximo para saque é R$ 500,00")
    else:
        print("Limite de saque diário ultrapassado...")
    return float(saldo), int(qtde_saques_dia)

def exibir_extrato(lancamentos):
    if len(lancamentos) == 0: print("Sem Lançamentos no extrato.")
    for lancamento in lancamentos:
        if lancamento > 0 : print(f"Depósito de R$ {lancamento}")
        if lancamento < 0 : print(f"Saque de R$ {lancamento}")
    print(f"Saldo em conta corrente: {saldo}")
        
        
opcao_menu = 10
while opcao_menu !=0:
    print(menu)
    opcao_menu = int(input("Digite a opcao desejada: "))
    if opcao_menu == 1:
        valor = float(input("Digite o valor do deposito: "))
        saldo = depositar(valor, saldo)
    if opcao_menu == 2:
        valor = float(input("Digite o valor do saque: "))
        saldo, qtde_saques_dia = sacar(valor, saldo, qtde_saques_dia)
    if opcao_menu == 3:
        exibir_extrato(lancamentos)
    if opcao_menu == 0:
        break









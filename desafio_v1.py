menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Cadastrar Conta
[5] Listar Contas
[6] Cadastrar Usuário
[0] Sair

=> """
saldo = 0.0
lancamentos = []
qtde_saques_dia = 0
LIMITE_SAQUE_DIARIO = 3
LIMITE_MAX_SAQUE = 500.0
usuarios = []
contas_sequencial = 0
contas = []

def cadastrar_conta(contas, usuarios):
    global contas_sequencial
    cpf = input("Digite o cpf: ")
    if not is_usuario_cadastrado(cpf, usuarios):
        print("Usuario não cadastrado")
    else:
        contas_sequencial += 1
        contas.append({"cpf": cpf, "agencia": "0001", "conta": contas_sequencial})
        print("Conta cadastrada com sucesso")
        
def listar_contas(contas):
    for conta in contas:
        print(f"CPF: {conta['cpf']} -- Agência: {conta['agencia']} -- Conta: {conta['conta']}")
    
def cadastrar_usuario(usuarios):
    cpf = input("Digite o numero do cpf: ")
    if not is_usuario_cadastrado(cpf, usuarios):    
        nome = input("Nome: ")
        data_nascimento = input("Nascimento: ")
        endereco = input("Endereco (logradouro, num, bairro - cidade / estado): ")
        usuarios.append({"nome": nome, "data_nascimento":data_nascimento, "cpf": cpf, "endereço": endereco})
        print("Usuário Cadastrado com sucesso")

def listar_usuarios(usuarios):
    for usuario in usuarios:
        print(usuario['cpf'])
        
#erro no segundo cpf cadastrado nao valida
def is_usuario_cadastrado(cpf, usuarios):
    usuario_cadastrado = False
    for usuario in usuarios:
        if usuario['cpf']==cpf:
            print("Usuário já possui cadastro")
            usuario_cadastrado = True
            break
    return usuario_cadastrado

def depositar(valor, saldo):
    saldo = saldo + valor
    lancamentos.append(valor)
    print(f"Deposito de {valor} realizado com sucesso e o seu saldo atual é R$ {saldo}")
    return saldo

def sacar (*, valor, saldo, qtde_saques_dia):
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
        saldo, qtde_saques_dia = sacar(valor = valor, saldo = saldo,qtde_saques_dia =  qtde_saques_dia)
    if opcao_menu == 3:
        exibir_extrato(lancamentos)
    if opcao_menu == 4:
        cadastrar_conta(contas, usuarios)
    
    if opcao_menu == 5:
        listar_contas(contas)
        
    if opcao_menu == 6:
        cadastrar_usuario(usuarios)
    if opcao_menu == 0:
        break









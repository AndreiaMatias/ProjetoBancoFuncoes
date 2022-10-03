

def menu():
    menu = """
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Novo cliente
    [5] Nova conta
    [6] Listar usuários
    [7] Listar contas
    [8] Sair
    
    => """

    return int(input(menu))

def main():
    saldo = 0;
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []
    contas = []
    proxima_conta = 1
    AGENCIA = "0001"



    while True:

        valor_deposito = 0
        valor_saque = 0
        opcao = menu()

        if opcao == 1:
            valor_deposito = float(input("Informe o valor de depósito: "))
            saldo, extrato = depositar(valor_deposito, saldo, extrato)
        elif opcao == 2:
            valor_saque = float(input("Informe o valor a sacar: "))
            saldo, extrato, numero_saques = sacar(valor_saque = valor_saque, numero_saques = numero_saques, saldo = saldo, limite = limite, limite_saques = LIMITE_SAQUES, extrato=extrato)
        elif opcao == 3:
            emitir_extrato(saldo, extrato=extrato)
        elif opcao == 4:
            criar_usuario(usuarios)
        elif opcao == 5:
            cpf = input("Informe o CPF do cliente: ")
            criar_conta_corrente(cpf, AGENCIA, proxima_conta, usuarios, contas)
        elif opcao == 6:
            listar_usuarios(usuarios)
        elif opcao == 7:
            listar_contas(contas)
        elif opcao == 8:
            break
        else:
            print("""
                         Operação inválida
                Selecione novamente a operação desejada.""")



def depositar(valor_deposito, saldo, extrato,/):
    if valor_deposito > 0:
        saldo += valor_deposito
        print("Depósito realizado com sucesso")
        extrato += f"Depósito............R$ {valor_deposito:.2f}\n"
    else:
        print("""
                    Valor inválido
                Operação não realizada""")
    return saldo, extrato

def sacar(*, valor_saque, numero_saques, saldo, extrato, limite_saques, limite):

    if (valor_saque < 0):
        print("""
                Valor inválido
                Operação não realizada""")
    elif (numero_saques < limite_saques):
        if ((saldo - valor_saque) > 0):
            if (valor_saque <= limite):
                saldo -= valor_saque
                print("Saque realizado com sucesso")
                extrato += f"Saque...............R$ {valor_saque:.2f}\n"
                numero_saques += 1
            else:
                print("""
                        Valor superior ao limite
                         Operação não realizada""")
        else:
            print("Saldo insuficiente")
    else:
        print("Limite de saques diário atingido")

    return saldo, extrato, numero_saques

def emitir_extrato(saldo, /, *, extrato):
    print("Extrato".center(31))
    print("=" * 31)
    print("Não foram realizadas transações" if not extrato else extrato)
    print(f"Saldo...............R$ {saldo:.2f}\n")

def criar_usuario(usuarios):
    cpf = input("Informe apenas os números do CPF com 11 posições: ").strip('.-')
    if usuarios:
        salvar_usuario(cpf, usuarios)
    else:
        salvar_usuario(cpf, usuarios)

def salvar_usuario(cpf, usuarios):
    novo_usuario = {}
    novo_usuario["cpf"] = cpf
    dados = informar_dados_usuario()
    novo_usuario["nome"] = dados[0]
    novo_usuario["data_nascimento"] = dados[1]
    novo_usuario["endereco"] = dados[2]
    usuarios.append(novo_usuario)
    print("Usuário criado com sucesso")

def criar_conta_corrente(cpf, agencia, conta, usuarios, contas):
    if contas:
        for c in contas:
            buscar_cliente(cpf, usuarios, agencia, conta, contas)
    else:
        buscar_cliente(cpf, usuarios, agencia, conta, contas)

def buscar_cliente(cpf, usuarios, agencia, conta, contas):
    nova_conta = {}
    usuario_localizado = False
    if usuarios:
        for u in usuarios:
            usuario_localizado = True
            if u["cpf"] == cpf:
                nova_conta["cpf"] = u["cpf"]
                nova_conta["usuario"] = u["nome"]
                nova_conta["agencia"] = agencia
                nova_conta["conta"] = conta
                conta += 1
                contas.append(nova_conta)
                return contas, conta
    if usuario_localizado == False:
        print("Cliente não localizado. Favor cadastrá-lo")

def informar_dados_usuario():

    nome = input("Informe o nome do cliente: ")
    data_nascimento = input("informe a data de nascimento no formato dd/mm/aaaa: ")
    logradouro = input("Informe o nome da rua, avenida, etc: ")
    numero = input("Informe o número: ")
    bairro = input("Informe o bairro: ")
    cidade = input("Informe a cidade: ")
    estado = input("informe a sigla do estado: ").upper()
    endereco = f"{logradouro}, {numero} - {bairro} - {cidade}/{estado}"
    return nome, data_nascimento, endereco

def listar_usuarios(usuarios):
    print("Usuários".center(100))
    print("="*100)
    for u in usuarios:
        for k, v in u.items():
            print(f"{k}: {v}")
        print("*"*100)



def listar_contas(contas):
    print("Contas".center(100))
    print("=" * 100)
    for c in contas:
        for k, v in c.items():
            print(f"{k}: {v}")
        print("*" * 100)

main()


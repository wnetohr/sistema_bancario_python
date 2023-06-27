#Menu
menu = " Selecione a operação desejada!\n [d] = Depositar\n [s] = Sacar\n [e] = Extrato\n [q] = Sair"

#Vars
saldo = 0.00
limite = 500.00
extrato = "Extrato:"
numero_saque = 0
limite_saque = 3

#Functions
def depositar(saldo, extrato):
    deposito = float(input("Digite o valor que você deseja depositar: "))
    saldo+=deposito
    extrato += f"\nDeposito de R${deposito}\n"
    print("Operação realizada!")
    resultado = [saldo,extrato]
    return resultado

def sacar(saldo, limite, numero_saque, limite_saque, extrato):
    if limite_saque > numero_saque:
        print(f"Você tem {(limite_saque - numero_saque)} saques disponíveis")
        saque = float(input(f"O limite por saque é de R${limite}\nDigite o valor a ser sacado: "))
        if saque <= 500 and saldo >= saque:
            saldo-=saque
            extrato+=f"\nSaque de R${saque}\n"
            numero_saque+=1
            resultado = [saldo, numero_saque, extrato]
            print("Operação realizada!")
            return resultado
        else:
            print("Saldo insuficiente")
            resultado = [saldo, numero_saque, extrato]
            return resultado
    else:
        print("Limite de saques diários excedido")
        resultado = [saldo, numero_saque, extrato]
        return resultado
    
def ver_extrato(extrato, saldo):
    return print(extrato+f"\n Saldo atual: R${saldo}")

#Main
while True:
    print('\n'+menu)
    opcao = input()

    if opcao == "d":
        saldo, extrato = depositar(saldo, extrato)
    elif opcao == "s":
        saldo, numero_saque , extrato = sacar(saldo, limite, numero_saque, limite_saque, extrato)
    elif opcao == "e":
        ver_extrato(extrato, saldo)
    elif opcao == "q":
        break
    else:
        print("Operação inválida! \n Selecione uma operação válida!")
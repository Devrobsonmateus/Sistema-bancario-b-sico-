menu = """
    ======== BANCO RMG ========
    
    1 - SAQUE
    2 - DEPOSITO 
    3 - EXTRATO
    0 - SAIR 
   
    ===========================
    ->  """
saldo = 0
extrato = "" 
limite = 500
quantidade_saque = 0
LIMITE_SAQUE = 3

while True:

    opcao = input(menu)


    if opcao == "1": 
        valor = float(input("\nINFORME O VALOR DESEJADO PARA SAQUE: \nR$: "))
        
        limite_saque = quantidade_saque >= LIMITE_SAQUE

        limite_saldo = valor > saldo

        limite_diaria = valor > limite

        if limite_saque:
            print('\n          LIMITE DE SAQUES EXCEDIDO! \nVOLTE NOVAMENTE AMANHÃ PARA UMA NOVA TRANSAÇÃO.')
        
        elif limite_saldo:
            print("\nSALDO INSUFICIENTE!")
            
        elif limite_diaria:
            print('\n      LIMITE DE SAQUE DIARO EXCEDIDO! \nVOLTE NOVAMENTE AMANHÃ PARA UMA NOVA TRANSAÇÃO.')
            

        elif valor > 0:
            saldo -= valor 
            extrato += f"SAQUE: R$ {valor:.2f}\n"
            quantidade_saque += 1
            mensagem_saque = "SAQUE REALIZADO COM SUCESSO!"
            print()
            print(mensagem_saque.center(38))

        else:
            print('AGUARDE A CONTAGEM DAS CÉDULAS \nSAQUE REALIADO COM SUCESSO!!!')    
    
    
    elif opcao == "2":

        valor = float(input("\nINFORME O VALOR DESEJADO PARA DEPOSITO.\nR$: "))
        if valor < 0:
            print("\nVALOR PARA DEPÓSITO INVÁLIDO.")
        elif valor > 0:
            mensagem = "DEPOSITO REALIZADO COM SUCESSO!"
            print()
            print(mensagem.center(38))
            saldo += valor
            extrato += f'DEPOSITO R$:  {valor:.2f}\n'
                   
       
    elif opcao == "3":
        print()
        print("============== BANCO RMG ================")
        print()
        print("     ========== EXTRATO ==========")
        print()
        nova_mensagem = "NÃO FORAM REALIZADAS MOVIMENTAÇÕES."
        print(nova_mensagem.center(40) if not extrato else extrato)
        print(f"\nSALDO: R$ {saldo:.2f}")
        print("==========================================")


    elif opcao == "0":
        break
  
    else:
        print("OPERAÇÃO INVÁLIDA. \nPor favor selicione novamente a operação desejada!")
# Utilizamos o while para repetir um bloco de código várias vezes. Diferente do for, aqui não sabemos o número exato de vezes que nosso bloco deve ser executado.

opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))
    
    if opcao == 1:
        print('Sacando valor. Aguarde!')
    
    elif opcao == 2:
        print('Imprimindo extrato. Aguarde!')    

else:
    print('Obrigada por utilizar nosso sistema!')        
        
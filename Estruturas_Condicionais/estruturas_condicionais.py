# a estrutura condicional permite o desvio de fluxo caso alguma expressão seja atendida

saldo = 2000.0
saque = float(input('Informe o valor do saque:'))

if saldo >=saque:
    print('Processando saque')
    saldo -= saque
    
else:
    print('Saldo insuficiente')    
    
# Quando precisarmos utilizar mais de um desvio, utilizamos elif

option = int(input('Informe uma opção: [1] Sacar \n[2] Extrato:'))

if option ==1:
    print('Informe o valor do saque')    
    
elif option == 2:
    print('Aguarde. Carregando extrato')
# elif é um else que testa outra condição. Em python não usamos if por diversas vezes antes de cairmos no else, como em JS por exemplo. Caso haja necessidade de utilizar mais de um desvio, utilizamos elif    
    
else:
    print('Opção invalida')        
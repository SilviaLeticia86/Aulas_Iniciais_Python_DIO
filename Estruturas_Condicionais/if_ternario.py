saldo = 500
saque = float(input('Digite o valor do saque: '))

status = 'Sucesso' if saldo >= saque else 'Falha'
print(f" {status} ao realizar o saque.")
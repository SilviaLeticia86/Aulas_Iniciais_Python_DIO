# Operadores lógicos são utilizados em conjunto com operadores de comparação para montar uma expressão lógica. Retorna um booleano

saldo = 10000
saque = 100
limite = 50000
conta_especial = True

print(saldo >= saque )
print(not saldo > limite)

print(saldo >= saque and saldo <= limite or conta_especial and saldo == True)

print(True and True )
print(True and False )
print(False and False)
print(True or True )
print(True or False )
print(False or False)

# AND - Para ser true tudo deve ser true
# OR - Para ser true somente um deve ser true

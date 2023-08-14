# Operadores de associação são utilizados em para verificar se um objeto está presente na sequência

curso = 'Curso de Python'
frutas = ['laranja', 'uva', 'banana']
saque = [1500, 100]

print('Python' in curso) # em strings diferencia caracter maiusculo de minusculo
print('maça' in frutas)
print(200 in saque)

print('Python'not in curso) # em strings diferencia caracter maiusculo de minusculo
print('maça' not in frutas)
print(200 not in saque)

print (frutas)
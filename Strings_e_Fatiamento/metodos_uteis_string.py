# Manipulando strings

curso = 'oUtroCurSodEPYthOn'

print(curso.upper()) #transforma todos os caracteres em letras maiúscula
print(curso.lower()) #transforma todos os caracteres em letras minúscula
print(curso.title()) #transforma a primeira letra em maiúscula e o restante minúsculas

# Para remover espaços em branco

curso = '   Python '

print(curso.strip()) #remove todos os espaços
print(curso.lstrip()) #remove os espaços da esquerda 'left strip'
print(curso.rstrip()) #remove os espaços da direita 'rigth strip'

exemplo = 'Aula de Python'
print(exemplo.center(10, '#')) #centralização 
print('.'.join(exemplo)) #junção - vai passar item a item e acrescentar. Mais comum utilizar com listas
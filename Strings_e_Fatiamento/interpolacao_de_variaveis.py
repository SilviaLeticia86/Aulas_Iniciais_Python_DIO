"""
Em Python há três formas de interpolar strings, sendo: 
1. usando o sinal %; essa forma não é atualmente recomendada
2. usando o método format;
3. usando f strings
"""
# Ols Style

nome = 'Sílvia'
idade = 36
profissao = 'estudante'
linguagem = 'Python'

print('Olá, me chamo %s. Tenho %d anos, trabalho como %s e estou matriculada no curso de linguagem %s.' %(nome, idade, profissao, linguagem))

#Método Format
print('Olá, me chamo {}. Tenho {} anos, trabalho como {} e estou matriculada no curso de linguagem {}.' .format(nome, idade, profissao, linguagem))

#f Strings
print(f'Olá, me chamo {nome}. Tenho {idade} anos, trabalho como {profissao} e estou matriculada no curso de linguagem {linguagem}.')

# Formatar strings com f-string

PI = 3.14159
print(f'Valor de PI: {PI: .2f}') #utilizando 2f irá trazer duas casas após o flutuante - formatar o float (f)
print(f'Valor de PI: {PI: 10.2f}')
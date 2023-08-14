age = 20
name = 'Ana'
print(f'Meu nome é {name} e tenho {age} anos de idade')

# ou podemos declarar valores separados por vírgula em uma mesma linha
age, name = (20, 'Ana')
print(f'Meu nome é {name} e tenho {age} anos de idade')


# Constantes - nasce e permanece com mesmo valor. Não é possível mudar
# Exemplo abaixo de variável com valor reatribuido

age = 27
age = 28

# em Python não existe constante. Para torna-la imutável existe uma convenção de utilizar o nome da variável em maiusculo

AGE = 24
BRAZILIAN_STATES = [
    'SP',
    'RJ',
    'RS'
]

# Boas práticas em Python

# 1. Utilizar o padrão snake case. Ex total_da_compra
# 2. Escolher nomes sugestivos
# 3. Nomes de constantes em maiusculo
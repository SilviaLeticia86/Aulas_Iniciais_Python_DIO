# Como converter os tipos de variáveis
# As vezes precisamos converter o tipo de dado para manipular de forma diferente.
#Ex: variáveis do tipo String que armazenam números e precisamos fazer alguma operação matemática com esse valor.

# transformar em float
float_value = 10
float_value = float(float_value)

float_value = 10/3
print(float_value)


# transformar em inteiro
int_value = 10.3
int_value = int(int_value)
print(int_value // 3) # Ao utilizar duas barras, o número inteiro é apresentado. Não retorna flutuante

# transformar em string
str_value = 10.50
idade = 30

print(str(str_value)) # vai aparecer os números, porém esses nº são strings
print(str(idade))

# Concatenar string com números
print(f'idade é {idade}, preço é {str_value}') # entre chaves vai o nome da variável

# de string para número

var_numero = '10.50'
print(float(var_numero))
# quando a conversão de string não for possível, um erro é lançado no terminal


print(int(1.945842))
print(float('100'))
print(str('10.10'))


#para verificar qual o tipo da variável
print(type(int(1.945842)))
print(type(float('100')))
print(type(str('10.10')))
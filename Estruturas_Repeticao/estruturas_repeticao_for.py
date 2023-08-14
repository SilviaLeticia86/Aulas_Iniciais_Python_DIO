#FOR - é utilizado para percorrer um objeto iterável e sabemos a quantidade de vezes que deveremos executá-lo

texto = input('Informe um texto: ')
VOGAIS = 'AEIOU' 

for letra in texto:
    if letra.upper() in VOGAIS: # o upper transforma as letras para maiusculas
        print(letra, end=" ") # o end define o caractere que será inserido entre as letras vogais que são impressas. Nesse caso, um espaço em branco entre os caracteres.
else:        
    print() # adiciona um quebra de linha       
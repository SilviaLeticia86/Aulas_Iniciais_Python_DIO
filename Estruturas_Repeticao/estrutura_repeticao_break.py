while True:
    numero = int(input('Digite um número: '))
       
    if numero == 10:
        break
        
    print(numero)
    
# o break é mais utilizado com looping infinito para quebrar a continuação, caso uma condição seja atendida. Pode ser utilizado também com for, porém sua função faz mais sentido com o while.

for numero in range(100):
    if numero == 10:
        break
    
    print(numero)    
    
    
# podemos utilizar o continue para excluir/pular/não exibir uma condição. Nesse caso, o número 10 não será exibido no print    

for numero in range(100):
    if numero == 10:
        continue
    
    print(numero)     
    
# o break para a execução no momento que a condição for atendida e o continue pula a execução e continua sem determinada condição
# Range é um função built-in do Python que é usada para produzir uma sequência de números inteiros a partir de um início (inclusivo) para um fim (exclusivo). Recebe 3 argumentos: stop (obrigatório), start (opcional) e step (opcional)
"""
for numero in range(0,11):
    print (numero, end="-")
# aqui o print retorna de 0 a 10 pq o último número, no caso 11, é exclusivo, não inclusivo    
"""

for numero in range(0, 51, 5): # aqui começa por zero, vai até 50 de cinco em cinco
    print(numero, end=" ")
# o print aqui é a tabuada do cinco: 0 5 10 15 20 25 30 35 40 45 50     

""" 
0 = start
51 = stop
5 = step
""" 
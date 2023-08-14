# Em python a identação vai além da manutenção e legibilidade do código. Nele a identação serve também para indicar onde um bloco de comando começa e onde termina.

# Boas práticas em Python
# Existe uma convenção que indica utilizar 4 espaços em branco por nível de identação, ou seja, a cada novo bloco adicionamos 4 novos espaços em branco.

# def sacar(self, value: float) -> None: # início do bloco do método
    # if self.saldo >= value: # início do bloco do if
        # self.saldo -= value
        
    # fim do bloco do if - mesmo que não haja {} o python entende pela identação de 4 espaços em branco para cada bloco, que aqui é o fim da execução dessa função.
    
#fim do bloco do método - mesmo que não haja {} o python entende pela identação de 4 espaços em branco para cada bloco, que aqui é o fim da execução dessa função.      

def saque(valor):
    saldo = 700
    
    if saldo >= valor:
        print('Valor sacado')
        print('Retire seu dinheiro')
        
    print('Obrigada por ser nosso cliente!')    
        
saque(1000)        
# São definidas informando 3 aspas simples ou duplas durante a atribuição. Elas podem ocupar várias linhas do código e todos os espaços em branco são incluídos na string final.

nome = "Silvia"
mensagem = f"""
Olá. Meu nome é {nome},
Estou aprendendo Python.
"""
print(mensagem)

#Pode ser utilizado para montar um menu, pois as 3 aspas mantém os recuos definidos no texto

print(
    """
    ========== MENU ==========
    
    1 - Depositar
    2 - Sacar
    0 - Sair
    
    ==========================
    
        Obrigada por utilizar nosso sistema!!!
"""        
)
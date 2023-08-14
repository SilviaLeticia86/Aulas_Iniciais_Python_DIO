# a função built input é usada para ler dados de entrada. Recebe argumento do tipo string que é exibido para o usuário na saída da tela. Ela lê a entrada, converte para string e retorna o valor

read_name = input("Digite seu nome:")
age = input("Digite sua idade:")

print(read_name, age)
print("teste", end=" ")
print(read_name, age, end="... \n")
print(read_name, age, sep="#")



lista_nomes = []
while True:
    nome = input("Digite um nome ou 0 para sair: ")
    if nome == "0":
        break
    lista_nomes.append(nome)
for i in lista_nomes:
    print("NOME : ", end= "")
    print(i)
    


print(lista_nomes)

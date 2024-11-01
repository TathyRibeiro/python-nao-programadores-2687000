lista_vazia = []
print(lista_vazia)
# Crie uma lista apenas com elementos numéricos
lista_numerica = [1,2,3,4,5,6,7,8,9,10]
print(lista_numerica)
# Crie uma lista contendo todos os tipos e estrutura de dados que você aprendeu até agora
lista_mista = ['python', 2024, 11.17, True, [1,2,3]]
print(lista_mista)
lista_encapsulada = [[1,2,3],[1,4,5]]
print(lista_encapsulada)

# tamanho da lista
print(len(lista_mista))

# Imprima na tela apenas os 5 primeiros elementos da lista
print('5 primeiros item da lista')
print(lista_numerica[0:5])

# Crie um slice na lista para que imprima na tela os elementos de índice par
print(lista_numerica[0:-1:2])

# Remova da lista o último item
lista_numerica.pop()
print(lista_numerica)

# Insira na lista um novo item
lista_mista.append('Java')
print(lista_mista)

lista_mista.extend(lista_encapsulada)
print(lista_mista)

lista_mista[3] = 'C++'
print(lista_mista)

# Remova da lista um item específico
lista_numerica.remove(2)
print(lista_numerica)

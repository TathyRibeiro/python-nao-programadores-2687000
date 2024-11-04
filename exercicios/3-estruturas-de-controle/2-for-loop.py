# Crie uma lista
#cores = ['amarelo', 'azul', 'branco', 'verde', 'vermelho']

# Crie um for loop para imprimir cada elemento dessa lista
#for item in cores:
#   print(item)

# Crie um objeto iterável utilizando a função range()
#range(10)
#nomes = list(range(10))
#print(nomes)

# Use esse objeto iterável para criar um for loop que imprima na tela a frase "Estou aprendendo uma linguagem de programação."
for itens in range(10):
   print(f'{itens} - Estou aprendendo uma linguagem de programação.')


#estruturas de controle
#for  variavel_temporaria in objeto_iteravel:
#  faça isso
#curso_linkedin_learning = ['SQL','PYTHON','CIÊNCIA DE DADOS','R','ALGORITMOS','JAVA','JAVASCRIPT']

#for curso in curso_linkedin_learning:
#   print(curso)


#função range (inicio,fim,passo) gera uma sequencia de intervalo aberto
#exemplo
#range(5)
#l = list(range(5))
#print(l)

#exemplo 2 - lista passando inicio, fim e passo, usando range 
#li = list(range(30,40,2))
#print(li)

#exemplo 3
#for item in range(7):
#   print(f'{item} - estou aprendendo python.')
#else:
#   print('Fim do Loop.')
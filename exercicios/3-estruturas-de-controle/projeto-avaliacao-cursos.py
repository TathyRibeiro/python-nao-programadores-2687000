# Nesse desafio você verificará dentro de uma lista se o item estar contido nela, caso verdadeiro deverá imprimir na tela essa informação, além disso deverá solicitar avaliação para o item e armazená-la em um dicionário.
# 1. Crie uma lista com 5 diferentes cursos do LinkedIn Learning
cursos_linkedin_learning = [
  'SQL',
  'JAVA',
  'PYTHON',
  'KUBERNETES',
  'AWS'
]

# 2. Crie 3 variáveis do tipo string e associe 1 curso a cada uma delas
curso_linguagem_1 = 'SQL'
curso_linguagem_2 = 'JAVA'
curso_linguagem_3 = 'PYTHON'

# 3. Crie um dicionário vazio para armazenar a nota do curso
nota = {}

# 4. Crie uma estrutura condicional para verificar se cada variável está contida na lista
if curso_linguagem_1 in cursos_linkedin_learning:
  print(f"O curso {curso_linguagem_1} está no catálogo.")
if curso_linguagem_2 in cursos_linkedin_learning:
  print(f"O curso {curso_linguagem_2} está no catálogo.")
if curso_linguagem_3 in cursos_linkedin_learning:
  print(f"O curso {curso_linguagem_3} está no catálogo.")

# 5. Se o curso estiver na lista, solicite uma nota para avaliação
if curso_linguagem_1 in cursos_linkedin_learning:
  print(f"O curso {curso_linguagem_1} está no catálogo. Por favor, avalie o curso.")
  nota[curso_linguagem_1] = int(input('Qual é a nota que você dá para o curso (0 a 5)? '))
if curso_linguagem_2 in cursos_linkedin_learning:
  print(f"O curso {curso_linguagem_2} está no catálogo. Por favor, avalie o curso.")
  nota[curso_linguagem_2] = int(input('Qual é a nota que você dá para o curso (0 a 5)? '))
if curso_linguagem_3 in cursos_linkedin_learning:
  print(f"O curso {curso_linguagem_3} está no catálogo. Por favor, avalie o curso.")
  nota[curso_linguagem_3] = int(input('Qual é a nota que você dá para o curso (0 a 5)? '))
else:
  print(f"Infelizmente o curso não compõe o nosso catálogo.")

# 6. Armazene essa nota no dicionário, sendo a chave o título do curso e o valor a nota
print(nota)




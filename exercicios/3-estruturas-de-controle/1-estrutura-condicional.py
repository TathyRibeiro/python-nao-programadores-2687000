# Declare 4 variáveis do tipo numérica
a = 23
b = 12
c = 32
d = 44

# Crie uma estrutura condicional para comparar dois números
if a > b:
  print(f'O número {a} é maior do que {b}')

# Se a condição for verdadeira, imprima na tela uma mensagem informando que a condição foi cumprida e informando o número de maior valor


# Se a condição não for cumprida, imprima na tela uma mensagem informando que a condição é negativa e informe o número de maior valor
if c == d:
  print(f'O número {c} é igual a {d}')
else :
  print(f'O número {c} não é igual a {d}')

# Insira outras condições na estrutura condicional usando o elif
if a < b:
  print(f'O número {c} é igual a {d}')
elif a > c:
  print(f'O número {a} é maior do que {c}')
elif d > c:
  print(f'O número {d} é maior do que {c}')

# Incremente a estrutura condicional já existente com expressões lógicas utilizando "and" ou "or"
if (a < b) and (b < c):
  print(f'O número {c} é igual a {d}')
elif (a > c) or (c > d):
  print(f'O número {a} é maior do que {c}')
elif d > c:
  print(f'O número {d} é maior do que {c}')

# Crie uma estrutura condicional onde mais de uma condição seja verdadeira, e use apenas a palavra reservada "if"




# condicionais 
x = 4
y = 30
a = 3
e = 66

# exemplo 1
if x > y:
  print(f'A condição foi cumprida. O número {x} é maior do que {y}')
elif x > a:
  print(f'Nesse caso, verificamos  que o número {x} é maior do que {a}')
else:
  print(f'A conidição não foi cumprida. Na verdade, o número {y} é maior do que {x}')

# exemplo 2
if (x > y) or (x > a):
  print(f'A condição foi cumprida. O número {x} é maior do que {y} ou maior do que {a}')
elif (x == a) and (e > y):
  print(f'Nesse caso, verificamos  que o número {x} é igual a {a} e {e} maior do que {y}')
else:
  print(f'A conidição não foi cumprida. Na verdade, o número {y} é maior do que {x}')

# comando clear no terminal limpa tudo
#   
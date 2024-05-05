# Exercício 1
# Dados dois números inteiros, retorne o seu produto somente se o produto for igual ou menor a 1000. Caso contrário, retorne a soma.


# Dados 1
# numero1 = 20
# numero2 = 30

# Dados 2
numero1 = 40
numero2 = 30

if (numero1 * numero2 <= 1000):
  produto = numero1 * numero2
  print(f'O resultado é {produto}')
else:
  soma = numero1 + numero2
  print(f'O resultado é {soma}')

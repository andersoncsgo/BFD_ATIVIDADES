from functools import reduce

# 1. Dobro dos números (map + lambda)
lista1 = [1, 2, 3, 4, 5]
dobro = list(map(lambda x: x * 2, lista1))
print("Dobro dos números:", dobro)
print("-----------------------------")

# 2. Filtrar pares (filter + lambda)
lista2 = [10, 15, 20, 25, 30]
pares = list(filter(lambda x: x % 2 == 0, lista2))
print("Números pares:", pares)
print("-----------------------------")

# 3. Soma dos números (reduce + lambda)
lista3 = [1, 2, 3, 4, 5]
soma = reduce(lambda x, y: x + y, lista3)
print("Soma dos números:", soma)
print("-----------------------------")

# 4. Ordenação por comprimento da palavra (sorted + lambda)
palavras = ["uva", "banana", "maçã", "laranja"]
ordenadas_tamanho = sorted(palavras, key=lambda x: len(x))
print("Palavras ordenadas por tamanho:", ordenadas_tamanho)
print("-----------------------------")

# 5. Primeira letra maiúscula (map + lambda)
nomes = ["ana", "pedro", "maria"]
nomes_maiusculo = list(map(lambda x: x.capitalize(), nomes))
print("Nomes com inicial maiúscula:", nomes_maiusculo)
print("-----------------------------")

# 6. Produto dos números (reduce + lambda)
lista4 = [2, 3, 4, 5]
produto = reduce(lambda x, y: x * y, lista4)
print("Produto dos números:", produto)
print("-----------------------------")

# 7. Ordenar por último caractere (sorted + lambda)
palavras2 = ["banana", "uva", "maçã", "laranja"]
ordenadas_ultimo = sorted(palavras2, key=lambda x: x[-1])
print("Palavras ordenadas pelo último caractere:", ordenadas_ultimo)
print("-----------------------------")
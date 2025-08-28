#Crie um dicionário simples - 1 Questao
aluno = {"nome": "Anderson", "idade": 22, "nota": 10}
#Acessando valores - 2 Questao
produto = {"nome": "Caneta", "preço": 2.5, "estoque": 100}

print(produto.get("nome"))
print(produto.get("estoque"))
print("---------------------------------------")

#Adicionando novos pares chave-valor - 3 Questao

pessoa = {"nome": "Carlos", "idade": 30}

pessoa["Cidade"] = ["São Paulo"]
print(pessoa.get("Cidade"))

print("---------------------------------------")

#Removendo elementos - 4 Questao

carro = {"marca": "Ford", "modelo": "Fiesta", "ano": 2010}
del carro["ano"]
print(carro.keys())
print("---------------------------------------")
#Verificando existência de uma chave - 5 Questao

contato = {"nome": "Ana", "email": "ana@email.com"}
if "telefone" in contato:
    print("telefone: ", contato.get[telefone])
else:
    print("telefone nao esta no dicionario")
print("---------------------------------------")
#Contando frequência de palavras - 6 Questao

palavras = ["maçã", "banana", "maçã", "laranja", "banana", "maçã"]

for fruta in enumerate(palavras):
    print(f"O dicionarios de {palavras} é {fruta}")

quantidade_maca = palavras.count("maçã")
quantidade_banana = palavras.count("banana")
quantidade_laranja = palavras.count("laranja")
print(f"A quantidade de maça é: {quantidade_maca}\na quantidade de banana é: {quantidade_banana}\na quantidade de laranja é: {quantidade_laranja}")

print("---------------------------------------")

#Invertendo um dicionário - 7 Questao

d = {"a": 1, "b": 2, "c": 3}

d_invertido = {valor: chave for chave, valor in d.items()}
print(d_invertido)

print("---------------------------------------")
# Dicionário com listas - 8 Questao

notas_dos_alunos = {
    "Anderson": [9.9, 10.0, 5.9],
    "João": [2.0, 10.0, 9.8],
    "Beatriz": [10.0, 5.9, 8.6]
            }

for aluno, notas in notas_dos_alunos.items():
    soma_das_notas = sum(notas)
    quantidades_de_notas = len(notas)

    certo = soma_das_notas / quantidades_de_notas
    print(f"A média do(a) aluno(a) {aluno} é: {certo:.2f}")

print("---------------------------------------")
#Mesclando dois dicionários - 9 Questao
def juncao(d1, d2):
    novo_dicionario = d1.copy()
    novo_dicionario.update(d2)

    return novo_dicionario

dicionario1 = {"a": 1, "b": 2, "c": 3}
dicionario2 = {"c": 4, "d": 5, "e": 6}

novo_dicionario = juncao(dicionario1,dicionario2)
print(f"Dicionário 1: {dicionario1}")
print(f"Dicionário 2: {dicionario2}")
print(f"Dicionário Combinado: {novo_dicionario}")

print("---------------------------------------")
#Ordenando dicionário por valor - 10 Questao
pontuacoes = {"João": 50, "Maria": 80, "Pedro": 70}
pontuacoes_ordenadas = sorted(pontuacoes.items(), key=lambda  item: item[1], reverse=True)


for nome, notas in pontuacoes_ordenadas:
    print(f"{nome} e {notas}")

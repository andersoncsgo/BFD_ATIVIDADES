# 1- Crie uma função chamada saudacao que imprime na tela a mensagem "Olá, bem-vindo ao Python!". Em seguida, chame a função no programa.
def saudacao():
    print("Olá, bem-vindo ao Python!")
saudacao()

def limpar_tela():
    print("-----------------------------")

limpar_tela()
# 2 - Crie uma função chamada dobro que recebe um número como parâmetro e retorna o dobro desse número. Teste chamando a função com diferentes valores.
def dobro(n):
    return n * 2
print(dobro(5))
print(dobro(10))

limpar_tela()
# 3 - Crie uma função chamada soma que receba dois números e retorne a soma deles. Depois, use a função para somar 10 + 20.
def soma(n1, n2):
    return n1 + n2
print(soma(10, 20))

limpar_tela()
# 4 - Crie uma função chamada mensagem que receba um nome como parâmetro e exiba a mensagem: Caso o nome não seja informado, mostre "Olá, visitante!".
def mensagem(nome):
    if nome:
        print(f"Olá, {nome}!")
    else:
        print("Olá, visitante!")

mensagem("Anderson")

limpar_tela()
# 5 - Crie uma função chamada operacoes que receba dois números e retorne a soma, a subtração e a multiplicação deles.
def operacoes(n1, n2):
    soma = n1 + n2
    subtracao = n1 - n2
    multiplicacao = n1 * n2
    return soma, subtracao, multiplicacao

print(operacoes(14, 7))

limpar_tela()
# 6 - Crie uma função chamada media que receba uma quantidade variável de números e retorne a média deles. Teste com 3, 5 e 7 valores diferentes.
def media(*args):
    return sum(args) / len(args)

print(media(3, 5, 7))

limpar_tela()
# 7 - Crie uma função chamada dados_pessoais que receba informações de uma pessoa (nome, idade, cidade, etc.) usando **kwargs e imprima cada dado em uma linha. Exemplo de chamada:
# dados_pessoais(nome="Ana", idade=25, cidade="Recife")
def dados_pessoais(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

dados_pessoais(nome="Ana", idade=25, cidade="Recife")

limpar_tela()
# 8 - Crie uma função chamada calculadora que tenha dentro dela outras funções (somar, subtrair, multiplicar, dividir). A função principal deve permitir escolher a operação e retornar o resultado.
def calculadora(operacao, n1, n2):
    def somar(a, b):
        return a + b
    def subtrair(a, b):
        return a - b
    def multiplicar(a, b):
        return a * b
    def dividir(a, b):
        if b != 0:
            return a / b
        else:
            return "Erro: Divisão por zero"
    
    if operacao == "somar":
        return somar(n1, n2)
    elif operacao == "subtrair":
        return subtrair(n1, n2)
    elif operacao == "multiplicar":
        return multiplicar(n1, n2)
    elif operacao == "dividir":
        return dividir(n1, n2)
    else:
        return "Operação inválida"
    
print(calculadora("somar", 10, 5))

limpar_tela()
# 9 -Crie uma função chamada aplicar_operacao que receba dois números e uma função como parâmetros. A função deve aplicar a operação recebida (ex: soma, multiplicação). Exemplo
#def soma(a, b): return a + b
#  aplicar_operacao(3, 4, soma)

def aplicar_operacao(n1, n2, opercao):
    return opercao(n1, n2)

resultado_soma = aplicar_operacao(3, 4, soma)
print(f"O resultado da soma é: {resultado_soma}")


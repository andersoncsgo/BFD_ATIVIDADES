from funcoes import limpar_tela
# 1 - Escreva um programa que peça ao usuário para digitar um número. Trate o erro caso ele digite algo que não seja um número inteiro.
try:
    numero = int(input("digite um numero inteiro: "))
except ValueError:
    print("Erro: Você não digitou um número inteiro.")

limpar_tela()

# 2 - Peça ao usuário dois números e tente multiplicá-los. Se o usuário digitar algo inválido, exiba uma mensagem de erro.
try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 * num2
    print(f"O resultado da multiplicação é: {resultado}")
except ValueError:
    print("Erro: Entrada inválida. Por favor, digite números válidos.")

limpar_tela()

# 3 - Crie um programa que peça ao usuário um número inteiro. Se a conversão for bem-sucedida, mostre uma mensagem usando o bloco else.
try:
    numero_inteiro = int(input("Digite um número inteiro: "))
except ValueError:
    print("Erro: Você não digitou um número inteiro.")
else:
    print(f"Você digitou o número inteiro: {numero_inteiro}")

limpar_tela()

# 4 - Implemente um programa que abra um arquivo chamado dados.txt (não precisa existir). Use try e finally para garantir que uma mensagem de "Encerrando programa" seja sempre exibida.

try:
    arquivo = open("dados.txt", "r")
    conteudo = arquivo.read()
    print(conteudo)
except FileNotFoundError:
    print("Erro: O arquivo 'dados.txt' não foi encontrado.")
finally:
    print("Encerrando programa.")

limpar_tela()

# 5 - Crie uma função dividir(a, b) que lance (raise) uma exceção ZeroDivisionError se b for igual a zero. Caso contrário, retorne o resultado da divisão.

def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("Erro: Divisão por zero não é permitida.")
    return a / b
try:
    print(dividir(10, 2))
    print(dividir(10, 0))
except ZeroDivisionError as e:
    print(e)

limpar_tela()

# 6 - Crie uma exceção personalizada chamada IdadeInvalidaError. Depois, crie uma função cadastrar_idade(idade) que lance essa exceção caso a idade seja negativa.
class IdadeInvalidaError(Exception):
    pass
def cadastrar_idade(idade):
    if idade < 0:
        raise IdadeInvalidaError("Erro: Idade não pode ser negativa.")
    print(f"Idade {idade} cadastrada com sucesso.")
try:
    cadastrar_idade(25)
    cadastrar_idade(-5)
except IdadeInvalidaError as e:
    print(e)

limpar_tela()

#7 - Peça ao usuário dois números e divida o primeiro pelo segundo. Trate dois tipos de erro: ValueError se o usuário digitar algo inválido ZeroDivisionError se tentar dividir por zero

try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 / num2
    print(f"O resultado da divisão é: {resultado}")
except ValueError:
    print("Erro: Entrada inválida. Por favor, digite números válidos.")
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")

limpar_tela()

# 8 - Crie um programa que peça ao usuário um número inteiro e verifique se ele é par. Use: try para a conversão,else para verificar se é par ou ímpar, finally para exibir "Fim do programa".
try:
    numero = int(input("Digite um número inteiro: "))
except ValueError:
    print("Erro: Você não digitou um número inteiro.")
else:
    if numero % 2 == 0:
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")
finally:
    print("Fim do programa.")

limpar_tela()

#Crie uma função sacar(saldo, valor) que: Lance (raise) uma exceção personalizada SaldoInsuficienteError se o valor for maior que o saldo. Caso contrário, retorne o novo saldo. Teste a função dentro de um try-except e exiba uma mensagem apropriada ao usuário.
class SaldoInsuficienteError(Exception):
    pass
def sacar(saldo, valor):
    if valor > saldo:
        raise SaldoInsuficienteError("Erro: Saldo insuficiente para realizar o saque.")
    return saldo - valor
try:
    saldo_atual = 1000
    novo_saldo = sacar(saldo_atual, 500)
    print(f"Saque realizado com sucesso. Novo saldo: {novo_saldo}")
    novo_saldo = sacar(novo_saldo, 600)
    print(f"Saque realizado com sucesso. Novo saldo: {novo_saldo}")
except SaldoInsuficienteError as e:
    print(e)
limpar_tela()
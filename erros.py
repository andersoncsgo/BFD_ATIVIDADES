from funcoes import limpar_tela
# 1 Escreva um programa que peça ao usuário para digitar um número. Trate o erro caso ele digite algo que não seja um número inteiro.
try:
    numero = int(input("digite um numero inteiro: "))
except ValueError:
    print("Erro: Você não digitou um número inteiro.")

limpar_tela()

#
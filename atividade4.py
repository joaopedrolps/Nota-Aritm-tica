#1 - Faça um programa em Python que receba o nome e as quatro notas de um aluno, calcule e mostre a média aritmética. No final mostre a mensagem de Aprovado se a média for maior ou igual a 6 ou Reprovado se a média for menor que 6.
nome2 = input("Qual o seu nome? ")


media1 = float(input("Digite sua nota de Português: "))
media2 = float(input("Digite sua nota de Matemática: "))
media3 = float(input("Digite sua nota de Fisíca: "))
media4 = float(input("Digite sua nota de Quimica: "))

conta1 = (media1 + media2 + media3 + media4)/4

operacao = print(nome2, "Sua média bimestral é:", conta1)

if conta1 >= 6:
    print("Sua situação é: Aprovado")

else: print("Sua situação é: Reprovado")

#2 - Faça um programa em Python que receba um número inteiro e imprima uma mensagem mostrando se o número digitado é par ou ímpar.

numero = int(input('Digite um inteiro: '))

if (numero%2) == 0:
        print("O número digitado é par")
else:
        print("O número digitado é ímpar")
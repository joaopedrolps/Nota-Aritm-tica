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

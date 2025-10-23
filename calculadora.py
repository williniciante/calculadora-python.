print("1-Soma.")
print("2-Subtração.")
print("3-Multiplicação.")
print("4-Divisão.")

escolha = int(input("Escolha uma das operações acima: "))

if escolha < 1 or escolha > 4:
    print("Opção inválida.")

else:
    numero_1 = float(input("Digite o primeiro número: "))
    numero_2 = float(input("Digite o segundo número: "))

if escolha == 1:
    print(f"Soma: {numero_1+numero_2}")
elif escolha == 2:
    print(f"Subtração: {numero_1-numero_2}")
elif escolha == 3:
    print(f"Multiplicação: {numero_1*numero_2}")
elif escolha == 4:
    print(f"Divisão: {numero_1/numero_2}")


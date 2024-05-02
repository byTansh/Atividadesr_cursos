idade = int(input("Insira sua idade: "))

if (idade <= 4):
    print("O nadador não esta apto a competir!")
elif (idade >= 5 and idade <= 7):
    print("O nadador está classificado como: criança nivel 1!")
elif (idade >= 8 and idade <= 10):
    print("O nadador está classificado como: criança nivel 2!")
elif (idade >= 11 and idade <= 13):
    print("O nadador está classificado como: adolescente nivel 1!")
elif (idade >= 14 and idade <= 17):
    print("O nadador está classificado como: adolescente nivel 2!")
else: print("O nadador não está apto a competir!")

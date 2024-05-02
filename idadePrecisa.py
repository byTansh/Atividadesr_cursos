valor1 = int(input("Insira o dia de nascimento: "));
valor2 = int(input("Insira o mês de nascimento: "));
valor3 = int(input("Insira o ano de nascimento: "));

valor4 = int(input("Insira o dia atual: "));
valor5 = int(input("Insira o mês atual: "));
valor6 = int(input("Insira o ano atual: "));

calc1 = valor6 - valor3
calc2 = calc1 - 1

if ((valor1 < valor4) or (valor2 < valor5)):
    print("Sua idade é igual a: ", calc2);
else: print("Sua idade é igual a: ", calc1);

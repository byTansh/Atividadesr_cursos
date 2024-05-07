Valor1 = int(input("Insira o primeiro valor: "))
Valor2 = int(input("Insira o segundo valor: "))
Valor3 = int(input("Insira o terceiro valor: "))
Valor4 = int(input("Insira o quarto valor: "))

soma_total = ((Valor1 + Valor2) + (Valor3 + Valor4)) / 4

if (soma_total > 7) :
    print(f"Parabens aluno, você passou! \nNota: {soma_total}")
elif (soma_total == 7) :
    print(f"Parabens aluno, você passou! mas cuidado, você quase reprovou! \nNota: {soma_total}")
else :
    print(f"Infelizmente você reprovou! estude mais da proxima vez \nNota: {soma_total}")

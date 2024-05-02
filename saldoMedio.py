saldo = int(input("Insira a media do seu sálario anualmente: R$"))

credito = (0 / 100) * saldo
credito2 = (20 / 100) * saldo
credito3 = (30 / 100) * saldo
credito4 = (40 / 100) * saldo

credito = "{:.2f}".format(credito)
credito2 = "{:.2f}".format(credito2)
credito3 = "{:.2f}".format(credito3)
credito4 = "{:.2f}".format(credito4)

if (saldo >= 0 and saldo <= 200):
    print(f"Seu saldo medio é de: R${saldo} \nSeu credito disponivel é de: R${credito}")
elif (saldo >= 201 and saldo <= 400):
    print(f"Seu saldo medio é de: R${saldo} \nSeu credito disponivel é de: R${credito2}")
elif (saldo >= 401 and saldo <= 600):
    print(f"Seu saldo medio é de: R${saldo} \nSeu credito disponivel é de: R${credito3}")
elif (saldo >= 601):
    print(f"Seu saldo medio é de: R${saldo} \nSeu credito disponivel é de: R${credito4}")
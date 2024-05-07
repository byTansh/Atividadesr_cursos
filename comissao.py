salario = int(input("Digite seu salario: "))
comissao = int(input("Digite o valor total das vendas feitas: "))

taxa = (3 / 100) * comissao
taxa_extra = 5 / 100 * (comissao - 1500)

if (comissao <= 1500):
    print (f"Seu salario é de: R${salario:.2f} \nSua comissão mensal foi de: R${taxa:.2f} \nValor total do salario: {salario + taxa:.2f}")
elif (comissao > 1500):
    print (f"Seu salario é de: R${salario:.2f} \nSua comissão mensal foi de: R${taxa + taxa_extra:.2f} \nValor total do salario: {salario + taxa + taxa_extra:.2f}") 
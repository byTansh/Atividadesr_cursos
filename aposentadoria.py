codigoF = int(input("Digite seu codigo pessoal: "))
anoNascimento = int(input("Digite seu ano de nascimento: "))
anoImpresa = int(input("Digite o ano que ingressou na empresa: "))

anoNascimento = 2024 - anoNascimento
anoImpresa = 2024 - anoImpresa

if (anoNascimento >= 65 or anoImpresa >= 30 or (anoNascimento >= 60 and anoImpresa >= 25)):
    print(f"Codigo = {codigoF} \nIdade = {anoNascimento} \nTempo de trabalho: {anoImpresa} \nRequerer aposentadoria")
else:
    print(f"Codigo = {codigoF} \nIdade = {anoNascimento} \nTempo de trabalho: {anoImpresa} \nNão requerer aposentadoria")
# capacidade de solicitação da carteira de mototrista

# variaveis
idade = int(input("digite sua idade:"))
exame_medico = input("você passou pelo exame médico: (y/n)")
violacoes_de_transito = input("você possui alguma infração de trânsito registrada: (y/n)")

#teste lógico

if idade >= 18 and exame_medico == "y" and violacoes_de_transito == "n":
    print("você pode solicitar a sua carteitra")
elif exame_medico == "n" and violacoes_de_transito == "y":
    print("você não pode solicitar uma carteira até fazer o exame e tratar sua infração")
elif idade < 18:
 print ("você não possui idade suficiente para solicitar sua carteira")
elif exame_medico == "n":
 print("realizse o exame médico para solicitar sua carteira")
elif violacoes_de_transito =="y":
    print("você não pode solicitar uma carteira até resolver sua infração no transito")

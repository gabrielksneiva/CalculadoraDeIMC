
def imc(peso, altura):
    IMC=peso/(altura**2)
    return IMC

def msg(mensagem):
    print(len(mensagem)*"=", end="\n")
    print(mensagem)
    print(len(mensagem) * "=", end="\n")

def sep(mensagem):
    print(len(mensagem)*"=", end="\n")

#Programa Principal
pergunta_peso="Digite seu peso (em kg): "
pergunta_altura="Digite sua altura (em m): "

msg("Bem vindo(a) a calculadora de IMC!")
sep(pergunta_peso)
peso = float(input(pergunta_peso))
sep(pergunta_peso)
sep(pergunta_altura)
altura = float(input(pergunta_altura))
sep(pergunta_altura)

imc = imc(peso, altura)

result = "Seu imc é %.2f"%(imc)

msg(result)

if imc < 16:
    msg("O seu IMC indica magreza grave!")
elif imc>=16 and imc<17:
    msg("O seu IMC indica magreza moderada!")
elif imc >= 17 and imc < 18.5:
    msg("O seu IMC indica magreza leve!")
elif imc>=18.5 and imc<25:
    msg("O seu IMC indica que você está saudável!")
elif imc>=25 and imc<30:
    msg("O seu IMC indica sobrepeso")
elif imc>=30 and imc<35:
    msg("O seu IMC indica obesidade de grau I")
elif imc>=35 and imc<40:
    msg("O seu IMC indica obesidade de grau II (severa)")
else:
    msg("O seu IMC indica obesidade de grau III (mórbida)")



input("Pressione Enter para encerrar o programa!")
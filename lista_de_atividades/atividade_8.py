import requests
import json

#resolução da proposta
def converssor():
    num = float(input("valor a ser convertido"))
    cotacao = float(input("cotaçao atual"))
    print(f"sua converção foi de :{num * cotacao} reais")

#Resposta alternativa A
def dolar_hoje():
    requisicao = requests.get("https://economia.awesomeapi.com.br/all/USD-BRL")
    cotacao = requisicao.json()
    print('### "cotação dolar hoje" ###')
    print({cotacao["USD"]["name"]})
    print("data da converção: "+cotacao["USD"]["create_date"])
    print("cotação atual: "+cotacao["USD"]["bid"])

#resposta alternativa B
def comparador():
    print("comparador")
    hoje_dol = float(input("dolar hoje:"))
    data_dol = float(input("dolar na data desejada:"))

    if hoje_dol > data_dol:
        al = (hoje_dol * 100) / data_dol
        print(f"o cotação do dolar aumentou:{al / 2} %")
    else:
        al = (data_dol * 100) / hoje_dol
        print(f"o dolar caiu: {al/ 2 }%")

dolar_hoje()
converssor()
comparador()




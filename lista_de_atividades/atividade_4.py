total = int(input("qual a quantidade total de ração em kg"))
gato = float(input("quantidade que seus gato comera em gramas"))

cal = total * 1000 - gato*5
print(f"em 5 dias restara:{cal:-2} gramas de ração")



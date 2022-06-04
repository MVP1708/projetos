renda = float(input("por favor insira seu salario atual"))

#def pois sempre é bom deixar o código mais genérico
def calc(salario):
    calcula = salario + (salario * 25 / 100)
    print(f"seu salario para os próximos meses será {calcula} ou seja um aumento de:{calcula - renda} reais")
calc(renda)


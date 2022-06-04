ano_input = int(input("favor insira seu ano de nacimento"))
atual = 2022

def calc_idade(ano, ano_atual):
    anos = atual - ano_input
    meses = anos * 12
    semanas = meses * 4
    dias = anos * 365
    print(f"sua idade é aproximadamente:{anos} anos, {meses} meses, {semanas} semanas ,{dias} dias")
calc_idade(ano_input, atual)

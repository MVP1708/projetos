#solução para a questão
a = int(input("primeiro numero"))
b = int(input("segundo numero"))
c = int(input("terceiro numero"))

#alternativa A
soma = a + b + c
print(f"soma ao quadrado: {soma ** 2}")

#alternativa B
ordem = [a,b,c]

max_value = max(ordem)
print(f"o maior valor ao quadrado :{max_value ** 2}")

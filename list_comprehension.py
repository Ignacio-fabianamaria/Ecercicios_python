# Compreensão de listas

# Criar uma lista com números de 1 a 10 e elevados à 2
potencias1 = []
for item in range(1, 11):
    potencias1.append(item**2)
print("Potencia **2:", potencias1)

# Mesma operação, mas utilizando list comprehension
potencias2 = [item ** 2 for item in range(1, 11)]
print("Potencia **2 + list comprehension :", potencias2)

# Multiplicar 10 os números de 1 a 16
numeros = [n * 10 for n in range(1, 16)]
print("Multiplicar 10: ", numeros)

# Lista de números pares elevados à 2
pares = [n ** 2 for n in range(0, 11) if n % 2 != 0]
print(pares)

# Lista com caractéres maiúsculos
maiusculos = [c.upper() for c in 'fabiana']
print(maiusculos)

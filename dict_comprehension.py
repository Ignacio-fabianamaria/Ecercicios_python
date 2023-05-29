# Criar dicionário com todos os números elevados à 2
dict_numeros1 = {}
for item in range(1, 11):
    dict_numeros1[item] = item ** 2
print('Dicioário de n° elevados à 2: ', dict_numeros1)

# Mesma operação, agora usando dict comprehesion
dict_numeros2 = {f'item_{item}': item ** 2 for item in range(1, 11)}
print('Dicioário de n° elevados à 2 com dict_comprehension:', dict_numeros2)


dict_impares = {
    f'index_{item}': item ** 2 for item in range(0, 11) if item % 2 != 0
    }
print('Números ímpares: ', dict_impares)
# Funções anonimas(Funções Lambda)

# Declaração tradicional
def area_quadrado(lado):
    return lado * lado


print('Área do quadrado:', area_quadrado(5))

# Declaração da função lambda
area_quad = lambda lado: lado * lado
print('Área do quadrado na função lambda:', area_quad(5))

triplo = lambda x: x * 3
print("Função lambda para calcular triplo: ", triplo(7))

# Declaração de função lambda usando 'map'
print('mapeando uma lista + lambda:', list(map(lambda x: x * 3, [4, 5, 6, 7, 8, 0, 1, 2])))

# Uma função lambda é uma função anônima em Python que pode ser
# definida em uma única linha. Ela é útil quando você precisa de
# uma função simples sem a necessidade de definir explicitamente
# uma função separada usando a declaração def.

# As funções lambda são declaradas usando a palavra-chave lambda,
# seguida por uma lista de argumentos separados por vírgulas,
# seguida por dois pontos : e uma expressão que define o retorno da função.
# A função lambda pode ter quantos argumentos você precisar, mas deve ter
# apenas uma expressão para calcular o retorno.

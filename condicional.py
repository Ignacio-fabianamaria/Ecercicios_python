# Atribuição condicional em uma linha de código

nome1 = 'casa'
if len(nome1) > 5:
    var = 100
else:
    var = 0
print('O tamanho da palavra: ', var)


nome2 = 'fabiana'
var = 100 if len(nome2) > 5 else 0
print('O valor de var é: ', var)

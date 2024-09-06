def somar_elementos(lista):
    soma = 0

    for numero in lista:
        soma += numero

    media = soma / len(lista)

    maiores = []

    for i in lista:
        if i >= media:
            maiores.append(i)

    return media, maiores


a = (5, 10, 6, 8)

print(somar_elementos(a))
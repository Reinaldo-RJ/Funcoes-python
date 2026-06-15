def media_lista(numeros):
    lista = []
    media = 0

    for i in numeros:
        media += i

    resultado = media / len(numeros)
    lista.append(resultado)
    print(lista)


media_lista([10,20,30,40])
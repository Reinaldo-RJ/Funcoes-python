def palindromo(texto):

    texto_inverso = texto[::-1]

    if texto == texto_inverso:
        print("palindromo")
    else:
        print("Não é palindromo")

palindromo("radar")
palindromo("computador")
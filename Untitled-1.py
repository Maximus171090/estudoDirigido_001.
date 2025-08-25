


numero = int(input('Digite o número para ver a tabuada '))



for numero in range(1, 11):
    print(f"\nTabuada do {numero}:")  # Cabeçalho da tabuada
    # Laço para multiplicar o número atual pelos números de 1 a 10
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
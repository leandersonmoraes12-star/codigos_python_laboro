while True:
    N = int (input('Digite um conjunto de números: '))
    if N == 0:
        break
    if N % 2 != 0:
        print(f'Número impar: {N}')
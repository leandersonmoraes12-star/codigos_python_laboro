# Função que irá somar valores
def soma_ate(n):    
    print(f"Entrando na soma_ate({n})")
    if n == 1: # Caso base: se n for igual 1 devolve 1
        print("-> Caso base! Retornando 1")
        return 1
    
    resultado = n + soma_ate(n-1)
    print(f"<- Retornando {n} + .... = {resultado}")
    return resultado

# Chamando a função - exemplos

print(soma_ate(3))
        
    
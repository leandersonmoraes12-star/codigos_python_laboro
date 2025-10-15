valores = [] # Criando uma lista vazia

for item in range(10,14):
    valores.append(item)
    
print(valores)

# Preenchendo uma lista com dados dinâmicos
valores2 = []
while True:
    num = int(input('Informe um valor númerico qualquer - Zero para encerrar: '))
    
    if num == 0:
        break # Encerra o sistema
    else:
        valores2.append(num)
        
print("\nPrograma encerrado\n")
print(valores2)

while True:
    print(valores2)
    
    print('Deseja apagar? 1-Sim 2-Não')
    resposta = int(input('Qual a sua resposta? '))
    
    if resposta == 1:
        valores2.pop()
        print(f'Item {resposta} apagado com sucesso!')
        
    elif resposta ==2:
        break
    else:
        break
                
print("Voce saiu do sistema!")
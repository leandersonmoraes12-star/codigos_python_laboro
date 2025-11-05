#Função - Modo 1 - sem parãmetro e sem retorno
def menu():
    print("--- MENU DO SISTEMA ---")
    print("1- Consultar")
    print("2- Inserir")
    print("3- Excluir")
    
# Chamando a função
menu()

#Função - Modo 2 - com parãmetro e sem retorno
def somar(num1, num2):
    print(f'A Soma é {num1 + num2}')
    
#Chamando a função somar
somar(4,5) 

#Função - Modo 3 - sem parãmetro e com retorno
def dobro():
    valor = int(input("Informe um valor numérico: "))
    
    return valor * 2  
    
#Chamando a função
print(f'O dobro é {dobro()}')

#Função - Modo 4 - com parãmetro e retorno 
def triplo(valor):
    resposta = valor * 3
    
    return resposta

#Chamando a função
print(f'O Triplo do valor é {triplo(8)}')
    
#Chamando a função com valor dinãmico
numero = int(input('Informe um valor: '))    
print(f'O Triplo do valor é{triplo(numero)}')
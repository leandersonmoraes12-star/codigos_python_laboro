# Tupla = Conjunto de dados
# Criando uma tupla - representado por ()
# p ramge sempre cria uma lista numérica - range(0,4)
# a tupla é imutável
frutas = ("Banana","Uva","Morango","Açerola",)

#print(type(frutas))

print(frutas)

frutas[2] = "Manga" # Aqui teremos um erro

print(frutas[2])

# Exibir todas as frutas

for item in frutas:
    print(item)
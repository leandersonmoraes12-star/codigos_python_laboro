# Trabalhando com o modo:
# 'a' ->(append) Adiciona conteúdo no final do arquivo

# Abrindo o arquivo em modo de escrita
arquivo = open("frutas.txt","a")

arquivo.write("Goiaba\n")
arquivo.write("Jambo\n")
arquivo.write("Pitanga\n")


arquivo.close()
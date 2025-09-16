##Testar se uma palavra é um palíndromo

# 1. Pedir a palavra para o usuário
palavra = input("Digite uma palavra: ")

# 2. Transformar a palavra toda em letras minúsculas
# (assim não dá problema se digitar "Radar" ou "RADAR")
palavra = palavra.lower()

# 3. Inverter a palavra
# [::-1] é um "truque" do Python para ler a string de trás pra frente
inversa = palavra[::-1]

# 4. Comparar se a palavra original é igual à invertida
if palavra == inversa:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")

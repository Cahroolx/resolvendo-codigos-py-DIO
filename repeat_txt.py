## Receber uma string e um número inteiro e depois retornar a string repetindo o número de vezes informado.
palavra = input("Informe a palavra desejada: ")
num = int(input("Informe o número desejado: "))

repeat = (palavra + " ") * num

print(repeat)
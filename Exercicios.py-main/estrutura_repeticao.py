texto = input("Informe um texto:")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()
    print("Executa no final do laço")

#range
for numero in range(0, 51, 5):
    print(numero, end=" ")


#while

while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break

    if numero % 2 == 0:
        continue

    

    print(numero)

  
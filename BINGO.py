import random

# Aquí creo la función llamada menu sin argumentos
def menu():
    entrada = input("Digite Un Número Del 1 Al 100 O 'S' Para Salir: ")
    if entrada != "s" and entrada != "S":
        if entrada.isdigit() and 1 <= int(entrada) <= 100:
            return entrada
        else:
            print("Número Fuera De Rango O Inválido.")
            return None
    else:
        print("Saliendo Del Programa...")
        return "s"

def funcion2():
    a = 1

entrada = "0"
contador = 0
tarjeton = [0] * 10
repetido = False

print("Bienvenido Al Bingo De Miguelinho")
print("Ingrese Hasta Llenar Su Tarjetón Con 10 Números Del 1 Al 100")

# Fase de ingreso de números del tarjetón
while True:
    entrada = menu()

    if entrada == "s":
        break
    elif entrada is None:
        continue

    entradaint = int(entrada)

    if entradaint >= 1 and entradaint <= 100:
        repetido = False
        for i in range(0, contador):
            if tarjeton[i] == entradaint:
                print("El Valor Que Usted Ingresó Ya Se Encuentra En El Tarjetón Con Valor:", entradaint)
                repetido = True
                break

        if not repetido:
            tarjeton[contador] = entradaint
            contador += 1
            print("Han Ingresado Un Total De", contador, "Números.")
        else:
            print("Ya Tiene Ese Número En El Tarjetón. Intente Con Otro.")

        if contador == 10:
            print("Tarjetón Lleno. Sus Números Son:", tarjeton)
            break

# Sorteo automático activado con Enter
print("\nIniciando Sorteo. Presione Enter Para Sacar Cada Número.")

aciertos = 0
numeros_sorteados = []

while aciertos < 10:
    sorteo = input("Presione Enter Para Sacar Un Número: ")
    if sorteo != "":
        print("No Es Necesario Escribir Nada. Solo Presione Enter.")
        continue

    numero = random.randint(1, 100)
    while numero in numeros_sorteados:
        numero = random.randint(1, 100)
    numeros_sorteados.append(numero)

    print("Número Sorteado:", numero)

    if numero in tarjeton:
        aciertos += 1
        print("El Número", numero, "Está En Su Tarjetón. Aciertos:", aciertos, "De 10")
    else:
        print("Ese Número No Está En Su Tarjetón.")

print("\nBingo Completado. Usted Ha Adivinado Los 10 Números.")
print("Gracias Por Jugar Al Bingo De Miguelinho")
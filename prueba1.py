#! media de algo
import random
def media():
    a=int(input("Ingrese un numero: "))
    b=int(input("Ingrese segundo numero: "))

    media = (a+b) / 2
    print(f"La media de {a} y {b} es: {media}")
    return

    print("Programa finalizado.")

media()


def listaRandom():
    print(random.choice(["gominola","trebol","bombon"]))
    print(random.choice(range(14)))
    print(random.choice((14,24,19)))

listaRandom()


def numeroMayor():
    primero = float(input("Escriba un número: "))
    segundo = float(input(f"Escriba un número mayor que {primero}: "))

    while segundo > primero:
        segundo = float(input(f"Escriba un número mayor que {primero}: "))

    print()
    print(f"{segundo} no es mayor que {primero}.")

numeroMayor()


def cuentaPares():
    
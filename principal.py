"""Modulo generado para obtener el turno"""
from num.numeros import siguiente_turno, perfumeria, farmacia, cosmeticos

while True:
    opcion = input("A qué área desea dirigirse? P-Perfumería, F-Farmacia, C-Cosméticos: ")
    if opcion.upper() == "P":
        print(siguiente_turno(perfumeria))
    elif opcion.upper() == "F":
        print(siguiente_turno(farmacia))
    elif opcion.upper() == "C":
        print(siguiente_turno(cosmeticos))
    else:
        print("Opción inválida")
        continue

    continuar = input("Desea sacar otro turno? S/N: ")
    if continuar.upper() != "S":
        break

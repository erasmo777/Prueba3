import csv
import funciones
op= 0
while op != 5:
    print("¡Bienvenido!")
    print("[1]-Agregar productos al inventario")
    print("[2]-Leer inventario")
    print("[3]-Clasificar y exportar productos")
    print("[4]-Salir")
    op=input("Seleccione una opcion: ")
    if op == "1":
        funciones.opcion1()
    if op == "2":
        funciones.opcion2()
    if op == "3":
        funciones.opcion3()
    if op == "4":
        print("")
        print("Usted ha salido")
        print("")
        break
        

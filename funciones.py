import csv
def opcion1():
    id= int(input("Ingresar ID del producto: "))
    nombre= input("Ingresar nombre del producto: ")
    categoria= input("Ingresar categoria del producto: ")
    precio= int(input("Ingresar precio del producto: "))
    with open('inventario.csv','a', newline='') as archivocsv:
        escribir= csv.writer(archivocsv)
        escribir.writerow(["ID","Nombre","Categoria","Precio"])
        escribir.writerow([id,nombre,categoria,precio])

   

def opcion2():
    with open('inventario.csv','r', newline='') as archivocsv:
        leer= csv.reader(archivocsv)
        for fila in leer:
            print(fila)
            


def opcion3():
    with open('inventario.csv','r', newline='') as archivocsv:
        leer= csv.reader(archivocsv)
        electronica= []
        textil= []
        calzado= []
        for categoria in leer:
            if categoria[2]== 'electronica':
                electronica.append(categoria)
            elif categoria[2]=='textil':
                textil.append(categoria)
            elif categoria[2]=='calzado':
                calzado.append(categoria)
    with open('clasificacion_productos.txt','w', newline='') as archivoclasi:
        archivoclasi.write('electronica: ')
        for elemento in electronica:
            archivoclasi.write(str(elemento))
        archivoclasi.write('\ntextil: ')
        for elemento in textil:
            archivoclasi.write(str(elemento))
        archivoclasi.write('\ncalzado: ')
        for elemento in calzado:
            archivoclasi.write(str(elemento))
    print("")
    print("Archivo generado con exito.")
    print("")
        
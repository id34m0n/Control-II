#Jeremy Iron Mancilla Cavada - 
def AgregarNota(anot):
    listaNotas.append(float(input("Ingrese Nota: ")))
    listaNombre.append(input("Ingrese Nombre de la Nota: "))
    print("Ingrese Fecha")
    listaDia.append(input("Ingrese Dia: "))
    listaMes.append(input("Ingrese Mes: "))
    listaAño.append(input("Ingrese Año: "))
    listaDesc.append(input("Ingrese Descripcion: "))

def MostrarNotas(mnot):
    mostrar = print("Las Notas son: ",listaNotas)

def BuscarNota(bnot):
    buscar = input("Ingrese Nombre de la Nota: ")
    for i in (bnot):
        if i == buscar:
            print("asd")

listaNotas = []
listaNombre = []
listaDia = []
listaMes = []
listaAño = []
listaFecha = [listaDia, listaMes, listaAño]
listaDesc =[]
listaTotal = [listaNotas, listaNombre, listaFecha, listaDesc]

print("*****MENU*****")
print("\nOpciones")
print("1)Agregar una nota")
print("2)Visualizar una Nota")
print("3)Buscar Nota")
opcion = int(input("Ingrese una Opcion: "))

while opcion != 4:
    if opcion == 1:
        print("AGREGAR UNA NOTA")
        AgregarNota(listaNotas)
        break
    elif opcion == 2:
        print("VISUALIzAR UNA NOTA")
        MostarNotas(listaNotas)
        break
    elif opcion == 3:
        BuscarNota(listaTotal)
        break
    else:
        print("Nos Vemos")

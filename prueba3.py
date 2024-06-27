print("librería diosito salvanos")

listaGenero=['ficción', 'No ficción', 'ciencia']

#print("1. Registrar libro") #título, autor, género, precio.
#print("2. Listar todos los libros") #print libros registrados.
#print("3. Registrar venta") #titulo libro, cantidad vendida, precio por unidad, precio final.
#print("5. Generar txt") #hacer un txt haha.
#print("6. Salir del programa")


titulo=""
autor=""
genero=""
precio=""
cantidad=""
preciocu=""
preciof=""
LibrosLOL=[titulo, autor, genero, precio]
Registroo=[titulo, cantidad, preciocu, preciof]


def RegistrarLibro():
    LibrosLOL.append()
    titulo=input("titulo: ")
    autor=input("autor: ")
    genero=input("genero: ")
    try:
        precio=int(input("precio "))
    except:
        print("números por favor")
    print(LibrosLOL)

def ListarLibros():
    print(LibrosLOL)

def RegistroVenta():
    Registroo.append()
    titulo=input("titulo: ")
    cantidad=input("cantidad: ")
    preciocu=input("precio por unidad: ")
    preciof=input("precio final: ")

def ReporteVentas():
    print(listaGenero)

while True:
    print("1. Registrar libro") #título, autor, género, precio.
    print("2. Listar todos los libros") #print libros registrados.
    print("3. Registrar venta") #titulo libro, cantidad vendida, precio por unidad, precio final.
    print("4. Imprimir reporte de ventas") #generos ig
    print("5. Generar txt") #hacer un txt haha.
    print("6. Salir del programa")
    op=input("ingrese opción: ")
    if op==1:
        RegistrarLibro()
    elif op==2:
        ListarLibros()
    elif op==3:
        RegistroVenta()
    elif op==4:
        ReporteVentas()
    elif op==5:
        print("del 1 no me salva nadie, fue un gusto")
    elif op==6:
        break
nominaTrabajadores = []
cargos = ("CEO","DESARROLLADOR","ANALISTA DE DATOS")
DESCUENTO_SALUD = 0.07
DESCUENTO_AFP = 0.12

def registrarTrabajador():
    nombre = input("INGRESE NOMBRE: ")
    #CARGO
    print("CARGOS DISPONIBLES")
    print("------------------")
    for i in range(len(cargos)):
        print(i,cargos[i])
    posicionCargo = int(input("SELECCIONE POSICIÓN DE CARGO "))
    cargo = cargos[posicionCargo]
    sueldoBruto = int(input("INGRESE SUELDO BRUTO $"))
    descuentoSalud = int(sueldoBruto*DESCUENTO_SALUD)
    descuentoAfp = int(sueldoBruto * DESCUENTO_AFP)
    liquidoPagar = sueldoBruto - descuentoSalud-descuentoAfp
    trabajador = [nombre,cargo, sueldoBruto,descuentoSalud,descuentoAfp,liquidoPagar]
    nominaTrabajadores.append(trabajador)


def listarTrabajador():
    print("TRABAJADOR\tCARGO\tSUELDO BRUTO\tDESC.SALUD\tDESC.AFP\tLÍQUIDO A PAGAR")
    print("----------------------------------------------------------------------")
    for i in range(len(nominaTrabajadores)):
        print(nominaTrabajadores[i][0],end="\t\t")
        print(nominaTrabajadores[i][1],end="\t\t")
        print(nominaTrabajadores[i][2],end="\t\t")
        print(nominaTrabajadores[i][3],end="\t\t")
        print(nominaTrabajadores[i][4],end="\t\t")
        print(nominaTrabajadores[i][5],end="\t\t")
        print()
        print("-----------------------------------------------------------------")



def imprimirPlanillaSueldos():
    op = int(input("(1)MOSTRAR TODOS LOS CARGOS (2)MOSTRAR UN CARGO ESPECÍFICO "))
    if op ==1:
        print("TRABAJADOR\tCARGO\tSUELDO BRUTO\tDESC.SALUD\tDESC.AFP\tLÍQUIDO A PAGAR")
        print("----------------------------------------------------------------------")
        for i in range(len(nominaTrabajadores)):
            print(nominaTrabajadores[i][0],end="\t\t")
            print(nominaTrabajadores[i][1],end="\t\t")
            print(nominaTrabajadores[i][2],end="\t\t")
            print(nominaTrabajadores[i][3],end="\t\t")
            print(nominaTrabajadores[i][4],end="\t\t")
            print(nominaTrabajadores[i][5],end="\t\t")
            print()
            print("-----------------------------------------------------------------")

    elif op==2:
        cargoBuscar = input("INGRESE CARGO A BUSCAR ")
        if cargoBuscar in cargos:
            print("CARGO EXISTENTE")
            posicionCargo = cargos.index(cargoBuscar)
            cargoSeleccionado= cargos[posicionCargo]
            print(f"TRABAJADORES EN EL CARGO {cargoBuscar}")

            for trabajador in nominaTrabajadores:
                if trabajador[1] == cargoSeleccionado:
                    print(trabajador[0], end="\t\t")
                    print(trabajador[1], end="\t\t")
                    print(trabajador[2], end="\t\t")
                    print(trabajador[3], end="\t\t")
                    print(trabajador[4], end="\t\t")
                    print(trabajador[5], end="\t\t")
                    print()
                    print("-----------------------------------------------------------------")
        else:
            print("CARGO NO EXISTE")


while True:
    print("(1)REGISTRAR TRABAJADOR")
    print("(2)LISTAR TODO LOS TRABAJADORES")
    print("(3)IMPRIMIR PLANILLA DE SUELDOS")
    print("(4)SALIR")

    opcion = int(input("INGRESE OPCIÓN "))

    if opcion==1:
        registrarTrabajador()
    elif opcion==2:
        listarTrabajador()
    elif opcion==3:
        imprimirPlanillaSueldos()
    elif opcion ==4:
        break



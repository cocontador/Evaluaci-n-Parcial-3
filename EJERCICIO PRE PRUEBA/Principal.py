import Funciones as fn

trabajadores=[]
while True: 
    print("Bienvenidos al super sistema de pago de sueldos")
    print("1. Registrar trabajador")
    print("2. Listar los trabajadores")
    print("3. Imprimir planilla de sueldos")
    print("4. Salir del programa")
   
    opcion=int(input("Ingrese una opción: "))

    if opcion==1:
        fn.registrar_trabajador(trabajadores)
    elif opcion==2:
        fn.listar_trabajadores(trabajadores)
    elif opcion==3:
        fn.imprimir_plantilla(trabajadores)
    
    elif opcion==4:
        break
    else: 
         print("Opción no válida, seleccione nuevamente")


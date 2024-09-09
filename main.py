eventos = []
tareas = []

base_de_datos_usuarios = []
base_de_datos_contraseñas = []

def insertar_eventos():
    # Funcion que inserta eventos o Tareas.
    evento_usuario = True
    while evento_usuario:
        print("Que quiere insertar?:")
        print("""
    (1) Para insertar un Evento
    (2) Para insertar una Tarea
    """)
        tarea_evento = int(input())
        if tarea_evento == 1:
            print("Ingrese un nuevo Evento:")
            evento_usuario = input("")
            eventos.append(evento_usuario)
            print("---------------------------------")
            print("| Evento Guardado ¡Exitosamente!|")
            print("---------------------------------\n")
        elif tarea_evento == 2:
            print("Ingrese una nueva Tarea:")
            tarea_usuario = input("")
            tareas.append(tarea_usuario)
            print("--------------------------------")
            print("| Tarea Guardada ¡Exitosamente!|")
            print("--------------------------------\n")
        else:
            print("Por favor elija una opcion valida, Gracias")

        print("Desea seguir agregando eventos o tareas? escriba 'si' o 'no'")
        sigue = input("").lower()

        if sigue != "si":
            evento_usuario = False
    

def eliminar_eventos():
    # Funcion que elimina registros
    print("Que quiere Eliminar?:")
    print("""
    (1) Para eliminar un Evento
    (2) Para eliminar una Tarea
    """)
    tarea_evento_eliminar = int(input())
    if tarea_evento_eliminar == 1:
        if len(eventos) != 0:
            print(f"Eventos que puedes eliminar:")
            for id_even, evento in enumerate (eventos):
                print(f"{id_even + 1}. {evento}")

            print("\nIngrese el numero de evento a eliminar:")
            seleccion = int(input()) -1 # convierte en indice la seleccion con -1
            evento_eliminado = eventos.pop(seleccion)
            print(f"Se ha eliminado el evento {evento_eliminado}")
        else:
            print("---------------------------------")
            print("| ¡No hay eventos que eliminar! |")
            print("---------------------------------")
    elif tarea_evento_eliminar == 2:
        if len(tareas) != 0:
            print(f"Tareas que puedes eliminar:")
            for id_tarea, tarea in enumerate (tareas):
                print(f"{id_tarea + 1}. {tarea}")

            print("\nIngrese el numero de evento a eliminar:")
            seleccion = int(input()) -1 # convierte en indice la seleccion con -1
            tarea_eliminada = tareas.pop(seleccion)
            print(f"Se ha eliminado la tarea {tarea_eliminada}")
        else:
            print("---------------------------------")
            print("| ¡No hay tareas que eliminar! |")
            print("---------------------------------")
    else:
        print("por favor elija una opcion valida, Gracias")
    
def modificar_eventos():
    # Funcion que modifica eventos
    print("Modificar")

def ver_eventos_pendientes():
    # Funcion para ver registros en memoria
    if len(eventos) != 0 or len(tareas) != 0:
        print(f"\nEventos registrados:")
        for id_even, evento in enumerate (eventos):
            print(f"{id_even + 1}. {evento}")
        
        print("\nTareas registradas:")
        for id_tarea, tarea in enumerate(tareas):
            print(f"{id_tarea +1}. {tarea}")
    
    else:
        print("-----------------------------------------")
        print("| ¡No hay eventos o tareas registrados! |")
        print("-----------------------------------------")

def register():
    # Registro de usuarios
    print("\n¡Registrese!\n")
    register_ususario = input("Ingrese su nombre para registrarse):\n").lower().capitalize()
    register_contra = input("Ingrese se apellido:\n").lower().capitalize()
    base_de_datos_usuarios.append(register_ususario)
    base_de_datos_contraseñas.append(register_contra)
    print("-------------------------------------")
    print("| Usuario Registrado ¡Exitosamente! |")
    print("-------------------------------------")
    

def login():
    # Inicio de sesion a la aplicación
    print("\nInicio de sesión\n")
    username = input("Ingrese su nombre para iniciar sesión):\n").lower().capitalize()
    password = input("Ingrese se apellido:\n").lower().capitalize()

    if username in base_de_datos_usuarios and password in base_de_datos_contraseñas: 
        print("-----------------------------")
        print("| Inicio de Sesión ¡Exitoso! |")
        print("-----------------------------")       
        return username
    else:
        print("\n----------------------------------------------------------------------------")
        print("Su Nombre o Apellido no se encuentra en la base de datos, Vuelva a intentarlo")
        return None



#################### Aplicación ###################

def menu_principal():
    # Funcion que maneja el menu principal de la app
    opcion = 0
    while opcion != 3:
        print("\n--- Menú Principal ---")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Salir")
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            register()
        elif opcion == 2:
            username = login()
            if username:
                menu_usuario(username)
        elif opcion == 3:
            print("\n----------------------------------------------------------")
            print("Saliendo de la aplicación... ¡Gracias por usar EvenPlus!\n")
        else:
            print("Opción inválida. Intente de nuevo.")




def menu_usuario(username):
    # El usuario logeado debera elegir la accion que desee.
    usuario_main = 0
    while usuario_main != 5:
        print(f"""
    Bienvenido ({username}) a EvenPLus tu app para gestionar tareas y eventos.
    Elija la acción que desee:
    (1) Insertar un Evento
    (2) Eliminar un Evento
    (3) Modificar un Evento
    (4) Ver Eventos guardados
    (5) Cerrar sesión
    """)
        
        usuario_main = int(input("Ingrese el numero de la accion que desea realizar: "))
        if usuario_main == 1:
            # def insertar
            insertar_eventos()

        elif usuario_main == 2:
            # def eliminar
            eliminar_eventos()

        elif usuario_main == 3:
            # def modificar
            modificar_eventos()
            
        elif usuario_main == 4:
            # def ver registros
            ver_eventos_pendientes()
        
        elif usuario_main == 5:
                print("\n-------------------------------")
                print("Cerrando sesión, ¡Vuelva Pronto!\n")

        else:
            print("¡Error!, Por favor ingrese un numero del 1 al 5 ")

menu_principal()
"""
Faltantes
"""

# Update de def ingresar_eventos:
#   1 - pide fecha de evento en tipo de registro eventos.

# Update de def ver_eventos_pendientes:
#   1 - ver detalles de eventos

# Memoria de la app

# def modificar_evento
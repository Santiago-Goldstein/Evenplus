# Usuario duro admin
usuarios = {
    "Admin": {
        "username": "Admin",
        "password": "Admin",
        "eventos": [
            {"titulo": "Cumpleaños de Agus", "fecha_limite": "25-08-24"},
            {"titulo": "Cumpleaños Abuela", "fecha_limite": "14-09-24"}
        ],
        "tareas": [
            {"titulo": "Juega River", "fecha_limite": "15-08-24"},
            {"titulo": "Juega Seleccion", "fecha_limite": "05-10-24"}
        ]
    }
}


def insertar_eventos(username):
    # Inserta eventos o tareas para el usuario logueado
    evento_usuario = True
    while evento_usuario:
        print("¿Qué quiere insertar?:")
        print("""
    (1) Para insertar un Evento
    (2) Para insertar una Tarea
    """)
        tarea_evento = int(input())
        
        if tarea_evento == 1:
            print("Ingrese el título del evento:")
            titulo_evento = input("").lower().capitalize()
            print("Ingrese la fecha límite del evento (Dia-Mes-Año):")
            fecha_limite = input("")
            usuarios[username]['eventos'].append({
                "titulo": titulo_evento,
                "fecha_limite": fecha_limite
            })
            print(f"Evento '{titulo_evento}' guardado exitosamente.")

        elif tarea_evento == 2:
            print("Ingrese el título de la tarea:")
            titulo_tarea = input("").lower().capitalize()
            print("Ingrese la fecha límite de la tarea (Dia-Mes-Año):")
            fecha_limite = input("")
            usuarios[username]['tareas'].append({
                "titulo": titulo_tarea,
                "fecha_limite": fecha_limite
            })
            print(f"Tarea '{titulo_tarea}' guardada exitosamente.")
        
        else:
            print("Por favor elija una opción válida.")

        print("¿Desea seguir agregando eventos o tareas? escriba 'si' o 'no'")
        sigue = input("").lower()

        if sigue != "si":
            evento_usuario = False

    

def eliminar_eventos(username):
    print("¿Qué quiere eliminar?:")
    print("""
    (1) Para eliminar un Evento
    (2) Para eliminar una Tarea
    """)
    tarea_evento_eliminar = int(input())

    if tarea_evento_eliminar == 1:
        if len(usuarios[username]['eventos']) != 0:
            print("Eventos que puedes eliminar:")
            for id_even, evento in enumerate(usuarios[username]['eventos']):
                print(f"{id_even + 1}. {evento['titulo']} - {evento['fecha_limite']}")

            print("\nIngrese el número de evento a eliminar:")
            seleccion = int(input()) - 1
            evento_eliminado = usuarios[username]['eventos'].pop(seleccion)
            print(f"Se ha eliminado el evento '{evento_eliminado['titulo']}'")
        else:
            print("No hay eventos que eliminar.")

    elif tarea_evento_eliminar == 2:
        if len(usuarios[username]['tareas']) != 0:
            print("Tareas que puedes eliminar:")
            for id_tarea, tarea in enumerate(usuarios[username]['tareas']):
                print(f"{id_tarea + 1}. {tarea['titulo']} - {tarea['fecha_limite']}")

            print("\nIngrese el número de tarea a eliminar:")
            seleccion = int(input()) - 1
            tarea_eliminada = usuarios[username]['tareas'].pop(seleccion)
            print(f"Se ha eliminado la tarea '{tarea_eliminada['titulo']}'")
        else:
            print("No hay tareas que eliminar.")
    else:
        print("Por favor elija una opción válida.")

    
def modificar_eventos():
    # Funcion que modifica eventos
    print("Modificar")

def ver_eventos_pendientes(username):
    # Muestra los eventos y tareas del usuario logueado
    if len(usuarios[username]['eventos']) != 0 or len(usuarios[username]['tareas']) != 0:
        print(f"\nEventos registrados de {username}:")
        for id_even, evento in enumerate(usuarios[username]['eventos']):
            print(f"{id_even + 1}. {evento['titulo']} - {evento['fecha_limite']}")
        
        print(f"\nTareas registradas de {username}:")
        for id_tarea, tarea in enumerate(usuarios[username]['tareas']):
            print(f"{id_tarea + 1}. {tarea['titulo']} - {tarea['fecha_limite']}")
    
    else:
        print("No hay eventos o tareas registrados.")

def register():
    print("\n¡Regístrese!\n")
    register_usuario = input("Ingrese su nombre para registrarse: ").lower().capitalize()
    register_contra = input("Ingrese su contraseña: ").lower().capitalize()

    usuarios[register_usuario] = {
        "username": register_usuario,
        "password": register_contra,
        "eventos": [],
        "tareas": []
    }

    print("Usuario registrado exitosamente.")

    

def login():
    # Inicio de sesión a la aplicación
    print("\nInicio de sesión\n")
    username = input("Ingrese su nombre para iniciar sesión:\n").lower().capitalize()
    password = input("Ingrese su contraseña:\n").lower().capitalize()

    # Verificamos si el usuario existe en el diccionario
    for usuario, datos in usuarios.items():
        if datos['username'] == username and datos['password'] == password:
            print("-----------------------------")
            print("| Inicio de Sesión ¡Exitoso! |")
            print("-----------------------------")
            return usuario  # Retorna la clave del usuario en el diccionario
    
    # Si no se encuentra el usuario o contraseña no coinciden
    print("\n----------------------------------------------------------------------------")
    print("Su Nombre o Contraseña no se encuentra en la base de datos, Vuelva a intentarlo")
    return None


#################### Aplicación ###################

def menu_principal():
    # Menú principal de la aplicación
    opcion = 0
    while opcion != 3:
        print("\n--- Menú Principal ---")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Salir")
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            register()  # Llamamos a la función de registro

        elif opcion == 2:
            usuario_logeado = login()  # Llamamos a la función login y obtenemos la clave del usuario

            if usuario_logeado:
                menu_usuario(usuario_logeado)  # Si el login es exitoso, vamos al menú de usuario

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
            insertar_eventos(username)

        elif usuario_main == 2:
            # def eliminar
            eliminar_eventos(username)

        elif usuario_main == 3:
            # def modificar
            modificar_eventos(username)
            
        elif usuario_main == 4:
            # def ver registros
            ver_eventos_pendientes(username)
        
        elif usuario_main == 5:
                print("\n-------------------------------")
                print("Cerrando sesión... ¡Vuelva Pronto!\n")

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
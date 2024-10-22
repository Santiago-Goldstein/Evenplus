import json
from colorama import Fore, init
from rich.console import Console
from pyfiglet import figlet_format

init(autoreset=True)
console = Console()

def cargar_datos():
    """ Cargar datos desde el archivo JSON """
    try:
        with open("C:/Users/santi/Desktop/Evenplus/evenplus.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}


def guardar_datos():
    """ Guardar datos en el archivo JSON """
    with open("C:/Users/santi/Desktop/Evenplus/evenplus.json", "w") as archivo:
        json.dump(usuarios, archivo, indent=4)

usuarios = cargar_datos()

def agregar_a_historial(username, tipo, titulo, fecha_limite, descripcion):
    """ Agrega un nuevo registro al historial del usuario """
    usuarios[username]['historial'].append([tipo, titulo, fecha_limite, descripcion])


def insertar_eventos(username):
    """ Inserta eventos o tareas para el usuario logueado """
    evento_usuario = True
    while evento_usuario:
        print("¿Qué quiere insertar?:")
        print("""
    (1) Para insertar un Evento
    (2) Para insertar una Tarea
    """)
        tarea_evento = int(input())
        
        if tarea_evento == 1:
            print("Ingrese el nombre del evento:")
            titulo_evento = input("").lower().capitalize()
            print("Ingrese la fecha del evento (Dia-Mes-Año):")
            fecha_limite = input("")
            print("Ingrese la descripción del evento:")
            descripcion = input("")
            usuarios[username]['eventos'].append({
                "titulo": titulo_evento,
                "fecha_limite": fecha_limite,
                "descripcion": descripcion
            })

            agregar_a_historial(username, "Evento", titulo_evento, fecha_limite, descripcion)  # Agregar al historial
            guardar_datos()  # Guardar cambios
            print(f"Evento '{titulo_evento}' guardado exitosamente.")

        elif tarea_evento == 2:
            print("Ingrese el nombre de la tarea:")
            titulo_tarea = input("").lower().capitalize()
            print("Ingrese la fecha de la tarea (Dia-Mes-Año):")
            fecha_limite = input("")
            print("Ingrese la descripción de la tarea:")
            descripcion = input("")
            usuarios[username]['tareas'].append({
                "titulo": titulo_tarea,
                "fecha_limite": fecha_limite,
                "descripcion": descripcion
            })

            agregar_a_historial(username, "Tarea", titulo_tarea, fecha_limite, descripcion)  # Agregar al historial
            guardar_datos()  # Guardar cambios     
            print(f"Tarea '{titulo_tarea}' guardada exitosamente.")
        else:
            print("Por favor elija una opción válida.")

        print("¿Desea seguir agregando eventos o tareas? escriba 'si' o 'no'")
        sigue = input("").lower()

        if sigue != "si":
            evento_usuario = False


def modificar_eventos(username):
    """ Te permite modificar eventos, tareas y descripciones """
    print("¿Qué quiere modificar?:")
    print("""
    (1) Para modificar un Evento
    (2) Para modificar una Tarea
    """)
    tarea_evento_modificar = int(input())

    if tarea_evento_modificar == 1:
        if len(usuarios[username]['eventos']) != 0:
            print("Eventos que puedes modificar:")
            for id_even, evento in enumerate(usuarios[username]['eventos']):
                print(f"{id_even + 1}. {evento['titulo']} - {evento['fecha_limite']} - {evento['descripcion']}")

            print("\nIngrese el número del evento a modificar:")
            seleccion = int(input()) - 1
            evento_seleccionado = usuarios[username]['eventos'][seleccion]
            
            print("¿Qué desea modificar?")
            print("""
            (1) Título
            (2) Fecha límite
            (3) Descripción
            """)
            opcion_modificar = int(input())

            if opcion_modificar == 1:
                nuevo_titulo = input("Ingrese el nuevo título: ").lower().capitalize()
                evento_seleccionado['titulo'] = nuevo_titulo
                guardar_datos()  # Guardar cambios
                print(f"Título del evento actualizado a '{nuevo_titulo}'")

            elif opcion_modificar == 2:
                nueva_fecha = input("Ingrese la nueva fecha límite (Dia-Mes-Año): ")
                evento_seleccionado['fecha_limite'] = nueva_fecha
                guardar_datos()  # Guardar cambios
                print(f"Fecha límite del evento actualizada a '{nueva_fecha}'")

            elif opcion_modificar == 3:
                nueva_descripcion = input("Ingrese la nueva descripción: ")
                evento_seleccionado['descripcion'] = nueva_descripcion
                guardar_datos()  # Guardar cambios
                print(f"Descripción del evento actualizada a '{nueva_descripcion}'")
            
        else:
            print("No hay eventos que modificar.")

    elif tarea_evento_modificar == 2:
        if len(usuarios[username]['tareas']) != 0:
            print("Tareas que puedes modificar:")
            for id_tarea, tarea in enumerate(usuarios[username]['tareas']):
                print(f"{id_tarea + 1}. {tarea['titulo']} - {tarea['fecha_limite']} - {tarea['descripcion']}")

            print("\nIngrese el número de la tarea a modificar:")
            seleccion = int(input()) - 1
            tarea_seleccionada = usuarios[username]['tareas'][seleccion]
            
            print("¿Qué desea modificar?")
            print("""
            (1) Título
            (2) Fecha límite
            (3) Descripción
            """)
            opcion_modificar = int(input())

            if opcion_modificar == 1:
                nuevo_titulo = input("Ingrese el nuevo título: ").lower().capitalize()
                tarea_seleccionada['titulo'] = nuevo_titulo
                guardar_datos()  # Guardar cambios
                print(f"Título de la tarea actualizado a '{nuevo_titulo}'")

            elif opcion_modificar == 2:
                nueva_fecha = input("Ingrese la nueva fecha límite (Dia-Mes-Año): ")
                tarea_seleccionada['fecha_limite'] = nueva_fecha
                guardar_datos()  # Guardar cambios
                print(f"Fecha límite de la tarea actualizada a '{nueva_fecha}'")

            elif opcion_modificar == 3:
                nueva_descripcion = input("Ingrese la nueva descripción: ")
                tarea_seleccionada['descripcion'] = nueva_descripcion
                guardar_datos()  # Guardar cambios
                print(f"Descripción de la tarea actualizada a '{nueva_descripcion}'")
            
        else:
            print("No hay tareas que modificar.")
    else:
        print("Por favor elija una opción válida.")


    

def eliminar_eventos(username):
    """ Te permite eliminar eventos o tareas """
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
            guardar_datos()  # Guardar cambios
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
            guardar_datos()  # Guardar cambios
            print(f"Se ha eliminado la tarea '{tarea_eliminada['titulo']}'")
        else:
            print("No hay tareas que eliminar.")
    else:
        print("Por favor elija una opción válida.")

    

def ver_eventos_pendientes(username):
    """ Muestra los eventos y tareas del usuario logueado """
    if len(usuarios[username]['eventos']) != 0 or len(usuarios[username]['tareas']) != 0:
        print(f"\nEventos registrados de {username}:")
        for id_even, evento in enumerate(usuarios[username]['eventos']):
            print(f"{id_even + 1}. {evento['titulo']} - {evento['fecha_limite']} - {evento['descripcion']}")
        
        print(f"\nTareas registradas de {username}:")
        for id_tarea, tarea in enumerate(usuarios[username]['tareas']):
            print(f"{id_tarea + 1}. {tarea['titulo']} - {tarea['fecha_limite']} - {tarea['descripcion']}")
    
    else:
        console.print("\n[bold red]---------------------------------------[/bold red]")
        console.print("[bold red]| No hay eventos o tareas registrados |[/bold red]")
        console.print("[bold red]---------------------------------------[/bold red]\n")


def ver_proximos_eventos_lambda(username):
    print(f"\nFunción en desarrollo: Próximos eventos de {username}")
    obtener_evento = lambda eventos, tareas: eventos[0] if eventos else (tareas[0] if tareas else None)
    proximo = obtener_evento(usuarios[username]['eventos'], usuarios[username]['tareas'])

    """ Mostrar eventos próximos """
    if proximo:
        print(f"Próximo evento/tarea: {proximo['titulo']} - {proximo['fecha_limite']} - {proximo['descripcion']}")
    else:
        console.print("\n[bold red]---------------------------------------[/bold red]")
        console.print("[bold red]| No hay eventos o tareas registrados |[/bold red]")
        console.print("[bold red]---------------------------------------[/bold red]\n")


def ver_historial(username):
    """ Funcion que muestra el historial de el usuario logueado """
    if len(usuarios[username]['historial']) != 0:
        print("\nHistorial de Eventos y Tareas:")
        for registro in usuarios[username]['historial']:
            tipo, titulo, fecha_limite, descripcion = registro
            print(f"{tipo}: {titulo} - {fecha_limite} - {descripcion}")
    else:
        console.print("\n[bold red]--------------------[/bold red]")
        console.print("[bold red]| No hay historial |[/bold red]")
        console.print("[bold red]--------------------[/bold red]\n")


def register():
    """ Funcion para registrarse en la app """
    print("\n¡Regístrese!\n")
    register_usuario = input("Ingrese un usuario para registrarse: ").lower().capitalize()
    register_contra = input("Ingrese una contraseña: ").lower().capitalize()

    usuarios[register_usuario] = {
        "username": register_usuario,
        "password": register_contra,
        "eventos": [],
        "tareas": [],
        "historial": []
    }
    guardar_datos()  # Guardar cambios
    console.print("[bold green]\n-----------------------------------[/bold green]")
    console.print("[bold green]| Usuario registrado exitosamente |[/bold green]")
    console.print("[bold green]-----------------------------------[/bold green]")

    

def login():
    """ Inicio de sesión a la aplicación """
    print("\nInicio de sesión\n")
    username = input("Ingrese su usuario para iniciar sesión:\n").lower().capitalize()
    password = input("Ingrese su contraseña:\n").lower().capitalize()

    """ Verificamos si el usuario existe en el diccionario """
    for usuario, datos in usuarios.items():
        if datos['username'] == username and datos['password'] == password:
            console.print("[bold green]------------------------------[/bold green]")
            console.print("[bold green]| Inicio de Sesión ¡Exitoso! |[/bold green]")
            console.print("[bold green]------------------------------[/bold green]")
            return usuario  # Retorna la clave del usuario en el diccionario
    
    """ Si no se encuentra el usuario o contraseña no coinciden """
    console.print("\n[bold red]-----------------------------------------------------------------------------------[/bold red]")
    console.print("[bold red]| Su Nombre o Contraseña no se encuentra en la base de datos, Vuelva a intentarlo |[/bold red]")
    console.print("[bold red]-----------------------------------------------------------------------------------[/bold red]")
    print()
    return None


#################### Aplicación ###################

def menu_principal():
    """ Menú principal de la aplicación """
    opcion = 0
    while opcion != 3:
        print(Fore.CYAN + figlet_format("Evenplus App"))
        print(Fore.BLUE + "\n--- Menú Principal ---")
        console.print("[bold green][1] Registrar usuario[/bold green]")
        console.print("[bold yellow][2] Iniciar sesión[/bold yellow]")
        console.print("[bold red][3] Salir[/bold red]")

        opcion = int(input(Fore.BLUE + "Seleccione una opción: "))

        if opcion == 1:
            register()  # Llamamos a la función de registro

        elif opcion == 2:
            usuario_logeado = login()  # Llamamos a la función login y obtenemos la clave del usuario

            if usuario_logeado:
                menu_usuario(usuario_logeado)  # Si el login es exitoso, vamos al menú de usuario

        elif opcion == 3:
            console.print("[bold red]\n------------------------------------------------------------[/bold red]")
            console.print("[bold red]| Saliendo de la aplicación... [bold green]¡Gracias por usar EvenPlus![/bold green] | [/bold red]")
            console.print("[bold red]------------------------------------------------------------[/bold red]")
        
        else:
            console.print("\n[bold red]--------------------------------------[/bold red]")
            console.print("[bold red]| Opción inválida. Intente de nuevo. |[/bold red]")
            console.print("[bold red]--------------------------------------[/bold red]\n")




def menu_usuario(username):
    """ El usuario logeado debera elegir la accion que desee. """
    usuario_main = 0
    while usuario_main != 7:
        print(f"""
    Bienvenido ({username}) a EvenPLus tu App para gestionar tareas y eventos.
    Elija la opción que desee:
    (1) Insertar un Evento
    (2) Eliminar un Evento
    (3) Modificar un Evento
    (4) Ver Eventos Pendientes
    (5) Ver Proximos Eventos 
    (6) Ver Historial
    (7) Cerrar sesión
    """)
        
        usuario_main = int(input("Ingrese el numero de la opción que desea realizar: "))
        if usuario_main == 1:
            """ def insertar """
            insertar_eventos(username)

        elif usuario_main == 2:
            """ def eliminar """
            eliminar_eventos(username)

        elif usuario_main == 3:
            """ def modificar """
            modificar_eventos(username)
            
        elif usuario_main == 4:
            """ def ver eventos pedientes """
            ver_eventos_pendientes(username)
            
        elif usuario_main == 5:
            """ def ver proximos eventos """
            ver_proximos_eventos_lambda(username)

        elif usuario_main == 6:
            """ def ver historial """
            ver_historial(username)
        
        elif usuario_main == 7:
                print("\n-------------------------------")
                print("Cerrando sesión... ¡Vuelva Pronto!\n")

        else:
            console.print("\n[bold red]---------------------------------------------------[/bold red]")
            console.print("[bold red]| ¡Error!, Por favor ingrese un numero del 1 al 7 |[/bold red]")
            console.print("[bold red]---------------------------------------------------[/bold red]")

menu_principal()

"""
Faltantes:

 Update de def ver_eventos_pendientes:
 1 - Ver detalles de eventos
 Memoria de la app (archivo externo json)
 implementarle alguna lógica que te permita ver los días restantes hasta el evento, tarea próximo, usando la fecha actual, en la que interviene el usuario. Ver próximo evento. (Datetime)
 Implementar expresiones regulares en registro. (Requerimientos para el usuario y la contraseña) (patrón)
 Embellecimiento del código, cadena de caracteres (comentarios del código)
 Ver eventos completados
"""

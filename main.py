import json
from colorama import Fore, init
from rich.console import Console
from pyfiglet import figlet_format
import os
import re

init(autoreset=True)
console = Console()

# Obtener el directorio base del proyecto (donde se encuentra main.py)
base_dir = os.path.dirname(os.path.abspath(__file__))

# Ruta al archivo JSON en la misma carpeta
json_path = os.path.join(base_dir, 'evenplus.json')


def validar_contrasena(contrasena):
    """Validar que la contraseña tenga exactamente 5 caracteres y 1 número"""
    patron = r"^(?=.*\d)(?=.*[a-zA-Z]).{5,}$"
    return re.search(patron, contrasena) is not None

def cargar_datos():
    """ Cargar datos desde el archivo JSON """
    try:
        with open(json_path, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print(f"No se encontró el archivo JSON en {json_path}.")
        return {}
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON.")
        return {}


def guardar_datos():
    """ Guardar datos en el archivo JSON """
    with open(json_path, "w", encoding="utf-8") as archivo:
        json.dump(usuarios, archivo, indent=4)

usuarios = cargar_datos()

def agregar_a_historial(username, tipo, titulo, fecha_limite):
    """ Agrega un nuevo registro al historial del usuario """
    usuarios[username]['historial'].append([tipo, titulo, fecha_limite])


def insertar_eventos(username):
    """ Inserta eventos o tareas para el usuario logueado """
    evento_usuario = True
    while evento_usuario:
        try:
                
            console.print("[bold green]¿Qué quiere insertar?:[/bold green]")
            console.print("""
        [bold cyan](1)[/bold cyan] [bold white]Para insertar un[/bold white] [bold cyan]Evento[/bold cyan]
                        
        [bold cyan](2)[/bold cyan] [bold white]Para insertar una[/bold white] [bold cyan]Tarea[/bold cyan]
                          
        [bold cyan](3)[/bold cyan] [bold green]<< Volver[/bold green]
        """)
            tarea_evento = int(input())
            
            if tarea_evento == 1:
                console.print("\n[bold white]Ingrese el nombre del evento:[/bold white]")
                titulo_evento = input(Fore.CYAN + "").lower().capitalize()
                console.print("\n[bold white]Ingrese la fecha del evento [bold cyan](Dia-Mes-Año)[/bold cyan]:[/bold white]")
                fecha_limite = input(Fore.CYAN + "")
                console.print("\n[bold white]Ingrese la descripción del evento:[/bold white]")
                descripcion = input(Fore.CYAN + "")
                usuarios[username]['eventos'].append({
                    "titulo": titulo_evento,
                    "fecha_limite": fecha_limite,
                    "descripcion": descripcion
                })

                agregar_a_historial(username, "Evento", titulo_evento, fecha_limite)  # Agregar al historial
                guardar_datos()  # Guardar cambios
                console.print(f"\n[bold green] Evento '{titulo_evento}' guardado exitosamente. [/bold green]")

                console.print("\n[bold yellow] ¿Desea seguir agregando eventos o tareas? escriba 'si' o 'no'[/bold yellow]")
                sigue = input(Fore.CYAN + "").lower()

                if sigue != "si":
                    evento_usuario = False

            elif tarea_evento == 2:
                console.print("\n[bold white]Ingrese el nombre de la tarea:[/bold white]")
                titulo_tarea = input(Fore.CYAN + "").lower().capitalize()
                console.print("\n[bold white]Ingrese la fecha de la tarea [bold cyan](Dia-Mes-Año)[/bold cyan]:[/bold white]")
                fecha_limite = input(Fore.CYAN + "")
                console.print("\n[bold white]Ingrese la descripción de la tarea:[/bold white]")
                descripcion = input(Fore.CYAN + "")
                usuarios[username]['tareas'].append({
                    "titulo": titulo_tarea,
                    "fecha_limite": fecha_limite,
                    "descripcion": descripcion
                })

                agregar_a_historial(username, "Tarea", titulo_tarea, fecha_limite)  # Agregar al historial
                guardar_datos()  # Guardar cambios     
                console.print(f"\n[bold green] Tarea '{titulo_tarea}' guardada exitosamente. [/bold green]")
                
                console.print("\n[bold yellow] ¿Desea seguir agregando eventos o tareas? escriba 'si' o 'no'[/bold yellow]")
                sigue = input(Fore.CYAN + "").lower()

                if sigue != "si":
                    evento_usuario = False

            elif tarea_evento == 3:
                evento_usuario =False

            else:
                console.print("\n[bold red]-------------------------------------[/bold red]")
                console.print("[bold red]| Por favor elija una opción válida |[/bold red]")
                console.print("[bold red]-------------------------------------[/bold red]\n")

        except ValueError:
            console.print("\n[bold red]-------------------------------------[/bold red]")
            console.print("[bold red]| ¡Por favor, ingrese solo NUMEROS! |[/bold red]")
            console.print("[bold red]-------------------------------------[/bold red]\n")      


def modificar_eventos(username):
    """ Te permite modificar eventos, tareas y descripciones """

    bandera_modificar = True
    while bandera_modificar:
        try:
            console.print("[bold yellow]¿Qué quiere modificar?:[/bold yellow]")
            console.print("""
        [bold cyan](1)[/bold cyan] [bold white]Para modificar un[/bold white] [bold cyan]Evento[/bold cyan]
                            
        [bold cyan](2)[/bold cyan] [bold white]Para modificar una[/bold white] [bold cyan]Tarea[/bold cyan]
                          
        [bold cyan](3)[/bold cyan] [bold green]<< Volver[/bold green]
        """)
            tarea_evento_modificar = int(input())

            if tarea_evento_modificar == 1:
                if len(usuarios[username]['eventos']) != 0:
                    console.print("\n[bold white]Eventos que puedes modificar:[/bold white]\n")
                    for id_even, evento in enumerate(usuarios[username]['eventos']):
                        console.print(f"[bold cyan]{id_even + 1}.[/bold cyan] [bold white]{evento['titulo']} - {evento['fecha_limite']} - {evento['descripcion']}[/bold white]")

                    console.print("\n[bold cyan]Ingrese el número del evento a modificar:[/bold cyan]")
                    seleccion = int(input()) - 1
                    evento_seleccionado = usuarios[username]['eventos'][seleccion]
                    
                    console.print("\n[bold cyan]¿Qué desea modificar?[/bold cyan]")
                    console.print("""
        [bold cyan](1)[/bold cyan] [bold white]Título[/bold white]
                                
        [bold cyan](2)[/bold cyan] [bold white]Fecha límite[/bold white]
                                
        [bold cyan](3)[/bold cyan] [bold white]Descripción[/bold white]
        """)        
                    opcion_modificar = int(input())

                    if opcion_modificar == 1:
                        console.print("[bold white]Ingrese el nuevo título: [/bold white]")
                        nuevo_titulo = input(Fore.CYAN + "").lower().capitalize()
                        evento_seleccionado['titulo'] = nuevo_titulo
                        guardar_datos()  # Guardar cambios
                        console.print(f"\n[bold green] Título del evento actualizado a '{nuevo_titulo}'. [/bold green]")
                        bandera_modificar = False

                    elif opcion_modificar == 2:
                        console.print("[bold white]Ingrese la nueva fecha límite[/bold white] [bold yellow](Dia-Mes-Año): [/bold yellow]")
                        nueva_fecha = input(Fore.CYAN + "")
                        evento_seleccionado['fecha_limite'] = nueva_fecha
                        guardar_datos()  # Guardar cambios
                        console.print(f"\n[bold green] Fecha límite del evento actualizada a '{nueva_fecha}'. [/bold green]")
                        bandera_modificar = False

                    elif opcion_modificar == 3:
                        console.print("[bold white]Ingrese la nueva descripción: [/bold white]")
                        nueva_descripcion = input(Fore.CYAN + "")
                        evento_seleccionado['descripcion'] = nueva_descripcion
                        guardar_datos()  # Guardar cambios
                        console.print(f"\n[bold green] Descripción del evento actualizada a '{nueva_descripcion}'. [/bold green]")
                        bandera_modificar = False
                    
                else:
                    console.print("\n[bold red]---------------------------------[/bold red]")
                    console.print("[bold red]| No hay eventos para modificar |[/bold red]")
                    console.print("[bold red]---------------------------------[/bold red]")

            elif tarea_evento_modificar == 2:
                if len(usuarios[username]['tareas']) != 0:
                    console.print("\n[bold white]Tareas que puedes modificar:[/bold white]\n")
                    for id_tarea, tarea in enumerate(usuarios[username]['tareas']):
                        console.print(f"[bold cyan]{id_tarea + 1}.[/bold cyan] [bold white]{tarea['titulo']} - {tarea['fecha_limite']} - {tarea['descripcion']}[/bold white]")

                    console.print("\n[bold cyan]Ingrese el número de la tarea a modificar:[/bold cyan]")
                    seleccion = int(input()) - 1
                    tarea_seleccionada = usuarios[username]['tareas'][seleccion]
                    
                    console.print("[bold cyan]¿Qué desea modificar?[/bold cyan]")
                    console.print("""
        [bold cyan](1)[/bold cyan] [bold white]Título[/bold white]
                                
        [bold cyan](2)[/bold cyan] [bold white]Fecha límite[/bold white]
                                
        [bold cyan](3)[/bold cyan] [bold white]Descripción[/bold white]
        """)
                    opcion_modificar = int(input())

                    if opcion_modificar == 1:
                        console.print("[bold white]Ingrese el nuevo título: [/bold white]")
                        nuevo_titulo = input(Fore.CYAN + "").lower().capitalize()
                        tarea_seleccionada['titulo'] = nuevo_titulo
                        guardar_datos()  # Guardar cambios
                        console.print(f"\n[bold green] Título de la tarea actualizado a '{nuevo_titulo}'. [/bold green]")
                        bandera_modificar = False

                    elif opcion_modificar == 2:
                        console.print("[bold white]Ingrese la nueva fecha límite[/bold white] [bold yellow](Dia-Mes-Año): [/bold yellow]")
                        nueva_fecha = input(Fore.CYAN + "")
                        tarea_seleccionada['fecha_limite'] = nueva_fecha
                        guardar_datos()  # Guardar cambios
                        console.print(f"\n[bold green] Fecha límite de la tarea actualizada a '{nueva_fecha}'. [/bold green]")
                        bandera_modificar = False

                    elif opcion_modificar == 3:
                        console.print("[bold white]Ingrese la nueva descripción: [/bold white]")
                        nueva_descripcion = input(Fore.CYAN + "")
                        tarea_seleccionada['descripcion'] = nueva_descripcion
                        guardar_datos()  # Guardar cambios
                        console.print(f"\n[bold green] Descripción de la tarea actualizada a '{nueva_descripcion}'. [/bold green]")
                        bandera_modificar = False
                    
                else:
                    console.print("\n[bold red]--------------------------------[/bold red]")
                    console.print("[bold red]| No hay tareas para modificar |[/bold red]")
                    console.print("[bold red]--------------------------------[/bold red]")
            
            elif tarea_evento_modificar == 3:
                bandera_modificar = False

            else:
                console.print("\n[bold red]-------------------------------------[/bold red]")
                console.print("[bold red]| Por favor elija una opción válida |[/bold red]")
                console.print("[bold red]-------------------------------------[/bold red]\n")
        except ValueError:
            console.print("\n[bold red]-------------------------------------[/bold red]")
            console.print("[bold red]| ¡Por favor, ingrese solo NUMEROS! |[/bold red]")
            console.print("[bold red]-------------------------------------[/bold red]\n")
        except IndexError:
            console.print("\n[bold red]-----------------------------[/bold red]")
            console.print("[bold red]| ¡Ingrese un valor valido! |[/bold red]")
            console.print("[bold red]-----------------------------[/bold red]\n")

def eliminar_eventos(username):
    """ Te permite eliminar eventos o tareas """
    bandera_eliminar = True
    while bandera_eliminar:
        try:
            console.print("[bold red]¿Qué quiere eliminar?:[/bold red]")
            console.print("""
        [bold cyan](1)[/bold cyan] [bold white]Para eliminar un[/bold white] [bold cyan]Evento[/bold cyan]
                        
        [bold cyan](2)[/bold cyan] [bold white]Para eliminar una[/bold white] [bold cyan]Tarea[/bold cyan]
                          
        [bold cyan](3)[/bold cyan] [bold green]<< Volver[/bold green]
        """)
            tarea_evento_eliminar = int(input())

            if tarea_evento_eliminar == 1:
                    if len(usuarios[username]['eventos']) != 0:
                            console.print("\n[bold white]Eventos que puedes eliminar:[/bold white]\n")
                            for id_even, evento in enumerate(usuarios[username]['eventos']):
                                console.print(f"[bold cyan]{id_even + 1}.[/bold cyan] [bold white]{evento['titulo']} - {evento['fecha_limite']}[/bold white]")

                            console.print("\n[bold cyan]Ingrese el número de evento a eliminar:[/bold cyan]")
                            seleccion = int(input()) - 1
                            evento_eliminado = usuarios[username]['eventos'].pop(seleccion)
                            guardar_datos()  # Guardar cambios
                            console.print(f"\n[bold green]***** Se ha eliminado el evento '{evento_eliminado['titulo']}'. *****[/bold green]")
                            bandera_eliminar = False
                    else:
                        console.print("\n[bold red]--------------------------------[/bold red]")
                        console.print("[bold red]| No hay eventos para eliminar |[/bold red]")
                        console.print("[bold red]--------------------------------[/bold red]")

            elif tarea_evento_eliminar == 2:
                if len(usuarios[username]['tareas']) != 0:
                    console.print("\n[bold white]Tareas que puedes eliminar:[/bold white]\n")
                    for id_tarea, tarea in enumerate(usuarios[username]['tareas']):
                        console.print(f"[bold cyan]{id_tarea + 1}.[/bold cyan] [bold white]{tarea['titulo']} - {tarea['fecha_limite']}[/bold white]")

                    console.print("\n[bold cyan]Ingrese el número de tarea a eliminar:[/bold cyan]")
                    seleccion = int(input()) - 1
                    tarea_eliminada = usuarios[username]['tareas'].pop(seleccion)
                    guardar_datos()  # Guardar cambios
                    console.print(f"\n[bold green]***** Se ha eliminado la tarea '{tarea_eliminada['titulo']}'. *****[/bold green]")
                    bandera_eliminar = False
                else:
                    console.print("\n[bold red]-------------------------------[/bold red]")
                    console.print("[bold red]| No hay tareas para eliminar |[/bold red]")
                    console.print("[bold red]-------------------------------[/bold red]")
            
            elif tarea_evento_eliminar == 3:
                bandera_eliminar = False

            else:
                console.print("\n[bold red]--------------------------------------[/bold red]")
                console.print("[bold red]| Por favor, elija una opción válida |[/bold red]")
                console.print("[bold red]--------------------------------------[/bold red]\n")
        except ValueError:
            console.print("\n[bold red]-------------------------------------[/bold red]")
            console.print("[bold red]| ¡Por favor, ingrese solo NUMEROS! |[/bold red]")
            console.print("[bold red]-------------------------------------[/bold red]\n")
        except IndexError:
            console.print("\n[bold red]-----------------------------[/bold red]")
            console.print("[bold red]| ¡Ingrese un valor valido! |[/bold red]")
            console.print("[bold red]-----------------------------[/bold red]\n")

def ver_eventos_pendientes(username):
    """ Muestra los eventos y tareas del usuario logueado """
    if len(usuarios[username]['eventos']) != 0 or len(usuarios[username]['tareas']) != 0:
        console.print(f"\n[bold cyan]Eventos registrados de {username}:[/bold cyan]\n")
        for id_even, evento in enumerate(usuarios[username]['eventos']):
            console.print(f"[bold cyan]{id_even + 1}.[/bold cyan] [bold white]{evento['titulo']} - {evento['fecha_limite']} - {evento['descripcion']}[/bold white]")
            print("---------------------------------------------------------------------------------------------")
        
        console.print(f"\n[bold cyan]Tareas registradas de {username}:[/bold cyan]\n")
        for id_tarea, tarea in enumerate(usuarios[username]['tareas']):
            console.print(f"[bold cyan]{id_tarea + 1}.[/bold cyan] [bold white]{tarea['titulo']} - {tarea['fecha_limite']} - {tarea['descripcion']}[/bold white]")
            print("---------------------------------------------------------------------------------------------")
    
    else:
        console.print("\n[bold red]---------------------------------------[/bold red]")
        console.print("[bold red]| No hay eventos o tareas registrados |[/bold red]")
        console.print("[bold red]---------------------------------------[/bold red]\n")


def ver_proximos_eventos_lambda(username):
    console.print(f"\n[bold yellow]Función en desarrollo:[/bold yellow] [bold white]Próximos eventos de {username}[/bold white]")
    obtener_evento = lambda eventos, tareas: eventos[0] if eventos else (tareas[0] if tareas else None)
    proximo = obtener_evento(usuarios[username]['eventos'], usuarios[username]['tareas'])

    """ Mostrar eventos próximos """
    if proximo:
        console.print(f"\n[bold cyan][1][/bold cyan] [bold white]Próximo evento/tarea: {proximo['titulo']} - {proximo['fecha_limite']} - {proximo['descripcion']}.[/bold white]")
    else:
        console.print("\n[bold red]---------------------------------------[/bold red]")
        console.print("[bold red]| No hay eventos o tareas registrados |[/bold red]")
        console.print("[bold red]---------------------------------------[/bold red]\n")


def ver_historial(username):
    """ Funcion que muestra el historial de el usuario logueado """
    if len(usuarios[username]['historial']) != 0:
        console.print("\n[bold cyan]Historial de Eventos y Tareas:[/bold cyan]\n")
        for registro in usuarios[username]['historial']:
            tipo, titulo, fecha_limite, *_ = registro # El *_ sirve para ignorar las descripciones que vienen de la base de datos
            console.print(f"[bold cyan]{tipo}[/bold cyan][bold white]: {titulo} - {fecha_limite}[/bold white]")
            print("----------------------------------------------")
    else:
        console.print("\n[bold red]--------------------[/bold red]")
        console.print("[bold red]| No hay historial |[/bold red]")
        console.print("[bold red]--------------------[/bold red]\n")


def register():
    """ Funcion para registrarse en la app """

    console.print("[bold green]\n----------------------------[/bold green]")
    console.print("[bold green]| ***** ¡Regístrese! ***** |[/bold green]")
    console.print("[bold green]---------------------------- \n[/bold green]")

    register_usuario = console.input("[bold green] Ingrese un usuario para registrarse [/bold green][bold white](o presione 'enter' para [bold green]<< Volver[/bold green]): [/bold white]").lower().capitalize()
    if register_usuario == "":
        return menu_principal() 
    
    contraseña_valida = False 
    while not contraseña_valida:        
        register_contra = console.input("\n[bold green] Ingrese una contraseña [/bold green][bold white](5 caracteres y al menos 1 numero): [/bold white]").lower().capitalize()
        if validar_contrasena(register_contra):
            contraseña_valida = True
        else:
            console.print("[bold red] Contraseña inválida. Por favor, asegúrese de que tenga al menos 5 caracteres y un número: [/bold red]")
        
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

    console.print("[bold yellow]\n--------------------------------[/bold yellow]")
    console.print("[bold yellow]| ***** Inicio de sesión ***** |[/bold yellow]")
    console.print("[bold yellow]-------------------------------- \n[/bold yellow]")

    username = console.input("[bold yellow]Ingrese su usuario para iniciar sesión[/bold yellow][bold white](o presione 'enter' para [bold green]<< Volver[/bold green]): [/bold white]\n").lower().capitalize()
    if username == "":
        return menu_principal()

    password = console.input("\n[bold yellow]Ingrese su contraseña:[/bold yellow]\n").lower().capitalize()

    """ Verificamos si el usuario existe en el diccionario """
    for usuario, datos in usuarios.items():
        if datos['username'] == username and datos['password'] == password:
            console.print("\n[bold green]------------------------------[/bold green]")
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
        try:
            print(Fore.CYAN + figlet_format("Evenplus App"))
            print(Fore.BLUE + "\n***** Menú Principal *****\n\n")
            console.print("[bold green][1] Registrar usuario[/bold green]\n")
            console.print("[bold yellow][2] Iniciar sesión[/bold yellow]\n")
            console.print("[bold red][3] Salir[/bold red]\n\n")

            opcion = int(input(Fore.BLUE + "Seleccione una opción: "))

            if opcion == 1:
                """ Llamamos a la función de registro """
                register() 

            elif opcion == 2:
                """ Llamamos a la función login y obtenemos la clave del usuario """
                usuario_logeado = login() 

                if usuario_logeado:
                    """ Si el login es exitoso, vamos al menú de usuario """
                    menu_usuario(usuario_logeado)  

            elif opcion == 3:
                console.print("[bold white]\n------------------------------------------------------------[/bold white]")
                console.print("[bold white]| Saliendo de la aplicación... [bold green]¡Gracias por usar EvenPlus![/bold green] | [/bold white]")
                console.print("[bold white]------------------------------------------------------------[/bold white]\n")
            
            else:
                console.print("\n[bold red]--------------------------------------[/bold red]")
                console.print("[bold red]| Opción inválida. Intente de nuevo. |[/bold red]")
                console.print("[bold red]--------------------------------------[/bold red]\n")
        except ValueError:
            console.print("\n[bold red]-------------------------------------[/bold red]")
            console.print("[bold red]| ¡Por favor, ingrese solo NUMEROS! |[/bold red]")
            console.print("[bold red]-------------------------------------[/bold red]\n")



def menu_usuario(username):
    """ El usuario logeado debera elegir la accion que desee. """
    usuario_main = 0
    while usuario_main != 7:
        try:
            print(Fore.CYAN + "\nBienvenido a EvenPlus ", end="")
            console.print(f"{username}", style="bold yellow", end="")
            print(Fore.CYAN + ", tu App para gestionar eventos y tareas.")
            print(Fore.CYAN + "Elija la opción que desee:")
            console.print("""
        
        | [bold cyan](1)[/bold cyan] [bold white]Insertar un Evento[/bold white]     |
        |----------------------------|
        | [bold cyan](2)[/bold cyan] [bold white]Eliminar un Evento[/bold white]     |
        |----------------------------|
        | [bold cyan](3)[/bold cyan] [bold white]Modificar un Evento[/bold white]    |
        |----------------------------|
        | [bold cyan](4)[/bold cyan] [bold white]Ver Eventos Pendientes[/bold white] |
        |----------------------------|
        | [bold cyan](5)[/bold cyan] [bold white]Ver Próximos Eventos[/bold white]   |
        |----------------------------|
        | [bold cyan](6)[/bold cyan] [bold white]Ver Historial[/bold white]          |
        |----------------------------|
        | [bold cyan](7)[/bold cyan] [bold white]Cerrar sesión[/bold white]          |
        
        """)
            
            usuario_main = int(input(Fore.CYAN + "Ingrese el numero de la opción que desea realizar: "))
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
                    print("Cerrando sesión... ¡Vuelva Pronto!\n")
                    console.print("\n[bold yellow]--------------------------------------[/bold yellow]")
                    console.print("[bold yellow]| Cerrando sesión... ¡Vuelva Pronto! |[/bold yellow]")
                    console.print("[bold yellow]--------------------------------------[/bold yellow]\n")

            else:
                console.print("\n[bold red]---------------------------------------------------[/bold red]")
                console.print("[bold red]| ¡Error!, Por favor ingrese un numero del 1 al 7 |[/bold red]")
                console.print("[bold red]---------------------------------------------------[/bold red]")
        except ValueError:
            console.print("\n[bold red]-------------------------------------[/bold red]")
            console.print("[bold red]| ¡Por favor, ingrese solo NUMEROS! |[/bold red]")
            console.print("[bold red]-------------------------------------[/bold red]\n")

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

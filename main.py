eventos = []
tareas = []

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

def main():
    # el usuario debera elegir la accion que desee.
    crud = 0
    while crud != 5:
        print("""
    Bienvenido a EvenPLus tu app para gestionar tareas y eventos.
    Elija la accion que desee:
    (1) Insertar un Evento
    (2) Eliminar un Evento
    (3) Modificar un Evento
    (4) Ver Eventos guardados
    (5) Salir de la App
    """)
        
        crud = int(input("Ingrese el numero de la accion que desea realizar: "))
        if crud == 1:
            # def insertar
            insertar_eventos()

        elif crud == 2:
            # def eliminar
            eliminar_eventos()

        elif crud == 3:
            # def modificar
            modificar_eventos()
            
        elif crud == 4:
            # def ver registros
            ver_eventos_pendientes()
        
        elif crud == 5:
                print("\n----------------------------------------------------------")
                print("Saliendo de la aplicación... ¡Gracias por usar EvenPlus!\n")

        else:
            print("¡Error!, Por favor ingrese un numero del 1 al 5 ")

main()
"""
Faltantes
"""

# Login Logout y create account

# Update de def ingresar_eventos:
#   1 - manejo de tipo de evento (tarea o evento), tarea: es de ingreso facil, evento: pregunta mas cosas
#   2 - pide fecha de evento.

# Update de def ver_eventos_pendientes:
#   1 - ver detalles de eventos

# Memoria de la app

# def modificar_evento
eventos = []

def insertar_eventos():
    # Funcion que inserta eventos.
    evento_usuario = True
    while evento_usuario:
        print("Ingrese un nuevo Evento:")
        evento_usuario = input("")
        eventos.append(evento_usuario)
        print("---------------------------------")
        print("| Evento Guardado ¡Exitosamente!|")
        print("---------------------------------\n")

        print("Desea seguir agregando eventos? escriba 'si' o 'no'")
        sigue = input("").lower()

        if sigue != "si":
            evento_usuario = False
    

def eliminar_eventos():
    # Funcion que elimina registros
    if len(eventos) != 0:
        print(f"Eventos que puedes eliminar:")
        for id, evento in enumerate (eventos):
            print(f"{id + 1}. {evento}")

        print("\nIngrese el numero de evento a eliminar:")
        seleccion = int(input()) -1 # convierte en indice la seleccion con -1
        evento_eliminado = eventos.pop(seleccion)
        print(f"Se ha eliminado el evento {evento_eliminado}")
    else:
        print("---------------------------------")
        print("| ¡No hay eventos que eliminar! |")
        print("---------------------------------")
    
def modificar_eventos():
    # Funcion que modifica eventos
    print("Modificar")

def ver_eventos_pendientes():
    # Funcion para ver registros en memoria
    if len(eventos) != 0:
        print(f"Eventos registrados:")
        for id, evento in enumerate (eventos):
            print(f"{id + 1}. {evento}")
    else:
        print("--------------------------------")
        print("| ¡No hay eventos registrados! |")
        print("--------------------------------")

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
# Update de def ingresar_eventos. pide fecha de evento.

# Memoria en txt

# def modificar_evento
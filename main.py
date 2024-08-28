def insertar_eventos():
    # Funcion que inserta eventos.
    print("Insertar")
    

def eliminar_eventos():
    # Funcion que elimina eventos
    print("Eliminar")
    

def modificar_eventos():
    # Funcion que modifica eventos
    print("Modificar")

def ver_eventos():
    # Funcion para ver eventos en memoria
    print("Eventos en memoria")


def main():
    # el usuario debera elegir la accion que desee.
    print("""
    Bienvenido a EvenPLus tu app para gestionar tareas y eventos.
    Elija la accion que desee:
    (1) Insertar un Evento
    (2) Eliminar un Evento
    (3) Modificar un Evento
    (4) Ver Eventos guardados
    (5) Salir de la App
    """)
    crud = 0
    while crud != 5:
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
            ver_eventos()
        
        elif crud == 5:
                print("Saliendo de la aplicación. ¡Gracias por usar EvenPlus!")

        else:
            print("¡Error!, Por favor ingrese un numero del 1 al 5 ")

main()
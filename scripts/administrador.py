import os

from scripts.usuarios import agregarUsuario, cargar_usuarios, eliminarUsuario
from scripts.utilidades import recibirOpcion, findDicsInList


def panelAdmin():
    while True:
        os.system("cls")
        print("## PANEL DE ADMINISTRADOR ##")
        _opPanel = recibirOpcion(input(".- Concurso -.\n"
                                       "1 - Terminar concurso\n"
                                       "2 - Cerrar Registro\n"
                                       "\n"
                                       ".- Videojuegos -.\n"
                                       "3 - Ver mejores puntuaciones\n"
                                       "4 - Descalificar videojuego\n"
                                       "\n"
                                       ".- Usuarios -.\n"
                                       "6 - Agregar un nuevo juez.\n"
                                       "7 - Eliminar un usuario.\n"
                                       "8 - Ver lista de jueces\n"
                                       "\n"
                                       "9 - Cerrar sesion"
                                       "\n¿Qué opción deseas? : "), 9)

        # Agregar un nuevo juez. #
        if _opPanel == 6:
            rango = "juez"
            agregarUsuario(rango)
            print("El nuevo {} ha sido creado con exito.".format(rango))
            os.system("pause")

        # Eliminar usuario. #
        if _opPanel == 7:
            while True:
                os.system("cls")
                nombreUsuario = input("Introduce el nombre del usuario a eliminar: ")
                if eliminarUsuario(nombreUsuario):
                    print("Usuario '{}' eliminado exitosamente.".format(nombreUsuario))
                    os.system("pause")
                    break
                else:
                    print("Usuario '{}' no existe.".format(nombreUsuario))
                    opcion = recibirOpcion(input("\n 1 - Reintentar con otro usuario."
                                                 "\n 2 - Salir"
                                                 "\n¿Qué opción desea? : "), 2)
                    if opcion == 2:
                        break

        # Ver lista de jueces. #
        if _opPanel == 8:
            os.system("cls")
            listaJueces = findDicsInList(cargar_usuarios(), rango="juez")
            if listaJueces is None:
                print("Aún no has registrado jueces.")
            else:
                print("## Lista de JUECES ##\n")
                for dicJuez in listaJueces:
                    print(" + Nombre: {}"
                          "\n   Usuario: {}"
                          "\n   Correo: {}\n"
                          .format(dicJuez.get("nombre"),
                                  dicJuez.get("usuario"),
                                  dicJuez.get("correo")))
                os.system("pause")

        # Salir. #
        if _opPanel == 9:
            break
from Usuario import Usuario
from Estudiante import Estudiante, TIPO_ARCHIVO
from Profesor import Profesor

def main ():


    usuarios = []

    while True:
        print("+---------Tabla----------+")
        print("Digite 1 si quiere registrar un nuevo usuario")
        print("Digite 2 si desea probar un metodo con valores especifios")
        print("Digite 3 si desea salir")

        respuesta = input("Seleccione una opcion")
        if respuesta =="1" :
            print("+-----------------------------+")
            print("+-1 para registrar estudiante-+")
            print("+-2 para registrar un profesor")

            user_selector=input("")

            if user_selector == "1":
                nombre = input("Ingrese el nombre del estudiante")
                id_user = input("Digite el ID del estudiante")
                contraseña = input("Ingrese la contraseña")
                new_student = Estudiante(nombre, id_user, contraseña)
                usuarios.append(new_student)
                print("Se ha añadido el estudiante " + nombre + " con exito")

            elif user_selector == "2":
                nombre = input("Ingrese el nombre del docente")
                id_profesor = input("Ingrese el ID del docente")
                contraseña = input("Ingrese la contraseña")
                new_teacher = Profesor(nombre, id_profesor, contraseña)
                usuarios.append(new_teacher)

            else: return "EXIT_SUCCES"

        elif respuesta == 2 and len(usuarios) >0:
            print("+------Tabla------+")
            print("+- 1 Para estudiantes -+")
            print("+- 2 Para docentes -+")

            option = input("")

            if option == "1":
                pass



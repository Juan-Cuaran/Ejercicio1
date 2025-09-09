from Usuario import Usuario
from Estudiante import Estudiante, TIPO_ARCHIVO
from Profesor import Profesor
import pandas as pd

def main ():

    usuarios = []

    while True:
        print("+--------------------------Tabla-----------------------------+")
        print("+-Digite 1 si quiere registrar un nuevo usuario -------------+")
        print("+-Digite 2 si desea probar un metodo con valores especifios -+")
        print("+-Digite 3 si desea salir -----------------------------------+")
        print("+------------------------------------------------------------+")
        respuesta = input("Seleccione una opcion")
        if respuesta =="1" :
            print("+--------------Registro---------------+")
            print("+------1 para registrar estudiante----+")
            print("+------2 para registrar un profesor---+")
            print("+-------------------------------------+")
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

            else: return ""

        elif respuesta == 2 and len(usuarios) >0:
            print("+------Tabla------+")
            print("+- 1 Para estudiantes -+")
            print("+- 2 Para docentes -+")

            option = input("Digite su opcion")

            if option == "1":
                estudiantes = [u for u in usuarios if isinstance(u, Estudiante)]
                
                if not estudiantes:
                    print("No hay estudiantes registrados.")
                else:
                    dataset = {
                        "Num": [i+1 for i in range (len(estudiantes))],
                        "Nombre": [n._Nombre for n in estudiantes],
                        "ID": [id._ID for id in estudiantes]
                    }
                    df = pd.DataFrame(dataset)
                    print("Listado de estudiantes")
                    print(df)

                    idx = int(input("Seleccione el indice del estudiante"))-1
                    estudiante_seleccionado = estudiantes[idx]  # Corregido: usar objeto original        
                    while True:
                            print("+------ Métodos Estudiante ------+")
                            print("1. Añadir curso")
                            print("2. Mostrar cursos")
                            print("3. Enviar tarea")
                            print("4. Participar en foro")
                            print("5. Volver al menú principal")
                            print("+--------------------------------+")
                            metodo = input("Seleccione el método que quiere probar: ")

                            if metodo == "1":
                                curso = input("Digite el nombre del curso: ")
                                estudiante_seleccionado.AñadirCursos(curso)

                            elif metodo == "2":
                                cursos = estudiante_seleccionado.MostrarCursos()
                                if cursos:
                                    print("Cursos del estudiante:", cursos)
                                else:
                                    print("El estudiante no tiene cursos registrados.")

                            elif metodo == "3":
                                tarea = input("Digite el nombre de la tarea: ")
                                print("Seleccione el tipo de archivo: ")
                                print("1. WORD")
                                print("2. PDF")
                                tipo = input("Opción: ")
                                if tipo == "1":
                                    estudiante_seleccionado.EnviarTarea(tarea, TIPO_ARCHIVO.WORD)
                                elif tipo == "2":
                                        estudiante_seleccionado.EnviarTarea(tarea, TIPO_ARCHIVO.PDF)

                            elif metodo == "4":
                                tema = input("Digite el tema del foro: ")
                                mensaje = input("Digite el mensaje: ")
                                estudiante_seleccionado.ParticipacionForo(tema, mensaje)

                            elif metodo == "5":
                                break
    
                            else:
                                print("Opción inválida")
        
            elif option == 2:
                profesores = [x for x in usuarios if isinstance(x, Profesor)]

                if not profesores:
                    return "No hay docentes registrados"
                else:
                    data_profes = {
                        "Num": [i for i in range(len((profesores)))],
                        "Nombre": [p._Nombre for p in profesores],
                        "ID": [ide._ID for ide in profesores]
                    }
                    de = pd.DataFrame(data_profes)

                    print("Listado de profes")
                    print(de)

                    index = int(input("Digite el numero del profesor segun el indice del inicio"))-1    
                    profesor_seleccionado = profesores[index]  
                    while True:
                        print("+------ Métodos Profesor ------+")
                        print("1. Añadir clases virtuales")
                        print("2. Subir material")
                        print("3. Volver al menú principal")
                        print("+------------------------------+")
                        metodo = input("Seleccione el método que quiere probar: ")

                        if metodo == "1":
                            name = input("Digite el nombre de la reunión: ")
                            fecha = input("Digite la fecha de la clase: ")
                            profesor_seleccionado.AñadirClasesVirtuales(name, fecha)

                        elif metodo == "2":
                            nombre_archivo = input("Digite el nombre del archivo: ")
                            print("Escoja el formato para subir el archivo:")
                            print("1. PDF")
                            print("2. WORD")
                            formato = input("Seleccione una opción: ")
                            if formato == "1":
                                profesor_seleccionado.SubirMaterial(TIPO_ARCHIVO.PDF, nombre_archivo)
                            elif formato == "2":
                                profesor_seleccionado.SubirMaterial(TIPO_ARCHIVO.WORD, nombre_archivo)

                        elif metodo == "3":
                            break
                        else:
                                print("Opción inválida")